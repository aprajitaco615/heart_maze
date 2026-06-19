A GUI-based maze generation game developed in Python using the tkinter library. 
The application uses a mathematical heart equation combined with a randomized depth-first search (DFS) algorithm to carve out a unique playable maze mask every time the application run. 

//Core Features
Mathematical Masking: Uses an algebraic heart curve equation to constrain a grid, dynamically rendering the maze boundaries within a perfectly proportioned heart shape.
Procedural Generation (DFS): Employs a recursive backtracking maze-carving algorithm, ensuring that every time the game opens, a brand-new, solvable maze is generated.
Custom Vector Elements: Features procedural rendering of interactive game elements, tracking a custom vector sun token as the player's avatar navigating toward a crescent moon (☾) exit.
Dynamic Win State UI: Includes a custom color-inverting vector animation routine triggered immediately upon successfully reaching the exit path.


Prerequisites:
-Python 3.x
-Tkinter package (Included by default with standard Python installations)

Execution
-Clone the repository and execute the main python file:
Bash
git clone https://github.com/YOUR_USERNAME/heart-maze.git
cd heart-maze
python main.py

Controls
-Movement: Use the Arrow Keys (Up, Down, Left, Right) to navigate the sun token out of the heart's depths.
-Objective: Reach the crescent moon icon (☾) located at the base of the heart structure to trigger the victory routine.
