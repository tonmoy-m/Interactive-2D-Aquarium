from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

# --------------------------------------------------
# Aquarium settings
# --------------------------------------------------

WIDTH = 900
HEIGHT = 600

paused = False
selectedFish = 0
dragging = False

# Each fish has: x, y, speed, direction, size, color
fishes = [
    {"x": 180, "y": 390, "speed": 1.8, "direction": 1,
     "size": 1.0, "color": (1.0, 0.75, 0.05)},
    {"x": 470, "y": 285, "speed": 1.3, "direction": -1,
     "size": 1.15, "color": (1.0, 0.15, 0.12)},
    {"x": 700, "y": 430, "speed": 1.6, "direction": 1,
     "size": 0.85, "color": (0.65, 0.15, 0.9)}
]

# Each bubble has: x, y, radius, speed
bubbles = [
    [100, 120, 5, 1.2],
    [145, 220, 8, 1.6],
    [260, 100, 6, 1.0],
    [350, 180, 5, 1.4],
    [540, 90, 7, 1.3],
    [620, 200, 5, 1.7],
    [760, 130, 8, 1.1],
    [820, 260, 5, 1.5]
]


# --------------------------------------------------
# Basic drawing functions
# --------------------------------------------------

def drawCircle(x, y, radius):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)

    for angle in range(361):
        a = math.radians(angle)
        px = x + radius * math.cos(a)
        py = y + radius * math.sin(a)
        glVertex2f(px, py)

    glEnd()


def drawAquariumFrame():
    # Outer aquarium frame (drawn with simple quads)
    glColor3f(0.03, 0.20, 0.32)
    glBegin(GL_QUADS)

    # Left frame
    glVertex2f(0, 0)
    glVertex2f(18, 0)
    glVertex2f(18, HEIGHT)
    glVertex2f(0, HEIGHT)

    # Right frame
    glVertex2f(WIDTH - 18, 0)
    glVertex2f(WIDTH, 0)
    glVertex2f(WIDTH, HEIGHT)
    glVertex2f(WIDTH - 18, HEIGHT)

    # Top frame
    glVertex2f(0, HEIGHT - 18)
    glVertex2f(WIDTH, HEIGHT - 18)
    glVertex2f(WIDTH, HEIGHT)
    glVertex2f(0, HEIGHT)

    # Bottom frame
    glVertex2f(0, 0)
    glVertex2f(WIDTH, 0)
    glVertex2f(WIDTH, 18)
    glVertex2f(0, 18)
    glEnd()

    # Inner glass highlights
    glColor3f(0.35, 0.85, 0.95)
    glBegin(GL_QUADS)

    # Left glass highlight
    glVertex2f(18, 20)
    glVertex2f(22, 20)
    glVertex2f(22, HEIGHT - 20)
    glVertex2f(18, HEIGHT - 20)

    # Right glass highlight
    glVertex2f(WIDTH - 22, 20)
    glVertex2f(WIDTH - 18, 20)
    glVertex2f(WIDTH - 18, HEIGHT - 20)
    glVertex2f(WIDTH - 22, HEIGHT - 20)

    # Top glass highlight
    glVertex2f(20, HEIGHT - 22)
    glVertex2f(WIDTH - 20, HEIGHT - 22)
    glVertex2f(WIDTH - 20, HEIGHT - 18)
    glVertex2f(20, HEIGHT - 18)
    glEnd()


def drawBackground():
    # Water background
    glColor3f(0.05, 0.55, 0.82)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(WIDTH, 0)
    glVertex2f(WIDTH, HEIGHT)
    glVertex2f(0, HEIGHT)
    glEnd()

    # Sandy floor
    glColor3f(0.95, 0.78, 0.42)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(WIDTH, 0)
    glVertex2f(WIDTH, 65)
    glVertex2f(0, 65)
    glEnd()

    # Small sand marks
    glPointSize(3)
    glColor3f(0.75, 0.55, 0.30)
    glBegin(GL_POINTS)
    for x in range(25, WIDTH, 55):
        glVertex2f(x, 18 + (x % 4) * 5)
    glEnd()

def drawFrontGlass():

    # Front glass border
    glColor3f(0.55, 0.90, 1.0)

    glBegin(GL_LINES)

    # Left side
    glVertex2f(25, 28)
    glVertex2f(25, HEIGHT - 25)

    # Right side
    glVertex2f(WIDTH - 25, 28)
    glVertex2f(WIDTH - 25, HEIGHT - 25)

    # Top
    glVertex2f(25, HEIGHT - 25)
    glVertex2f(WIDTH - 25, HEIGHT - 25)

    # Bottom
    glVertex2f(25, 28)
    glVertex2f(WIDTH - 25, 28)

    glEnd()


    # Glass reflections
    glColor3f(0.45, 0.82, 0.94)

    glBegin(GL_QUADS)

    # Left reflection
    glVertex2f(35, 100)
    glVertex2f(42, 100)
    glVertex2f(42, 475)
    glVertex2f(35, 475)

    # Right reflection
    glVertex2f(WIDTH - 43, 155)
    glVertex2f(WIDTH - 36, 155)
    glVertex2f(WIDTH - 36, 500)
    glVertex2f(WIDTH - 43, 500)

    # Top reflection
    glVertex2f(100, HEIGHT - 37)
    glVertex2f(330, HEIGHT - 37)
    glVertex2f(330, HEIGHT - 42)
    glVertex2f(100, HEIGHT - 42)

    glEnd()


    # Small glass glare marks
    glColor3f(0.75, 0.94, 1.0)

    glBegin(GL_LINES)

    glVertex2f(55, 490)
    glVertex2f(95, 530)

    glVertex2f(WIDTH - 105, 455)
    glVertex2f(WIDTH - 65, 495)

    glEnd()

