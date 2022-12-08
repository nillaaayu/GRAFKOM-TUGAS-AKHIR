from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import random as rn
import OpenGL.GLUT as glut
import math

w,h= 500,500

# ketinggian meteor
Y_meteor = 0

# planet
plnt_x = 0
plnt_y = 0

# player
gerak_x = 0
gerak_y = -400
pla_x_1 = -30
pla_x_2 = 30
pla_y_1 = -30
pla_y_2 = 30

# score
score = 0

# level
lvl = 0 

# posisi spawn meteors
random_X_spawn = []
for i in range(-350, 350, 10):
    random_X_spawn.append(i)

# ukuran meteor
ukuran_meteor = [10, 30, 40]

# kecepatan meteor
speed_meteor = 0.3
speed_meteor1 = 0.3

# spawn random meteor
meteor = [random_X_spawn[rn.randint(0, len(random_X_spawn) - 1 )], ukuran_meteor[rn.randint(0, 2)]]

# x jalan kiri
x_jalan_kiri = -400

# x jalan kanan
x_jalan_kanan = 400

# batas player kiri
x_batas_kiri_player = -400

# batas player kanan
x_batas_kanan_player = 400

# nabrak meteor
tabrak = False # krn blm nabrak meteornya

# mulai
play = False



def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)
    

def gerak_meteor():
    global Y_meteor, meteor, speed_meteor, x_jalan_kiri, x_jalan_kanan, x_batas_kiri_player, x_batas_kanan_player, score, lvl, tabrak
    Y_meteor -= speed_meteor
    
    if Y_meteor < -1300:
        meteor = [random_X_spawn[ rn.randint(0, len(random_X_spawn) - 1 )], ukuran_meteor[rn.randint(0, 2)]]
        Y_meteor = 0

    if meteor[1] == 10:
        if (gerak_x in range(meteor[0] - 30, meteor[0] + 40)) and Y_meteor <= -1160:
            time.sleep(1)
            tabrak = True
    elif meteor[1] == 30:
        if (gerak_x in range(meteor[0] - 50, meteor[0] + 60)) and Y_meteor <= -1140:
            time.sleep(1)
            tabrak = True
    elif meteor[1] == 40:
        if (gerak_x in range(meteor[0] - 60, meteor[0] + 70)) and Y_meteor <= -1130:
            time.sleep(1)
            tabrak = True


def gerak_meteor1():
    global Y_meteor, meteor, speed_meteor, x_jalan_kiri, x_jalan_kanan, x_batas_kiri_player, x_batas_kanan_player, score, lvl, tabrak
    Y_meteor -= speed_meteor
    
    if Y_meteor < -1300:
        meteor = [random_X_spawn[ rn.randint(0, len(random_X_spawn) - 1 )], ukuran_meteor[rn.randint(0, 2)]]
        Y_meteor = 0

    if meteor[1] == 10:
        if (gerak_x in range(meteor[0] - 30, meteor[0] + 40)) <= -1160:
            time.sleep(1)
            tabrak = True
    elif meteor[1] == 30:
        if (gerak_x in range(meteor[0] - 50, meteor[0] + 60)) <= -1150:
            time.sleep(1)
            tabrak = True
    elif meteor[1] == 40:
        if (gerak_x in range(meteor[0] - 60, meteor[0] + 70)) <= -1140:
            time.sleep(1)
            tabrak = True

def meteorsPoints(x, y, s):
    glTranslate(0, Y_meteor, 0)
    glPointSize(s)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    glVertex2f(x, y)
    glEnd()

def meteorsPoints1(x, y, s):
    glTranslate(0, Y_meteor, 0)
    glPointSize(s)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    glVertex2f(x, y)
    glEnd()

def jalan():
    global x_jalan_kiri, x_jalan_kanan

    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    # kiri
    glVertex2f(x_jalan_kiri, -500)
    glVertex2f(x_jalan_kiri, 500)
    # kanan
    glVertex2f(x_jalan_kanan, 500)
    glVertex2f(x_jalan_kanan, -500)
    glEnd()

