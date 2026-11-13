# 🐠 Interactive 2D Aquarium

An interactive 2D aquarium simulation developed using **Python and OpenGL (PyOpenGL)** as a Computer Graphics Lab project.

The project creates an underwater environment featuring animated fish, rising bubbles, aquatic plants, rocks, and a glass aquarium frame. Users can interact with the aquarium by selecting, moving, resizing, and controlling individual fish.

## 🎥 Project Demo

[![Watch the Project Demo](https://img.youtube.com/vi/uEeVPuV_SCI/0.jpg)](https://www.youtube.com/watch?v=uEeVPuV_SCI)

▶️ **[Watch the demo on YouTube](https://www.youtube.com/watch?v=uEeVPuV_SCI)**

## ✨ Features

- **2D Aquarium Environment:** Blue water background, sandy floor, aquatic plants, rocks, and a glass frame.
- **Animated Fish:** Three colorful fish swim automatically inside the aquarium.
- **Rising Bubbles:** Bubbles continuously move upward and reappear from the bottom.
- **Fish Selection:** Select individual fish using keyboard keys or mouse clicks.
- **Manual Movement:** Move the selected fish using arrow keys or mouse dragging.
- **Fish Resizing:** Increase or decrease the size of the selected fish.
- **Pause and Resume:** Pause or resume the aquarium animation.
- **Reset Function:** Restore the aquarium to its initial state.
- **Glass Effect:** Simple glass borders, reflections, and highlights create the appearance of an aquarium.

## 🛠️ Technologies Used

- **Python 3** – Main programming language.
- **PyOpenGL** – Python bindings for OpenGL.
- **GLUT / FreeGLUT** – Window management, input handling, and animation callbacks.
- **GLU** – 2D orthographic projection.

## 📦 Requirements

- Python 3.x
- PyOpenGL
- PyOpenGL_accelerate (optional)
- GLUT / FreeGLUT

## 🚀 Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/tonmoy-m/Interactive-2D-Aquarium.git
```

### 2. Navigate to the Project Directory

```bash
cd Interactive-2D-Aquarium
```

### 3. Install Required Python Packages

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

**Note:** GLUT / FreeGLUT must also be installed and available on your system. Depending on your operating system, you may need to install it separately.

### 4. Run the Project

```bash
python "Interactive 2D Aquarium.py"
```

## 🎮 Controls

| Key / Input | Action |
|---|---|
| `SPACE` | Pause / Resume animation |
| `1` | Select the first fish |
| `2` | Select the second fish |
| `3` | Select the third fish |
| `↑` | Move selected fish upward |
| `↓` | Move selected fish downward |
| `←` | Move selected fish left |
| `→` | Move selected fish right |
| `+` / `=` | Increase selected fish size |
| `-` | Decrease selected fish size |
| `R` | Reset the aquarium |
| Left Mouse Click | Select a fish |
| Left Mouse Drag | Move the selected fish |

## 🎨 Computer Graphics Concepts

This project demonstrates the practical application of fundamental computer graphics concepts:

### 1. Geometric Primitives

- `GL_QUADS`
- `GL_TRIANGLES`
- `GL_LINES`
- `GL_POINTS`
- `GL_TRIANGLE_FAN`

### 2. 2D Transformations

- Translation using `glTranslatef()`
- Scaling using `glScalef()`
- Matrix operations using `glPushMatrix()` and `glPopMatrix()`

### 3. Projection

- 2D orthographic projection using `gluOrtho2D()`.

### 4. Animation

- Timer-based animation using `glutTimerFunc()`.
- Screen updates using `glutPostRedisplay()`.

### 5. User Interaction

- Keyboard input handling.
- Special-key handling.
- Mouse-click detection.
- Mouse-drag interaction.

## 📁 Project Structure

```text
Interactive-2D-Aquarium/
│
├── Interactive 2D Aquarium.py    # Main aquarium simulation
└── README.md                     # Project documentation
```

## 🖼️ Aquarium Components

The aquarium environment consists of:

- Three colorful animated fish.
- Rising air bubbles.
- Aquatic plants.
- Underwater rocks.
- A sandy aquarium floor.
- An outer aquarium frame with front-glass reflections.

All objects are constructed using basic OpenGL geometric primitives without external image assets or 3D models.

## 🎓 Project Purpose

This project was developed as a **Computer Graphics Lab project** to demonstrate the practical application of fundamental OpenGL concepts, including 2D object construction, transformations, animation, and user interaction.

## 👨‍💻 Repository

**GitHub:** [Interactive 2D Aquarium](https://github.com/tonmoy-m/Interactive-2D-Aquarium)

## 📄 License

This project is available for educational and learning purposes. You are welcome to explore, modify, and improve it.
