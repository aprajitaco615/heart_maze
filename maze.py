import tkinter as tk 
import random


Row = 43
Col = 45
cell = 15

def in_heart(r, c):
    x = (c- Col/2)/(Col/2.38)
    y = -(r-47/2)/(47/2.45)
    return  ((x**2) + (y**2) - 1)**3 - (x**2)*(y**3) <= 0.0
 
    
def carve(row, col):
    global maze
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    random.shuffle(directions)
    
    for offr, offc in directions:
        nr , nc = row+offr, col +offc
        if 0 <= nr < Row and 0 <= nc < Col and maze[nr][nc] == '#' and in_heart(nr, nc):
                
                maze[row+ offr//2][col+offc//2] = ' '
            
                maze[nr][nc] = ' '
                carve(nr, nc)
    
def win_mes():
    canvas.config(bg='#dea0de')
    canvas.create_text(Col*cell//2, Row*cell//2,
                       text='Victory!!!!!!\n\nHere have my heart as the prize: 🫀',
                       font=('Helvetica', 25), justify='center')

    

def win_animation(radius=0):
    canvas.delete('all')
    for r in range(Row):
        for c in range(Col):
            if in_heart(r, c):
                x, y = c*cell, r*cell
                canvas.create_rectangle(x, y, x+cell, y+cell, fill='#dea0de', outline='')
            else:
                x, y = c*cell, r*cell
                canvas.create_rectangle(x, y, x+cell, y+cell, fill='#0d0b30', outline='')
            
                
                
    root.after(1000, win_mes)

        
    
    
#generation of maze    
maze=[]
for i in range(Row):
    maze.append(['#']*Col)
    
    #start 
st_r , st_c = Row//2 - 12, Col//2 
if st_r%2==0 : st_r+=1
if st_c%2==0 : st_c+=1

maze[st_r][st_c]=' '
carve(st_r, st_c) 
    

#exit
e_r, e_c = Row-2, Col//2 
if e_r%2==0 : e_r+=1
if e_c%2==0 : e_c+=1

maze[e_r][e_c] = 'e'


def draw(maze, canvas):
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            x , y = c*cell , r*cell
            
            if not in_heart(r, c):
                canvas.create_rectangle(x, y, x+cell, y+cell, fill = '#0d0b30', outline='')
            elif maze[r][c] == '#':
                canvas.create_rectangle(x, y, x+cell, y+cell, fill = '#dea0de', outline='')
            elif maze[r][c] =='e':
                canvas.create_text(x + cell//2, y + cell//2, text='☾', font = ('Segoe UI Symbol', 18, 'bold'))
            else:
                canvas.create_rectangle(x, y, x+cell, y+cell, fill = 'black', outline ='')
            
 
    
 
    
 
root = tk.Tk()
canvas = tk.Canvas(root, width = Col*cell, height = Row*cell, bg='black') #width = cols*cellsize, height = rows*cellsize           
canvas.pack() 

draw(maze, canvas)

p_pos=[st_r, st_c]
p = canvas.create_text(st_c*cell + cell//2, st_r*cell + cell//2, text='☀', fill= '#e0e03a', font = ('Arial', 18, 'bold'))
            
def key_move(e) :
    global p_pos
    global p 
    
    offset_row=offset_col=0
    
    if e.keysym=='Up':
        offset_row=-1
    elif e.keysym=='Down':
        offset_row=+1
    elif e.keysym=='Left':
        offset_col=-1
    elif e.keysym=='Right':
        offset_col=+1
       
    new_col=p_pos[1]+offset_col
    new_row=p_pos[0]+offset_row
    
    if maze[new_row][new_col] != '#':
        p_pos = [new_row, new_col]
        canvas.coords(p, new_col*cell + cell//2, new_row*cell + cell//2)
        
        if maze[new_row][new_col] == 'e': ##WIN
            root.after(500, win_animation)
            
            
    
root.bind('<Up>', key_move)
root.bind('<Down>', key_move)
root.bind('<Left>', key_move)
root.bind('<Right>', key_move)
        

root.focus_force()
root.mainloop()