def munculkan_text_score(x, y, font, text, score, r,  g , b , a):
    blending = False 

    if glIsEnabled(GL_BLEND) :
        blending = True

    glRasterPos2f(x,y)

    for i in text :
        glutBitmapCharacter(font, ctypes.c_int(ord(i)))
    for i in score :
        glutBitmapCharacter(font, ctypes.c_int(ord(i)))

    if not blending :
        glDisable(GL_BLEND) 

def munculkan_text_lvl(x, y, font, text, lvl, r,  g , b , a):
    blending = False 

    if glIsEnabled(GL_BLEND) :
        blending = True

    glRasterPos2f(x,y)

    for i in text :
        glutBitmapCharacter(font, ctypes.c_int(ord(i)))
    for i in lvl :
        glutBitmapCharacter(font, ctypes.c_int(ord(i)))

    if not blending :
        glDisable(GL_BLEND) 

def Score():
    munculkan_text_score(-380, 450, glut.GLUT_BITMAP_HELVETICA_12, "Score: ", str(score), 1, 1, 1, 0)
    glutSwapBuffers()

def Level():
    munculkan_text_lvl(-380, 400, glut.GLUT_BITMAP_HELVETICA_12, "Level: ", str(lvl), 1, 1, 1, 0)
    glutSwapBuffers()

def scoring():
    global score, lvl, tabrak, speed_meteor, speed_meteor1
    if tabrak == False:
        score += 1
        if (score%10000) == 1:
            lvl += 1
            speed_meteor += 0.05
            speed_meteor1 += 0.05

def circle(r,xR,yR):
    glPushMatrix()
    glBegin(GL_POLYGON)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + xR, y + yR)
    glEnd();
    glPopMatrix()

def planet():
    # planet 1
    glColor3ub(190,130,20)
    circle(100,200,500)

    # planet 2
    glColor3ub(0,105,205)
    circle(180,-200,300)

    # planet 3
    glColor3ub(205,0,0)
    circle(260,-600,-100)

    # planet 4
    glColor3ub(255,255,0)
    circle(400,700,-100)

def player():
    global gerak_x, gerak_y
    global pla_x_1, pla_x_2, pla_y_1, pla_y_2

    # BODY
    glBegin(GL_POLYGON)
    glColor3ub(225,225, 225)
    glVertex2f(pla_x_1 + 40 + gerak_x, pla_y_1 + 80 +gerak_y)
    glVertex2f(pla_x_1 + 20 + gerak_x, pla_y_1 + 40 + gerak_y)
    glVertex2f(pla_x_1 + 7 + gerak_x, pla_y_1 - 40 + gerak_y )
    glVertex2f(pla_x_1 + 72 + gerak_x, pla_y_1 - 40 +gerak_y)
    glVertex2f(pla_x_1 + 60 + gerak_x, pla_y_1 + 40 + gerak_y)
    glEnd()

    # LEFT WING
    glBegin(GL_QUADS)
    glColor3ub(150, 0, 0)
    glVertex2f(pla_x_1 - 7 + gerak_x, pla_y_1 - 66 + gerak_y)
    glVertex2f(pla_x_1 - 7 + gerak_x, pla_y_1 - 47 + gerak_y)
    glVertex2f(pla_x_1 + 12 + gerak_x, pla_y_1 + 10 + gerak_y)
    glVertex2f(pla_x_1 + 5 + gerak_x, pla_y_1 - 40 + gerak_y)
    glEnd()

    # RIGHT WING
    glBegin(GL_QUADS)
    glColor3ub(150, 0, 0)
    glVertex2f(pla_x_1 + 68 + gerak_x, pla_y_1 + 10 + gerak_y)
    glVertex2f(pla_x_1 + 87 + gerak_x, pla_y_1 - 47 + gerak_y)
    glVertex2f(pla_x_1 + 87 + gerak_x, pla_y_1 - 65 + gerak_y)
    glVertex2f(pla_x_1 + 75 + gerak_x, pla_y_1 - 40 + gerak_y)
    glEnd()

    # WINDOW
    glBegin(GL_QUADS)
    glColor3ub(0, 30, 180)
    glVertex2f(pla_x_1 + 28 + gerak_x, pla_y_1 + 31 + gerak_y)
    glVertex2f(pla_x_1 + 52 + gerak_x, pla_y_1 + 31 + gerak_y)
    glVertex2f(pla_x_1 + 52 + gerak_x, pla_y_1 + 8 + gerak_y)
    glVertex2f(pla_x_1 + 28 + gerak_x, pla_y_1 + 8 + gerak_y)
    glEnd()

    # NOS1
    glBegin(GL_QUADS)
    glColor3ub(75, 75, 75)
    glVertex2f(pla_x_1 + 12 + gerak_x, pla_y_1 - 40 + gerak_y)
    glVertex2f(pla_x_1 + 68 + gerak_x, pla_y_1 - 40 + gerak_y)
    glVertex2f(pla_x_1 + 68 + gerak_x, pla_y_1 - 56 + gerak_y)
    glVertex2f(pla_x_1 + 12 + gerak_x, pla_y_1 - 56 + gerak_y)
    glEnd()

    # NOS2
    glBegin(GL_QUADS)
    glColor3ub(255, 85, 0)
    glVertex2f(pla_x_1 + 48 + gerak_x, pla_y_1 - 68 + gerak_y)
    glVertex2f(pla_x_1 + 32 + gerak_x, pla_y_1 - 68 + gerak_y)
    glVertex2f(pla_x_1 + 32 + gerak_x, pla_y_1 - 56 + gerak_y)
    glVertex2f(pla_x_1 + 48 + gerak_x, pla_y_1 - 56 + gerak_y)
    glEnd()


