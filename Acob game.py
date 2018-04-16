from gamelib import *

game=Game(800,750,"Character Movement")
bk=Image("Dojo_Background.JPG",game)
bk.resizeTo(800,750)
game.setBackground(bk)

#Graphics
index = []
smurf = Animation("MOVES2.png",5,game,356/3,377/3,2)
sword = Image("weapon1.png",game)
sword2 = Image("weapon2.png",game)
sword3 = Image("weapon3.png",game)
sword4 = Image("weapon4.png",game)
stars = Image("Ninja_star.png",game)
stars2 = Image("Ninja_star2.PNG",game)
stars3 = Image("Ninja_star3.PNG",game)
stars4 = Image("Ninja_star4.PNG",game)
stars5 = Image("Ninja_star5.PNG",game)
stars6 = Image("Ninja_star6.PNG",game)
stars7 = Image("Ninja_star7.PNG",game)
stars8 = Image("Ninja_star8.PNG",game)
sword = Image("weapon1.png",game)
sword2 = Image("weapon2.png",game)
sword3 = Image("weapon3.png",game)
sword4 = Image("weapon4.png",game)
sword5 = Image("weapon5.png",game)
dead=Image("Dead_Ninja.JPG",game)
lose=Image("Loser.PNG",game)
bk2=Image("bamboo forest.jpg",game)
instructions = Image("instructions.png",game)
back=Image("BACK.png",game)
Tutorialtext=Image("TUTORIALTEXT.png",game)
end = Image("QUIT.png",game)
play = Image("play.png",game)
Win= Image("win.png",game)
winpose=Image("Cartoon Ninja.JPG",game)
winpose.resizeBy(-70)
dead.resizeBy(-70)
back.resizeBy(-40)
back.moveTo(game.width-100,game.height-100)
back.visible=False
Tutorialtext.visible=False
play.resizeBy(-40)
Tutorialtext.resizeBy(-3)
play.y +=89
instructions.resizeBy(-40)
instructions.moveTo(play.x,play.y+100)
end.moveTo(instructions.x-10,instructions.y+100)
Tutorialtext.moveTo(game.width-400,game.height-300)
end.resizeBy(-40)
Jump= Sound("bounce.wav",1)



bar=Animation("bar.png",3,game,2100/3,110)
bar.moveTo(bar.x,game.height-50)
bar.resizeBy(30)
sword.moveTo(450,290)
sword2.moveTo(610,400)
sword3.moveTo(220,520)
sword4.moveTo(300,320)
sword.resizeBy(-50)
sword2.resizeBy(-50)
sword3.resizeBy(-50)
sword4.resizeBy(-50)
smurf.moveTo(bar.x,bar.y-100)



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

#Sound
collected=0



#Title Screen
while not game.over:
    game.processInput()
    bk2.draw()
    instructions.draw()
    end.draw()
    play.draw()
    Tutorialtext.draw()
    back.draw()
    
    
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    if end.collidedWith(mouse) and mouse.LeftClick:
        game.quit()

    if instructions.collidedWith(mouse) and mouse.LeftClick:
        play.visible=False
        end.visible=False
        instructions.visible=False
        back.visible=True
        Tutorialtext.visible=True

    if back.collidedWith(mouse) and mouse.LeftClick:
        play.visible=True
        end.visible=True
        instructions.visible=True
        back.visible=False
        Tutorialtext.visible=False

    game.update(30)

game.over = False
#Loop
while not game.over:
    game.processInput()
    bk.draw()
    smurf.draw()
    sword.draw()
    sword2.draw()
    sword3.draw()
    sword4.draw()
    smurf.stop()#stops animating (displays last frame)

    if end.collidedWith(mouse) and mouse.LeftClick:
        game.quit()
    
    if keys.Pressed[K_RIGHT]:
        smurf.nextFrame() #advances one frame at a time
        smurf.x +=5 #moves to right
        
    if keys.Pressed[K_LEFT]:
        
        smurf.prevFrame() # retreats one frame at a time
        smurf.x -=5 #moves to left

    if smurf.collidedWith(bar) and smurf.y>=game.height-50:
        smurf.y+=0
        
    stars.move(True)
    stars3.move(True)
    stars4.move(True)
    stars5.move(True)
    stars6.move(True)
    stars7.move(True)      
    stars8.move(True)




    if smurf.collidedWith(sword):
        sword.visible=False
        collected+=1

    if smurf.collidedWith(sword2):
        sword2.visible=False
        collected+=1

    if smurf.collidedWith(sword2):
        sword2.visible=False
        collected+=1

    if smurf.collidedWith(sword3):
        sword3.visible=False
        collected+=1

    if smurf.collidedWith(sword4):
        sword4.visible=False
        collected+=1

    if smurf.collidedWith(stars):
        smurf.health-=40
        stars.visible=False

    if smurf.collidedWith(stars3):
        smurf.health-=40
        stars3.visible=False

    if smurf.collidedWith(stars4):
        smurf.health-=40
        stars4.visible=False

    if smurf.collidedWith(stars5):
        smurf.health-=40
        stars5.visible=False

    if smurf.collidedWith(stars6):
        smurf.health-=40
        stars6.visible=False

    if smurf.collidedWith(stars7):
        smurf.health-=40
        stars7.visible=False

    if smurf.collidedWith(stars8):
        smurf.health-=40
        stars8.visible=False

    if smurf.health<=0:
        lose.moveTo(400,300)
        smurf.visible=False
        sword.visible=False
        sword2.visible=False
        sword3.visible=False
        sword4.visible=False
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
      
            

    
    

    if collected>=4:
        Win.moveTo(400,300)
        smurf.visible=False
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

    game.drawText("Health: " + str(smurf.health),smurf.x - 20,smurf.y + 50)
    



    #while jumping:
        #smurf[index].append(Animation("jump.png",2,game,238/2,124,3))
    
    if jumping:
        smurf.y -= 31 * factor 
        factor *= .95
        landed = False
    if factor < .31:
        jumping = False
        factor = 1
    if keys.Pressed[K_SPACE] and smurf.collidedWith(bar) and not jumping:
        jumping = True
    if not smurf.collidedWith(bar,"rectangle"):
        smurf.y += 12
        Jump.play()


    game.update(30)

#game.quit()
