from gamelib import *

game=Game(800,750,"Character Movement")
bk=Image("Dojo_Background.JPG",game)
bk.resizeTo(800,750)
game.setBackground(bk)
#Ninja
#Graphics
index = []
Ninja= Animation("MOVES2.png",5,game,356/3,377/3,2)
#Swords
sword = Image("weapon1.png",game)
sword2 = Image("weapon2.png",game)
sword3 = Image("weapon3.png",game)
sword4 = Image("weapon4.png",game)
sword5 = Image ("weapon5.png",game)
sword6 = Image ("weapon6.png",game)
sword7 = Image ("weapon7.png",game)
sword8 = Image ("weapon8.png",game)
#Ninja Stars
stars = Image("Ninja_star.png",game)
stars2 = Image("Ninja_star2.PNG",game)
stars3 = Image("Ninja_star3.PNG",game)
stars4 = Image("Ninja_star4.PNG",game)
stars5 = Image("Ninja_star5.PNG",game)
stars6 = Image("Ninja_star6.PNG",game)
stars7 = Image("Ninja_star7.PNG",game)
stars8 = Image("Ninja_star8.PNG",game)
#Lose/Win Images
dead=Image("Dead_Ninja.JPG",game)
lose=Image("Loser.PNG",game)
bk2=Image("bamboo forest.jpg",game)
#Background
instructions = Image("instructions.png",game)
back=Image("BACK.png",game)
#Title Screen
Tutorialtext=Image("TUTORIALTEXT.png",game)
end = Image("QUIT.png",game)
play = Image("play.png",game)
Win= Image("win.png",game)
Story=Image("STORYLINE.png",game)
StoryText=Image("story.png",game)
winpose=Image("Cartoon Ninja.JPG",game)
#Image Resizing and Positioning
winpose.resizeBy(-70)
dead.resizeBy(-70)
back.resizeBy(-40)
back.moveTo(game.width-100,game.height-100)
Story.moveTo(instructions.x-10,instructions.y+300)
StoryText.moveTo(game.width-400,game.height-300)
Story.resizeBy(-40)
StoryText.resizeBy(-71)
back.visible=False
Tutorialtext.visible=False
StoryText.visible=False
play.resizeBy(-40)
Tutorialtext.resizeBy(-69)
play.y +=89
instructions.resizeBy(-40)
instructions.moveTo(play.x,play.y+100)
Tutorialtext.moveTo(game.width-400,game.height-300)
end.resizeBy(-40)

bar=Animation("bar.png",3,game,2100/3,110)
bar.moveTo(bar.x,game.height-50)
bar.resizeBy(30)
#Sword Positioning and Speed
sword.moveTo(450,290)
sword2.moveTo(610,400)
sword3.moveTo(540,520)
sword4.moveTo(510,320)
sword5.moveTo(200,470)
sword6.moveTo(320,460)
sword7.moveTo(500,420)
sword8.moveTo(420,450)
sword.resizeBy(-50)
sword2.resizeBy(-50)
sword3.resizeBy(-50)
sword4.resizeBy(-50)
sword5.resizeBy(-50)
sword6.resizeBy(-50)
sword7.resizeBy(-50)
sword8.resizeBy(-50)
Ninja.moveTo(bar.x,bar.y-100)
#Ninja Stars Positioning and Speed
stars.resizeBy(-95)
stars.moveTo(700,500)
stars.setSpeed(10,40)
stars2.resizeBy(-95)
stars2.moveTo(283,200)
stars2.setSpeed(10,382)
stars3.resizeBy(-95)
stars3.moveTo(291,230)
stars3.setSpeed(10,710)
stars4.resizeBy(-95)
stars4.moveTo(145,125)
stars4.setSpeed(10,459)
stars5.resizeBy(-95)
stars5.moveTo(189,135)
stars5.setSpeed(10,504)
stars6.resizeBy(-95)
stars6.moveTo(130,140)
stars6.setSpeed(10,210)
stars7.resizeBy(-95)
stars7.moveTo(210,150)
stars7.setSpeed(10,239)
stars8.resizeBy(-95)
stars8.moveTo(100,140)
stars8.setSpeed(10,300)
jumping = False
factor = 1
landed = False
a=randint(2,320)
collected=0
#Sound
hit=Sound("oof.wav",1)
collect=Sound("collect.wav",2)
song=Sound("song.wav",3)



