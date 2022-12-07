from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import random as rn
import OpenGL.GLUT as glut

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
# posisi spawn meteors
random_X_spawn = []
for i in range(-400, 400, 10):
    random_X_spawn.append(i)

# ukuran meteor
ukuran_meteor = [10, 30, 40]

# kecepatan meteor
speed_meteor = 0.1

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



def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)
    

def gerak_meteor():
    global Y_meteor, meteor, speed_meteor, x_jalan_kiri, x_jalan_kanan, x_batas_kiri_player, x_batas_kanan_player, score
    Y_meteor -= speed_meteor
    
    if Y_meteor < -1300:
        meteor = [random_X_spawn[ rn.randint(0, len(random_X_spawn) - 1 )], ukuran_meteor[rn.randint(0, 2)]]
        Y_meteor = 0

    if meteor[1] == 10:
        if (gerak_x in range(meteor[0] - 30, meteor[0] + 40)) and Y_meteor <= -1160:
            
            time.sleep(3)
            glutLeaveMainLoop()
    elif meteor[1] == 30:
        if (gerak_x in range(meteor[0] - 50, meteor[0] + 60)) and Y_meteor <= -1140:
            time.sleep(3)
            glutLeaveMainLoop()
    elif meteor[1] == 40:
        if (gerak_x in range(meteor[0] - 60, meteor[0] + 70)) and Y_meteor <= -1130:
            time.sleep(3)
            glutLeaveMainLoop()

    score = int(score)
    score += 1
    if (score%100) == 1:
        speed_meteor += 0.0001
        score = str(score)
    else : 
        score = str(score)        

def gerak_meteor1():
    global Y_meteor, meteor, speed_meteor, x_jalan_kiri, x_jalan_kanan, x_batas_kiri_player, x_batas_kanan_player, score
    Y_meteor -= speed_meteor
    
    if Y_meteor < -1300:
        meteor = [random_X_spawn[ rn.randint(0, len(random_X_spawn) - 1 )], ukuran_meteor[rn.randint(0, 2)]]
        X_meteors = 0

    if meteor[1] == 10:
        if (gerak_x in range(meteor[0] - 30, meteor[0] + 40)) <= -1160:
            time.sleep(3)
            glutLeaveMainLoop()
    elif meteor[1] == 30:
        if (gerak_x in range(meteor[0] - 50, meteor[0] + 60)) <= -1150:
            time.sleep(3)
            glutLeaveMainLoop()
    elif meteor[1] == 40:
        if (gerak_x in range(meteor[0] - 60, meteor[0] + 70)) <= -1140:
            time.sleep(3)
            glutLeaveMainLoop()
    score = int(score)
    score += 1
    if (score%100) == 1:
        speed_meteor += 0.001
        score = str(score)
    else : 
        score = str(score)

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

def munculkan_text(x, y, font, text, score, r,  g , b , a):
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

def Score():
    munculkan_text(-455, 450, glut.GLUT_BITMAP_HELVETICA_18, "Score: ", score, 1, 1, 1, 0)
    glutSwapBuffers()

def planet():
    global plnt_x, plnt_y
    # PLANET 1
    glBegin(GL_POLYGON)
    glColor3ub(16, 35, 110)
    glVertex2f(plnt_x - 125, plnt_y + 155)
    glVertex2f(plnt_x - 125, plnt_y + 290)
    glVertex2f(plnt_x - 220, plnt_y + 380)
    glVertex2f(plnt_x - 355, plnt_y + 380)
    glVertex2f(plnt_x - 445, plnt_y + 295)
    glVertex2f(plnt_x - 445, plnt_y + 160)
    glVertex2f(plnt_x - 350, plnt_y + 65)
    glVertex2f(plnt_x - 220, plnt_y + 65)
    glEnd()

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
    glVertex2f(pla_x_1 - 20 + gerak_x, pla_y_1 - 60 + gerak_y)
    glVertex2f(pla_x_1 - 20 + gerak_x, pla_y_1 - 40 + gerak_y)
    glVertex2f(pla_x_1 + 12 + gerak_x, pla_y_1 - 20 + gerak_y)
    glVertex2f(pla_x_1 + 7 + gerak_x, pla_y_1 - 40 + gerak_y)
    glEnd()

    # RIGHT WING
    glBegin(GL_QUADS)
    glColor3ub(150, 0, 0)
    glVertex2f(pla_x_1 + 68 + gerak_x, pla_y_1 - 20 + gerak_y)
    glVertex2f(pla_x_1 + 100 + gerak_x, pla_y_1 - 40 + gerak_y)
    glVertex2f(pla_x_1 + 100 + gerak_x, pla_y_1 - 60 + gerak_y)
    glVertex2f(pla_x_1 + 72 + gerak_x, pla_y_1 - 40 + gerak_y)
    glEnd()

    # WINDOW
    glBegin(GL_QUADS)
    glColor3ub(0, 30, 180)
    glVertex2f(pla_x_1 + 28 + gerak_x, pla_y_1 + 31 + gerak_y)
    glVertex2f(pla_x_1 + 52 + gerak_x, pla_y_1 + 31 + gerak_y)
    glVertex2f(pla_x_1 + 52 + gerak_x, pla_y_1 + 8 + gerak_y)
    glVertex2f(pla_x_1 + 28 + gerak_x, pla_y_1 + 8 + gerak_y)
    glEnd()

def input_keyboard(key, x, y):
    global gerak_x, gerak_y, x_batas_kiri_player, x_batas_kanan_player

    # Untuk mengubah posisi player
    if key == GLUT_KEY_RIGHT:
        gerak_x += 20
    if key == GLUT_KEY_LEFT:
        gerak_x -= 20

    if gerak_x == x_batas_kiri_player or gerak_x == x_batas_kanan_player:
        glutLeaveMainLoop()

def menu():
    glClear(GL_COLOR_BUFFER_BIT)
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
    Score()
    glPopMatrix()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Rocket")
    glutDisplayFunc(menu)
    glutIdleFunc(menu)
    glutSpecialFunc(input_keyboard)
    init()
    glutMainLoop()

main()