def input_keyboard(key, x, y):
    global gerak_x, gerak_y, x_batas_kiri_player, x_batas_kanan_player, play, tabrak

    # Untuk mengubah posisi player
    if key == GLUT_KEY_RIGHT:
        gerak_x += 20
    if key == GLUT_KEY_LEFT:
        gerak_x -= 20
    if key == GLUT_KEY_F1:
            play = 1

    if gerak_x - 22 < x_batas_kiri_player or gerak_x + 50 > x_batas_kanan_player:
        time.sleep(1)
        tabrak = True

def text_menu(x, y, font, text, r,  g , b , a):
    blending = False 

    if glIsEnabled(GL_BLEND) :
        blending = True

    glRasterPos2f(x,y)

    for i in text :
        glutBitmapCharacter(font, ctypes.c_int(ord(i)))

    if not blending :
        glDisable(GL_BLEND)

def menu():
    global play
    glClear(GL_COLOR_BUFFER_BIT)
    if play == True:
        if tabrak == False:
            glPushMatrix()
            player()
            glPopMatrix()
            glPushMatrix()
            planet()
            glPopMatrix()
            glPushMatrix()
            jalan()
            glPopMatrix()
            glPushMatrix()
            meteorsPoints(meteor[0], 800, meteor[1])
            glPopMatrix()
            glPushMatrix()
            gerak_meteor()
            glPopMatrix()
            glPushMatrix()
            meteorsPoints1(meteor[0], 800, meteor[1])
            glPopMatrix()
            glPushMatrix()
            gerak_meteor1()
            glPopMatrix()
            glPushMatrix()
            scoring()
            glPopMatrix()
            glPushMatrix()
            Score()
            glPopMatrix()
            glPushMatrix()
            Level()
            glPopMatrix()
        else:
            text_menu(-100,0, glut.GLUT_BITMAP_HELVETICA_18, "GAME OVER", 1, 1, 1, 0)
    else:
        text_menu(-130,100, glut.GLUT_BITMAP_TIMES_ROMAN_24, "Rocket Keeper", 1, 1, 1, 0)
        text_menu(-100,0, glut.GLUT_BITMAP_HELVETICA_18, "PLAY GAME", 1, 1, 1, 0)
        text_menu(-50,-50, glut.GLUT_BITMAP_HELVETICA_12, "PRESS F1", 1, 1, 1, 0)
        # kalo tombol play diklik, masuk ke game
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Rocket Keeper") 
    init()
    glutSpecialFunc(input_keyboard)
    glutDisplayFunc(menu)
    glutIdleFunc(menu)
    glutMainLoop()

main()