song.play()
#Title Screen
while not game.over:
    #Image Draw
    game.processInput()
    bk2.draw()
    instructions.draw()
    play.draw()
    Tutorialtext.draw()
    back.draw()
    Story.draw()
    StoryText.draw()
    
    #Start Game
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    #Game Quit
    if end.collidedWith(mouse) and mouse.LeftClick:
        game.quit()
    #Instructions
    if instructions.collidedWith(mouse) and mouse.LeftClick:
        play.visible=False
        end.visible=False
        instructions.visible=False
        back.visible=True
        Tutorialtext.visible=True
        Story.visible=False
    #to go back to title screen
    if back.collidedWith(mouse) and mouse.LeftClick:
        play.visible=True
        end.visible=True
        instructions.visible=True
        back.visible=False
        Tutorialtext.visible=False
        Story.visible=True
        StoryText.visible=False
    #Storyline
    if Story.collidedWith(mouse) and mouse.LeftClick:
        play.visible=False
        end.visible=False
        instructions.visible=False
        back.visible=True
        StoryText.visible=True
        Story.visible=False

    game.update(30)

game.over = False
#Game Loop
while not game.over:
    game.processInput()
    bk.draw()
    Ninja.draw()
    sword.draw()
    sword2.draw()
    sword3.draw()
    sword4.draw()
    sword5.draw()
    sword6.draw()
    sword7.draw()
    sword8.draw()
    Ninja.stop()#stops animating (displays last frame)

    if end.collidedWith(mouse) and mouse.LeftClick:
        game.quit()
    
    if keys.Pressed[K_RIGHT]:
        Ninja.nextFrame() #advances one frame at a time
        Ninja.x +=5 #moves to right
        
    if keys.Pressed[K_LEFT]:
        
        Ninja.prevFrame() # retreats one frame at a time
        Ninja.x -=5 #moves to left

    if Ninja.collidedWith(bar) and Ninja.y>=game.height-50:
        Ninja.y+=0
        
    stars.move(True)
    stars3.move(True)
    stars4.move(True)
    stars5.move(True)
    stars6.move(True)
    stars7.move(True)      
    stars8.move(True)




    if Ninja.collidedWith(sword):
        sword.visible=False
        collected+=1

    if Ninja.collidedWith(sword2):
        sword2.visible=False
        collected+=1

    if Ninja.collidedWith(sword2):
        sword2.visible=False
        collected+=1

    if Ninja.collidedWith(sword3):
        sword3.visible=False
        collected+=1

    if Ninja.collidedWith(sword4):
        sword4.visible=False
        collected+=1
    if Ninja.collidedWith(sword5):
        sword5.visible=False
        collected+=1
    if Ninja.collidedWith(sword6):
        sword6.visible=False
        collected+=1
    if Ninja.collidedWith(sword7):
        sword7.visible=False
        collected+=1
    if Ninja.collidedWith(sword8):
        sword8.visible=False
        collected+=1
    if Ninja.collidedWith(stars):
        Ninja.health-=25
        stars.visible=False
        hit.play()

    if Ninja.collidedWith(stars3):
        Ninja.health-=25
        stars3.visible=False
        hit.play()
    if Ninja.collidedWith(stars4):
        Ninja.health-=25
        stars4.visible=False
        hit.play()
    if Ninja.collidedWith(stars5):
        Ninja.health-=25
        stars5.visible=False
        hit.play()
    if Ninja.collidedWith(stars6):
        Ninja.health-=25
        stars6.visible=False
        hit.play()
    if Ninja.collidedWith(stars7):
        Ninja.health-=25
        stars7.visible=False
        hit.play()
    if Ninja.collidedWith(stars8):
        Ninja.health-=25
        stars8.visible=False
        hit.play()
    #if you lose
    if Ninja.health<=0:
        lose.moveTo(400,300)
        Ninja.visible=False
        sword.visible=False
        sword2.visible=False
        sword3.visible=False
        sword4.visible=False
        sword5.visible=False
        sword6.visible=False
        sword7.visible=False
        sword8.visible=False
        stars.visible=False
        stars2.visible=False
        stars3.visible=False
        stars4.visible=False
        stars5.visible=False
        stars6.visible=False
        stars7.visible=False
        stars8.visible=False
        dead.moveTo(400,500)
        dead.visible=True
        end.moveTo(700,650)
        end.visible=True
      
            

    
    
    #if you win
    if collected>=8:
        Win.moveTo(400,300)
        Ninja.visible=False
        stars.visible=False
        stars2.visible=False
        stars3.visible=False
        stars4.visible=False
        stars5.visible=False
        stars6.visible=False
        stars7.visible=False
        stars8.visible=False
        winpose.moveTo(400,500)
        winpose.visible=True
        end.moveTo(700,650)
        end.visible=True

    game.drawText("Health: " + str(Ninja.health),Ninja.x - 20,Ninja.y + 50)
    



    #while jumping:
        #smurf[index].append(Animation("jump.png",2,game,238/2,124,3))
    
    if jumping:
        Ninja.y -= 31 * factor 
        factor *= .95
        landed = False
    if factor < .31:
        jumping = False
        factor = 1
    if keys.Pressed[K_SPACE] and Ninja.collidedWith(bar) and not jumping:
        jumping = True
    if not Ninja.collidedWith(bar,"rectangle"):
        Ninja.y += 12
        


    game.update(30)

#game.quit()