def drawPlant(x, y, height, color):
    # Plant stems
    glColor3f(0.05, 0.45, 0.12)
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x - 8, y + height * 0.55)

    glVertex2f(x, y)
    glVertex2f(x + 12, y + height)

    glVertex2f(x, y)
    glVertex2f(x + 30, y + height * 0.65)
    glEnd()

    # Leaves made from triangles
    glColor3f(*color)
    glBegin(GL_TRIANGLES)

    # Left leaf
    glVertex2f(x - 8, y + height * 0.55)
    glVertex2f(x - 38, y + height * 0.85)
    glVertex2f(x - 12, y + height * 0.30)

    # Middle leaf
    glVertex2f(x + 12, y + height)
    glVertex2f(x + 38, y + height * 0.72)
    glVertex2f(x + 8, y + height * 0.45)

    # Right leaf
    glVertex2f(x + 30, y + height * 0.65)
    glVertex2f(x + 55, y + height * 0.90)
    glVertex2f(x + 20, y + height * 0.35)

    glEnd()


def drawRock(x, y, size):
    # Rock made from simple triangles
    glBegin(GL_TRIANGLES)

    glColor3f(0.42, 0.47, 0.50)
    glVertex2f(x, y)
    glVertex2f(x + size * 0.35, y + size * 0.65)
    glVertex2f(x + size * 0.70, y)

    glColor3f(0.55, 0.60, 0.62)
    glVertex2f(x + size * 0.35, y + size * 0.65)
    glVertex2f(x + size * 0.75, y + size * 0.75)
    glVertex2f(x + size, y)

    glColor3f(0.32, 0.38, 0.42)
    glVertex2f(x + size * 0.35, y + size * 0.65)
    glVertex2f(x + size, y)
    glVertex2f(x + size * 0.70, y)

    glEnd()


def drawOneFish(fish, index):
    glPushMatrix()

    # Move fish to its current position.
    glTranslatef(fish["x"], fish["y"], 0)

    # Flip the fish horizontally when it swims left.
    glScalef(fish["size"] * fish["direction"], fish["size"], 1)

    # Highlight the selected fish with a simple outline.
    if index == selectedFish:
        glColor3f(1, 1, 1)
        glBegin(GL_LINES)
        glVertex2f(-48, -27)
        glVertex2f(48, -27)

        glVertex2f(48, -27)
        glVertex2f(48, 27)

        glVertex2f(48, 27)
        glVertex2f(-48, 27)

        glVertex2f(-48, 27)
        glVertex2f(-48, -27)
        glEnd()

    # Fish tail
    glColor3f(*fish["color"])
    glBegin(GL_TRIANGLES)
    glVertex2f(-32, 0)
    glVertex2f(-58, 22)
    glVertex2f(-58, -22)
    glEnd()

    # Fish body
    glBegin(GL_QUADS)
    glVertex2f(-35, -18)
    glVertex2f(30, -18)
    glVertex2f(30, 18)
    glVertex2f(-35, 18)
    glEnd()

    # Top fin
    glColor3f(
        min(fish["color"][0] + 0.12, 1),
        min(fish["color"][1] + 0.12, 1),
        min(fish["color"][2] + 0.12, 1)
    )
    glBegin(GL_TRIANGLES)
    glVertex2f(-5, 18)
    glVertex2f(12, 38)
    glVertex2f(22, 18)
    glEnd()

    # Bottom fin
    glBegin(GL_TRIANGLES)
    glVertex2f(-5, -18)
    glVertex2f(12, -35)
    glVertex2f(22, -18)
    glEnd()

    # Eye: white circle and black circle
    glColor3f(1, 1, 1)
    drawCircle(20, 7, 6)
    glColor3f(0, 0, 0)
    drawCircle(22, 7, 2.5)


    glPopMatrix()


def drawAllFish():
    for i in range(len(fishes)):
        drawOneFish(fishes[i], i)


def drawAllBubbles():
    for bubble in bubbles:
        # Slightly transparent-looking pale blue/white circles.
        glColor3f(0.78, 0.94, 1.0)
        drawCircle(bubble[0], bubble[1], bubble[2])

        # Small highlight made with a point.
        glPointSize(2)
        glColor3f(1, 1, 1)
        glBegin(GL_POINTS)
        glVertex2f(bubble[0] - bubble[2] * 0.3,
                   bubble[1] + bubble[2] * 0.3)
        glEnd()


