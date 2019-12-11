# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:56:35 2019

@author: Brahim
"""

import tkinter as tk
from random import randint

class game:
    # The main class which contains every method and elements in order to run the application
    over = False
    
    
    def __init__(self): #Initialisation of the dimension of my window
        
        self.width = 800
        self.height = 800
        #In order to display the window
        self.create_window()
        

    def create_window(self):
        #Creation of the window
        self.window = tk.Tk()
        self.window.title("Space Invaders")
        self.window.geometry("1000x800")
        #Create the widget for placing elements like button and others.
        self.game_area = tk.Canvas(self.window,width = self.width,height = self.height)
        self.game_area.grid(row = 0, column = 0)
        
        self.setbackground('')
        
        self.set_text()
        
        self.settings_default()
        
        self.game_area.pack()
        
        self.create_controls()
        
        self.window.mainloop()
        
    
    def set_text(self):
        self.text_start = tk.StringVar()
        self.text_start.set('Start Game')
        
        self.text_finish = tk.StringVar()
        self.text_finish.set('Exit Game')
        
        self.text_options = tk.StringVar()
        self.text_options.set('Options')
        
        self.text_difficulty = tk.StringVar()
        self.text_difficulty.set('Difficulty')
        
        self.text_language = tk.StringVar()
        self.text_language.set('Language')
        
        self.text_controls = tk.StringVar()
        self.text_controls.set('Controls')
        
        self.text_previous = tk.StringVar()
        self.text_previous.set('Previous')
        
        self.textedifact = tk.StringVar()
        self.textedifact.set('Normal')

        self.text_normal = tk.StringVar()
        self.text_normal.set('Normal')        
        
        self.text_hard = tk.StringVar()
        self.text_hard.set('Hard')
        
        self.text_english = tk.StringVar()
        self.text_english.set('English')
    
        self.text_french = tk.StringVar()
        self.text_french.set('French')
    
        self.text_japanese = tk.StringVar()
        self.text_japanese.set('Japanese')
        
        self.text_valid = tk.StringVar()
        self.text_valid.set('Valid')
        
        self.text_right = tk.StringVar()
        self.text_right.set('Choose the right arrow key')

        self.text_left = tk.StringVar()
        self.text_left.set('Choose the left arrow key')      
        
        self.text_space = tk.StringVar()
        self.text_space.set('Choose the space arrow key')     
        
    def settings_default(self):
        # In order to change the key in the option menu
        self.key_l = '' 
        self.key_r = ''
        self.key_s = ''
        
        self.nb_row = 3 # Number of aliens per column
        self.nb_col = 5 # Number of aliens per row
        
            
    def setbackground(self, path_img):
        #If no image has been given as parameter, a standard image is loaded
        if path_img == '':
            self.img = tk.PhotoImage(file = 'menu.png', format = 'png')
            self.bg  = self.game_area.create_image(0,0,anchor = 'nw',image = self.img)
        else:
            self.img = tk.PhotoImage(file = path_img, format = 'png')
            self.bg  = self.game_area.create_image(0,0,anchor = 'nw',image = self.img)
    
    def create_controls(self):
        #Button for Start Game
        self.bool_options = False
        
        self.nuke_blown = tk.PhotoImage(file = 'nuclear.gif', format = 'gif')
        self.blown_up = []
        
        self.new_game = tk.Button(self.game_area, textvariable = self.text_start, command = self.start_game, fg ="white", background =  "#110d1a",font = "helvetica") # création du bouton start
        self.new_game.pack()
        self.new_game.place(relx = 0.5, rely = 0.5,anchor = 'n')
        
        #Button for Finish Game
        self.finish_game = tk.Button(self.game_area, textvariable = self.text_finish, command = self.exit_game,fg="white", background = "#110d1a", font = "helvetica")
        self.finish_game.pack()
        self.finish_game.place(relx = 0.5,rely = 0.7, anchor = 'n')
        #Button for Options
        self.button_option = tk.Button(self.game_area, textvariable = self.text_options, command = self.options,fg="white", background = "#110d1a", font = "helvetica")
        self.button_option.pack()
        self.button_option.place(relx = 0.5, rely = 0.9, anchor = 'n')
    
# The main menu 
        
    def start_game(self):
        #Destroy the buttons of the main menu
        
        self.new_game.destroy()
        self.button_option.destroy()
        self.finish_game.destroy()
        
        self.game_background = tk.PhotoImage(file = 'jeu.png', format = 'png')
        self.game_area.itemconfigure (self.bg, image = self.game_background) # Changement d'image de fond 
        
        #Start the game, place Quit Game, Score and Life at the East corner
        
        self.finish_game = tk.Button(self.window,textvariable = self.text_finish, command = self.exit_game,fg="white", background = "#110d1a", font = "helvetica")
        self.finish_game.pack()
        self.finish_game.place(relx = 0.9,rely = 0.4)
        
        
        self.score_int = 0
        self.score = tk.StringVar()
        self.score.set(self.score_int)
        
        self.life = tk.StringVar()
        self.life_int = 1
        self.life.set(self.life_int)
        
        self.Label_life = tk.Label(self.window,text = 'Life : ')
        self.Label_Score = tk.Label(self.window,text = 'Score : ')
    
        self.Label_life.pack()
        self.Label_life.place(relx = 0.9, rely = 0.1)
    
        self.Label_Score.pack()
        self.Label_Score.place(relx = 0.9, rely = 0.2)
        
        self.Text_Life = tk.Label(self.window,textvariable = self.life)
        self.Text_Life.pack()
        self.Text_Life.place(relx = 0.95, rely = 0.1)
        
        self.Text_Score = tk.Label(self.window,textvariable = self.score)
        self.Text_Score.pack()
        self.Text_Score.place(relx = 0.95, rely = 0.2)
        
        # End Label and Text
        
        #Enabling the first wave
        self.wave = 1
        
        self.create_aliens()
        self.move_aliens()
        
        if self.key_l == '' or self.key_r == '' or self.key_s == '':
            self.key_l = 'Left'
            self.key_r = 'Right'
            self.key_s = 'space'
            
        self.player = player(self,self.game_area,self.window,self.width,self.height, self.key_l, self.key_r, self.key_s)
        self.buildings = buildings(self.game_area,self.width,self.height)
        
   
    def exit_game(self):
        self.window.destroy()
            
    def language(self):
        
        self.bool_language = True
        
        self.button_language.destroy()
        self.button_controls.destroy()
        self.button_difficulty.destroy()
        self.button_previous.destroy()
        
        self.button_english = tk.Button(self.window, textvariable = self.text_english,fg="white",command = self.english, background = "#110d1a", font = "helvetica")
        self.button_english.pack()
        self.button_english.place(relx = 0.5,rely = 0.3, anchor = 'n')
            
        self.button_french = tk.Button(self.window, textvariable = self.text_french,fg="white",command = self.french, background = "#110d1a", font = "helvetica")
        self.button_french.pack()
        self.button_french.place(relx = 0.5,rely = 0.5, anchor = 'n')
        
        self.button_japanese = tk.Button(self.window, textvariable = self.text_japanese,fg="white",command = self.japanese, background = "#110d1a", font = "helvetica")
        self.button_japanese.pack()
        self.button_japanese.place(relx = 0.5,rely = 0.7, anchor = 'n')
            
        self.button_previous = tk.Button(self.window, textvariable = self.text_previous,fg="white", command = self.previous, background = "#110d1a", font = "helvetica")
        self.button_previous.pack()
        self.button_previous.place(relx = 0.1,rely = 0.9, anchor = 'n')
        
    def difficulty(self):
        
        self.bool_difficulty = True
        
        self.button_language.destroy()
        self.button_controls.destroy()
        self.button_difficulty.destroy()
        
        self.difficulty_now = self.game_area.create_text(400,100,text = self.textedifact.get(), fill = 'red', font = ("helvetica",30))
        
        self.button_normal = tk.Button(self.window, textvariable = self.text_normal,command = self.normal,fg="white", background = "#110d1a", font = "helvetica")
        self.button_normal.pack()
        self.button_normal.place(relx = 0.5,rely = 0.5, anchor = 'n')
        
        self.button_hard = tk.Button(self.window, textvariable = self.text_hard,command = self.hard, fg="white", background = "#110d1a", font = "helvetica")
        self.button_hard.pack()
        self.button_hard.place(relx = 0.5,rely = 0.7, anchor = 'n')
        
    def normal(self):
        self.game_area.delete(self.difficulty_now)
        self.textedifact.set('Normal')
        self.difficulty_now = self.game_area.create_text (400,100,text = self.textedifact.get(), fill = 'red', font = ("helvetica",30))
        
    def hard(self):
        self.game_area.delete(self.difficulty_now)
        self.textedifact.set('Hard')
        self.difficulty_now = self.game_area.create_text (400,100,text = self.textedifact.get(), fill = 'red', font = ("helvetica",30))
        
        self.nb_row = 4
        self.nb_col = 6
        
    def english(self):
        self.set_text()

    def french(self):
        self.text_start.set('Commencer')
        
        self.text_finish.set('Quitter')
        
        self.text_options.set('Options')
        
        self.text_difficulty.set('Difficulté')
        
        self.text_language.set('Langue')
    
        self.text_controls.set('Commandes')

        self.text_previous.set('Precedent')
        
        self.textedifact.set('Normal')

        self.text_normal.set('Normal')        
        
        self.text_hard.set('Difficile')
        
        self.text_english.set('Anglais')
    
        self.text_french.set('Francais')
        
        self.text_japanese.set('Japonais')
        
        self.text_valid.set('Valider')
        
        self.text_right.set('Touche de déplacement droite')
        
        self.text_left.set('Touche de déplacement gauche')      
        
        self.text_space.set('Tirer')   
        
        
    def japanese(self):
        
        self.text_start.set('スタート')
        
        self.text_finish.set('休暇')
        
        self.text_options.set('オプション')
        
        self.text_difficulty.set('難しさ')
        
        self.text_language.set('言語')
    
        self.text_controls.set('キー')

        self.text_previous.set('前')
        
        self.textedifact.set('通常レベル')

        self.text_normal.set('通常レベル')        
        
        self.text_hard.set('難しいレベル')
        
        self.text_english.set('英語')
    
        self.text_french.set('フランス語')
        
        self.text_japanese.set('日本語')
        
        self.text_valid.set('検証')
        
        self.text_right.set('右矢印キー')
        
        self.text_left.set('左矢印キー')      
        
        self.text_space.set('ファイア')   

        
    def controls(self): 
        
        self.bool_controls = True
        
        self.button_language.destroy()
        self.button_controls.destroy()
        self.button_difficulty.destroy()
        
        self.entry_left = tk.Entry(self.window)
        self.entry_left.pack()
        self.entry_left.place(relx = 0.6,rely = 0.3, anchor = 'n')
        
        self.entry_right = tk.Entry(self.window)
        self.entry_right.pack()
        self.entry_right.place(relx = 0.6,rely = 0.5, anchor = 'n')
        
        self.entry_space = tk.Entry(self.window)
        self.entry_space.pack()
        self.entry_space.place(relx = 0.6,rely = 0.7, anchor = 'n')
        
        self.button_changer = tk.Button(self.window, textvariable = self.text_valid,fg="white", command = self.change, background = "#110d1a", font = "helvetica")
        self.button_changer.pack()
        self.button_changer.place(relx = 0.5,rely = 0.9, anchor = 'n')
        
        self.textdroite = self.game_area.create_text (200,410,text = self.text_right.get(), fill = 'red', font = ("helvetica",15))    
        self.textgauche = self.game_area.create_text (200,250,text = self.text_left.get(), fill = 'red', font = ("helvetica",15))     
        self.textespace = self.game_area.create_text (200,570,text = self.text_space.get(), fill = 'red', font = ("helvetica",15))    
    
    def change(self):
        self.key_r = ''+self.entry_right.get()
        self.key_l = ''+self.entry_left.get()
        self.key_s = ''+self.entry_space.get()  
        
        
    def previous(self):
        if self.bool_options:
            self.bool_options = False 
            
            self.button_language.destroy()
            self.button_controls.destroy()
            self.button_difficulty.destroy()
            self.button_previous.destroy()
            
            self.create_controls()
            
        if self.bool_language:
            self.bool_language = False
            
            self.button_english.destroy()
            self.button_french.destroy()
            self.button_japanese.destroy()
            self.options()
        
        if self.bool_controls:
            self.bool_controls = False
            self.entry_left.destroy()
            self.entry_right.destroy()
            self.entry_space.destroy()
            self.button_changer.destroy()
            
            self.game_area.delete(self.textdroite)
            self.game_area.delete(self.textgauche)
            self.game_area.delete(self.textespace)
            
            self.options()
            
            
        if self.bool_difficulty:
            
            self.bool_difficulty = False 
            
            self.button_normal.destroy()
            self.button_hard.destroy()
            self.game_area.delete(self.difficulty_now)
            
            self.options()
            
            
        
    def options(self):
        
        print("Je suis la")
        self.bool_options = True
        self.bool_language = False
        self.bool_controls = False
        self.bool_difficulty = False
        
        self.button_option.destroy()
        self.new_game.destroy()
        self.finish_game.destroy()
        
        self.button_language = tk.Button(self.window, textvariable = self.text_language,fg="white",command = self.language, background = "#110d1a", font = "helvetica")
        self.button_language.pack()
        self.button_language.place(relx = 0.5,rely = 0.5, anchor = 'n')
        
        self.button_controls = tk.Button(self.window, textvariable = self.text_controls,fg="white",command = self.controls, background = "#110d1a", font = "helvetica")
        self.button_controls.pack()
        self.button_controls.place(relx = 0.5,rely = 0.7, anchor = 'n')
        
        self.button_difficulty = tk.Button(self.window, textvariable = self.text_difficulty,fg="white",command = self.difficulty, background = "#110d1a", font = "helvetica")
        self.button_difficulty.pack()
        self.button_difficulty.place(relx = 0.5,rely = 0.3, anchor = 'n')
        
        self.button_previous = tk.Button(self.window, textvariable = self.text_previous,fg="white", command = self.previous, background = "#110d1a", font = "helvetica")
        self.button_previous.pack()
        self.button_previous.place(relx = 0.1,rely = 0.9, anchor = 'n')
        
        
        
# Create aliens after pushing the start game button
    
    def create_aliens(self):

        dist = 100 # Distance between two aliens
        coordX = 200
        coordY = 100
        #
        self.alien_line = []
        self.alien_id = []
        
        if self.wave%2 == 1:
            img = 'alian2.gif'
        else:
            img = 'alian3.gif'
            
        self.alien_img = self.extract_gif(img) #permet d'extraire  le gif de l'alien
        for line in range(self.nb_row):
            self.alien_line.append([])
            self.alien_id.append([])
            for column in range(self.nb_col):
                aliens = alien(self,self.window,self.game_area,coordX + dist*column,coordY + dist*line,self.width,self.height,self.alien_img, 'alien')
                self.alien_id[line].append(aliens.id)
                self.alien_line[line].append(aliens)
        self.alien_fire()
            
    def move_aliens(self):
        in_bounds = True
#    y = coordAliens[-1][1]
#    dy = 20
        for i in self.alien_line: # Pour chaque alien, je les deplace de dx
            for alien in i:
                alien.auto_move()
                if alien.in_bounds() == False:
                    in_bounds = False
                alien.is_crashed()
                #self.aliens.auto_move()
        if in_bounds == False:
            for i in self.alien_line:
                for alien in i:
                    alien.dx = -alien.dx
                    if alien.dx > 0:
                        alien.dy = 2
        if game.over == False:
            self.callback = self.window.after(25, self.move_aliens)
        
    def alien_fire(self):
        #methode qui selectionne un alien vivant au hasard pour tirer

        alive_aliens = []

        for line in self.alien_line:
            for alien in line:
                alive_aliens.append(alien)

        if len(alive_aliens) != 0:
            the_one_who_shot = randint(0, len(alive_aliens) - 1)
            alive_aliens[the_one_who_shot].fire()
            
    def delete_alien_by_id(self, alien):
        no_aliens = True
        print(len(self.alien_line))
        # methode qui permet de supprimer un alien de la liste des aliens pouvant tirer lorsqu'il meurt
        for index in range(len(self.alien_id)):
            # For every alien who has been hitting
            if alien in self.alien_id[index]:
                #We delete the canvas
                sub_idx = self.alien_id[index].index(alien)
                self.alien_id[index].remove(alien)
                #And his position
                self.alien_line[index].pop(sub_idx)
                #We take the alien's canvas box and use it for the explosion gif.
                box = self.game_area.bbox(alien)
                self.blown_up.append(self.game_area.create_image(box[0], box[1], anchor = 'nw', image = self.nuke_blown))

                self.window.after(70, self.explosion)
                
                
        for i in self.alien_line:
            for alien in i:
                if len(i) != 0:
                    no_aliens = False
        
        if no_aliens == True:
            self.gagner()
    
    def explosion(self):
        # methode qui gère la disparitions des images d'explosions lors de la destruction des aliens

        self.game_area.delete(self.blown_up[0])
        self.blown_up.pop(0)
                   
        
    def gagner(self):
        self.window.unbind(self.key_l)
        self.window.unbind(self.key_r)
        self.window.unbind(self.key_s)
        print("gagner")
        self.game_area.delete(self.player.id) 
        self.win_img = tk.PhotoImage(file = 'win.png', format = 'png')
        self.game_area.itemconfigure(self.bg, image = self.win_img)
        
    def loose(self):
        self.window.unbind(self.key_l)
        self.window.unbind(self.key_r)
        self.window.unbind(self.key_s)
        print("perdu")
        self.game_area.delete(self.player.id) 
        self.loose_img = tk.PhotoImage(file = 'gameover.png', format = 'png')
        self.game_area.itemconfigure(self.bg, image = self.loose_img)
    
    def extract_gif(self, path):
        #methode qui extrait les  gifs image par image et revoie une liste d'image

        gif = []
        idx = 0
        while True:
            try:
                frt = "gif -index " + str(idx)
                gif.append(tk.PhotoImage(file = path, format = frt))
                idx += 1
            except:
                break
        return gif
    
class alien:
    #class which creates alien
    def __init__(self, parent, window, canvas, init_pos_x, init_pos_y, can_width, can_height, img, tag):
        # method which define the characteristics of my alien at the beginning
        
        #In order to include the alien in the widget, i need to precise which window and which widget
        self.canvas = canvas
        self.window = window
        #We get our window and canevas from our class game, so we precise that the class alien is the children of the class game
        self.parent = parent
        #We get the dimension of our canevas
        self.can_w = can_width
        self.can_h = can_height
        #We get the picture of the alien
        self.img = img
       
#        self.tag = tag
        self.gif_alien = 0
        # Position of the alien
        self.x = init_pos_x
        self.y = init_pos_y
        # Lateral and Vertical Speed
        self.dx = 4 # Absolute speed : (4 pixels)
        self.dy = 0
         #We give a tag to the alien image
        self.tag = tag
        #Create the widget for the alien
        self.id = self.canvas.create_image(self.x, self.y, image = self.img[0], tag = self.tag)
        self.index_img = 1
        
        
    def auto_move(self):
        # méthode qui permet de gérer le gif alien ennemi
        
        self.canvas.move(self.id, self.dx, self.dy)
        self.gif_alien += 1
        if self.gif_alien == 10:
            self.canvas.itemconfig(self.id, image = self.img[self.index_img])
            self.gif_alien = 0
            if self.index_img == 1:
                self.index_img = 0
            else:
                self.index_img = 1

        if self.dy != 0:
            self.dy = 0
        
# If the alien is at the bounds of the screen
    def in_bounds(self):
        x0 = self.canvas.bbox(self.id)[0]
        x1 = self.canvas.bbox(self.id)[2]
        
        if (x0 < 0) or (x1 > self.can_w):
            return False
        else:
            return True
        
    def fire(self, img = ''):
        # méthode qui gére le tir alien
        pos=self.canvas.bbox(self.id)
        self.missile = projectile(self, self.canvas, pos[0] +10, pos[1]-10, self.window, img)
        
    def is_crashed(self):
        # methode qui permet de gerer les colisions
        # distingue si les aliens touche le vaisseau allié, un block

        x0 = self.canvas.bbox(self.id)[0]
        y0 = self.canvas.bbox(self.id)[1]
        x1 = self.canvas.bbox(self.id)[2]
        y1 = self.canvas.bbox(self.id)[3]

        items = self.canvas.find_overlapping(x0, y0, x1, y1)

        if len(items) > 2:

            ids = [i for i in items]
            ids.remove(1)

            aliens_in_list = False
            bloc_in_list = False

            new_id = []

            for i in ids:
                if 'alien' in self.canvas.gettags(i):
                    aliens_in_list = True

                if 'bloc' in self.canvas.gettags(i):
                    bloc_in_list = True
                    new_id.append(i)

                if 'vaisseau' in self.canvas.gettags(i):
                    
                    self.parent.end_game()

            if aliens_in_list and bloc_in_list:
                for i in new_id:                  
                    self.canvas.delete(i)
                    self.parent.delete_alien_by_id(i)
                    
                    
class player:
    #classe qui gère le spaceship allié

    def __init__(self, parent, canvas, window, can_width, can_height, keyl, keyr, keys):
        # Creating the spaceship with the different characteristics : Position, Key event
        # Display etc..
        self.can_w = can_width
        self.can_h = can_height
        self.canvas = canvas
        self.window = window
        self.parent = parent
        self.dx = 10

        self.PosX=self.can_w / 2
        self.PosY=self.can_h

        self.player= tk.PhotoImage(file = 'spaceship.gif', format = 'gif')
        self.id = self.canvas.create_image(self.PosX, self.PosY - 20, image = self.player, tag = 'spaceship')
        self.parent.player_id = self.id
        

        self.key_right = "<"+keyr+">"
        self.key_left = "<"+keyl+">"
        self.key_space = "<"+keys+">"
        self.window.bind(self.key_left,self.gauche)
        self.window.bind(self.key_right, self.droite)
        self.enable_fire()

    def gauche(self, event):
        # méthode qui gère le déplacement du vaisseau vers la gauche
        # ne fait rien si le vaisseau est collé au bord gauche, grâce à l'argument event
        pos=self.canvas.bbox(self.id)

        if pos[0] > 0:
            self.canvas.move(self.id, -self.dx, 0)
        else:
            pass

    def droite(self, event):
        # méthode qui gère le déplacement du vaisseau vers la droite
        # ne fait rien si le vaisseau est collé au bord droit, grâce à l'argument event
        pos=self.canvas.bbox(self.id)

        if pos[2] <= self.can_w:
            self.canvas.move(self.id, self.dx, 0)
        else:
            pass

    def enable_fire(self):
        #Spaceship launching missiles
        self.window.bind(self.key_space, self.fire)


    def fire(self,event):
        # If the key "space" has been pressed, fire will create the missile
        pos=self.canvas.bbox(self.id)
        # Width and height of the projectile 
        self.missile = projectile(self, self.canvas, pos[0]+20, pos[1] + 20, self.window)
        # This line is a condition in order to prevent the player to press too many times the key <space>
        self.fire_rate = self.window.after(1200, self.enable_fire) #fire rate
        
class projectile:

    # Class which create the different projectile for the different class, and manage collisions between the class.

    alive_missiles = []

    def __init__(self, parent, canvas, x, y, window, img = ''):


        self.parent = parent
        self.window = window
        self.canvas = canvas
        self.img = img

        if isinstance(self.parent, player):
            # création d'un tir allié
            self.id = self.canvas.create_rectangle(x,y-25,x+1,y, fill = "red", outline = "red", tag = ('my_shoot','tir'))
            self.window.unbind(self.parent.key_space)
            self.dy = -25

        if isinstance(self.parent, alien):
            # méthode qui permet de faire tirer les aliens
            r = lambda: randint(0,255) # genere un nombre au hasard entre  0 et 255
            a = '#%02X%02X%02X' % (r(),r(),r()) # génere un code couleur, ce qui permet d'avoir une couleur choisit au hasard pour chaque projectil
            if self.img == '':
                self.id = self.canvas.create_rectangle(x,y+50,x+5,y+60, fill = a, outline = a, tag = ('alien_shoot'))
                self.dy = 10
            else:
                self.id = self.canvas.create_image(x,y+100,image = self.img, tag = ('alien_shoot','nuke'))
                self.dy = 8

        projectile.alive_missiles.append(self.id)
        self.auto_move()
    
    def auto_move(self):
        
        if self.id not in self.canvas.find_withtag('all'):
            return
        self.canvas.move(self.id, 0, self.dy)
        x1 = self.canvas.bbox(self.id)[0]
        y1 = self.canvas.bbox(self.id)[1]
        x2 = self.canvas.bbox(self.id)[2]
        y2 = self.canvas.bbox(self.id)[3]
        
        alien_hit = False
        alien_shoot = False
        my_shoot = False
        my_spaceship = False
        
        #☺Overlapped will return a tuple containing the id of each element that collides around the missile  
        overlapped = self.canvas.find_overlapping(x1, y1, x2, y2) # Création d'une "sélection rectangulaire" autour du tir qui doit collidé avec la target
        # Overlapped contains the transmitter of the missile, which is symbolised by the number 1 : we need to get ride off it.
        if len(overlapped) > 2:
            items = [i for i in overlapped]
            # We remove the transmitter of the missile to avoid self collision
            if 1 in items:
                items.remove(1)
                for i in items:
                    # We want to know if the alien_shoot collides with the spaceship or the buildings
                    
                    # If the alien_shoot collided with something else : 
                    if 'alien_shoot' in self.canvas.gettags(i):
                        if alien_shoot:
                            if game.over == False:
                                self.callback = self.window.after(50, self.auto_move)
                                return
                        else:
                            alien_shoot = True

                        
                    # Same we want to know if the shoot collides with alien or building
                    # If my shoot collided with something else : 
                    if 'my_shoot' in self.canvas.gettags(i):
                        my_shoot = True
                        #If the buildings were hit we destroy them.
                    if i in buildings.alive_buildings:
                        buildings.alive_buildings.remove(i)
                    
                    if 'spaceship' in self.canvas.gettags(i):
                        my_spaceship = True
                # If at least one alien has been hitten by my shoot : alien_hit = True
                    for index in range(len(self.parent.parent.alien_id)):
                        if i in self.parent.parent.alien_id[index]:
                            alien_hit = True
                    # If I hit one alien i update my score 
                    if my_shoot and alien_hit:
                        self.parent.parent.score_int += 50
                        self.parent.parent.score.set(self.parent.parent.score_int)
                        
                 # If i hit at least one alien
                if alien_hit and my_shoot:
                    # I search for every alien i hit
                    for i in items:
                        for index in range(len(self.parent.parent.alien_id)):
                            # If a specific alien has been hitting
                            if i in self.parent.parent.alien_id[index]:
                                # I delete the canvas and his position in alien_lines.
                                self.parent.parent.delete_alien_by_id(i)
                                self.canvas.delete(self.id)
                                self.parent.parent.game_area.delete(i)
                #♂ If the alien hit my spaceship
                if alien_shoot and my_spaceship:
                    # I search for 
                    for i in items:
                        
                        if i == self.parent.parent.player_id:
                            self.parent.parent.life_int -= 1
                            self.parent.parent.life.set(self.parent.parent.life_int)
                            if self.parent.parent.life_int == 0:
                                self.parent.parent.loose()
                            tir_aliens = self.canvas.find_withtag('alien_shoot')
                            id_aliens = [i for i in tir_aliens]
                            for k in id_aliens:
                                self.canvas.delete(k)
                        else:
                            self.canvas.delete(i)
                            
                    if isinstance(self.parent, player):
                        self.parent.enable_fire()

                    elif isinstance(self.parent, alien):
                        self.parent.parent.alien_fire()
                    
                else:
                    if game.over == False:
                        self.callback = self.window.after(50, self.auto_move)
                     
                    
            
               
        else:
            if y1 < 0 or y2 > self.parent.can_h:
                self.canvas.delete(self.id)

                if isinstance(self.parent, player):
                    self.parent.enable_fire()

                if isinstance(self.parent, alien):
                    self.parent.parent.alien_fire()
                
            else:
                if game.over == False:
                    self.callback = self.window.after(50, self.auto_move)
                   
        
class buildings:
    # classe qui permet la création des blocs de protection

    alive_buildings = []

    def __init__(self, canvas, can_width, can_height):

        # méthode qui permet de caractériser les blocs de protection

        self.pattern = "00000000000000000000000111111111111111111111"*4 # motif de répartition des blocs de proction
        self.can_w = can_width
        self.can_h = can_height
        self.cote = 4 # largeur
        self.height = 5 # hauteur

        for i in range(self.height):
            for j in enumerate(self.pattern):
                if j == "1":
                    buildings.alive_buildings.append(canvas.create_rectangle(pos*self.cote,self.can_h-(i*self.cote+150), (pos+1)*self.cote, self.can_h-(self.cote*(i+1)+150), fill = "grey", outline = "grey", tag = 'bloc'))

     
game()