# --------------------------------------------------
# Scene drawing
# --------------------------------------------------

def main():
    drawBackground()

    # Plants behind fish
    drawPlant(80, 65, 150, (0.05, 0.65, 0.20))
    drawPlant(250, 65, 105, (0.10, 0.72, 0.25))
    drawPlant(640, 65, 145, (0.04, 0.60, 0.18))
    drawPlant(790, 65, 125, (0.08, 0.70, 0.22))

    # Rocks
    drawRock(95, 65, 115)
    drawRock(680, 65, 130)

    # Bubbles and fish
    drawAllBubbles()
    drawAllFish()

    # Aquarium glass/frame
    drawAquariumFrame()

    # Front glass
    drawFrontGlass()


def showScreen():
    glClearColor(0.05, 0.55, 0.82, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, 0, HEIGHT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    main()

    glutSwapBuffers()


# --------------------------------------------------
# Animation
# --------------------------------------------------

def update(value):
    if not paused and not dragging:
        # Move fish automatically.
        for fish in fishes:
            fish["x"] += fish["speed"] * fish["direction"]

            # Change direction at the aquarium boundaries.
            if fish["x"] > WIDTH - 75:
                fish["direction"] = -1

            elif fish["x"] < 75:
                fish["direction"] = 1

        # Move bubbles upward.
        for bubble in bubbles:
            bubble[1] += bubble[3]

            if bubble[1] > HEIGHT + bubble[2]:
                bubble[1] = 65
                bubble[0] = 40 + (bubble[0] + 137) % (WIDTH - 80)

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)


# --------------------------------------------------
# Keyboard controls
# --------------------------------------------------

def normalKey(key, x, y):
    global paused, selectedFish

    if key == b' ':
        paused = not paused

    elif key == b'r' or key == b'R':
        resetAquarium()

    elif key == b'1':
        selectedFish = 0

    elif key == b'2':
        selectedFish = 1

    elif key == b'3':
        selectedFish = 2

    elif key == b'+' or key == b'=':
        fishes[selectedFish]["size"] += 0.1

    elif key == b'-':
        fishes[selectedFish]["size"] -= 0.1

        if fishes[selectedFish]["size"] < 0.5:
            fishes[selectedFish]["size"] = 0.5

    glutPostRedisplay()


def specialKey(key, x, y):
    fish = fishes[selectedFish]

    if key == GLUT_KEY_LEFT:
        fish["x"] -= 10

    elif key == GLUT_KEY_RIGHT:
        fish["x"] += 10

    elif key == GLUT_KEY_UP:
        fish["y"] += 10

    elif key == GLUT_KEY_DOWN:
        fish["y"] -= 10

    # Keep fish inside the aquarium.
    fish["x"] = max(65, min(WIDTH - 65, fish["x"]))
    fish["y"] = max(100, min(HEIGHT - 45, fish["y"]))

    glutPostRedisplay()


# --------------------------------------------------
# Mouse controls
# --------------------------------------------------

def mouseClick(button, state, x, y):
    global selectedFish, dragging

    mouseX = x
    mouseY = HEIGHT - y

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            dragging = False

            # Check which fish was clicked.
            for i in range(len(fishes)):
                fish = fishes[i]
                halfWidth = 55 * fish["size"]
                halfHeight = 40 * fish["size"]

                if (abs(mouseX - fish["x"]) <= halfWidth and
                        abs(mouseY - fish["y"]) <= halfHeight):
                    selectedFish = i
                    dragging = True
                    break

        elif state == GLUT_UP:
            dragging = False

    glutPostRedisplay()


def mouseDrag(x, y):
    if dragging:
        fish = fishes[selectedFish]

        fish["x"] = max(65, min(WIDTH - 65, x))
        fish["y"] = max(100, min(HEIGHT - 45, HEIGHT - y))

        glutPostRedisplay()


# --------------------------------------------------
# Reset
# --------------------------------------------------

def resetAquarium():
    global fishes, paused, selectedFish, dragging

    fishes = [
        {"x": 180, "y": 390, "speed": 1.8, "direction": 1,
         "size": 1.0, "color": (1.0, 0.75, 0.05)},
        {"x": 470, "y": 285, "speed": 1.3, "direction": -1,
         "size": 1.15, "color": (1.0, 0.15, 0.12)},
        {"x": 700, "y": 430, "speed": 1.6, "direction": 1,
         "size": 0.85, "color": (0.65, 0.15, 0.9)}
    ]

    paused = False
    selectedFish = 0
    dragging = False
    glutPostRedisplay()


# --------------------------------------------------
# OpenGL initialization
# --------------------------------------------------

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(100, 50)
glutCreateWindow(b"Underwater World - Glass Aquarium")

glutDisplayFunc(showScreen)
glutKeyboardFunc(normalKey)
glutSpecialFunc(specialKey)
glutMouseFunc(mouseClick)
glutMotionFunc(mouseDrag)

glutTimerFunc(16, update, 0)

glutMainLoop()
