import cv2
import numpy as np
img = cv2.imread("maze01.jpg",cv2.IMREAD_GRAYSCALE)
_,img = cv2.threshold(img,220,255,cv2.THRESH_BINARY)

cell_size = 20

total_cell = int(img.shape[0]/(cell_size))

src = (0,0)
dest = (total_cell-1,total_cell-1)


#========================== functions =============================#

def upward(x,y,d_up):
    l = d_up[(x, y)]
    a = l[0][0]
    b = l[0][1]
    c = l[1][0]
    d = l[1][1]
    e =img[a:b,c:d][1][total_cell]
    if e == 0:
        return False
    else:
        return True        
        
def downward(x,y,d_down):
    l = d_down[(x, y)]
    a = l[0][0]
    b = l[0][1]
    c = l[1][0]
    d = l[1][1]
    e =img[a:b,c:d][1][total_cell]
    if e == 0:
        return False
    else:
        return True


def leftward(x,y,d_left):
    l = d_left[(x, y)]
    a = l[0][0]
    b = l[0][1]
    c = l[1][0]
    d = l[1][1]
    e =img[a:b,c:d][total_cell][1]
    if e == 0:
        return False
    else:
        return True
        
        
def rightward(x,y,d_right):    
    l = d_right[(x, y)]
    a = l[0][0]
    b = l[0][1]
    c = l[1][0]
    d = l[1][1]
    e =img[a:b,c:d][total_cell][1]
    if e == 0:
        return False
    else:
        return True
        
        
# BFS Algorith for shortest path
            
            
def BFS(adj_list,src,dest):
    q = []
    visited = [[0 for i in range(total_cell)] for j in range(total_cell)]
    global parent 
    parent = [[-1 for i in range(total_cell)] for j in range(total_cell)]
    q.append(src)
    visited[src[0]][src[1]] = True
    
    while len(q)!=0:
        node = q.pop(0)
        for neighbour in adj_list[node]:
            if visited[neighbour[0]][neighbour[1]] == False:
                q.append(neighbour)
                visited[neighbour[0]][neighbour[1]] = True
                parent[neighbour[0]][neighbour[1]] = node
    global arr 
    arr = []
    temp = dest
    while temp!=src:
        #print(temp,"<----",end=' ')
        temp = parent[temp[0]][temp[1]]
        arr.append(temp)  
    
    arr.reverse()
    arr.append(dest)
    
    print("The Following are the co-ordinates of the Maze")
    
    for i in arr:
        print(i,end="")
        
def SHOW():
    for i in arr:
        x = i[0]
        y = i[1]
        img[x*20:(x+1)*20,y*20:(y+1)*20] = 0

    cv2.imshow("Maze" , img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
#=================================================================#        

d_up = dict()
d_down = dict()
d_left = dict()
d_right = dict()

##right obstacle
for i in range(total_cell):
    for j in range(total_cell):
        d_right[(i,j)] = [(i*cell_size,(i+1)*cell_size),(j*cell_size+18,(j+1)*cell_size)]
##down obstacle    
for i in range(total_cell):
    for j in range(total_cell):
        d_down[(i,j)] = [(i*cell_size+18,(i+1)*cell_size),((j*cell_size),(j+1)*cell_size)]

##left obstacle
for i in range(total_cell):
    for j in range(total_cell):
        d_left[(i,j)] = [(i*cell_size,(i+1)*cell_size),(j*cell_size,(j+1)*cell_size - 18)]
        
#up obstacle
for i in range(total_cell):
    for j in range(total_cell):
        d_up[(i,j)] = [(i*cell_size,(i+1)*cell_size -1),(j*cell_size,(j+1)*cell_size)]
        
        
#Creates adjacency list to find shortest path        
        
adj_list = dict()
for i in range(total_cell): 
    for j in range(total_cell):
        adj_list[(i,j)] = []

r = [-1,1,0,0]
c = [0,0,-1,1]

for i in range(total_cell):
    for j in range(total_cell):
        if upward(i,j,d_up)==True:
            adj_list[(i,j)].append((i+r[0],j+c[0]))
        if downward(i,j,d_down)==True:
            adj_list[(i,j)].append((i+r[1],j+c[1]))
        if leftward(i,j,d_left)==True:
            adj_list[(i,j)].append((i+r[2],j+c[2]))
        if rightward(i,j,d_right)==True:
            adj_list[(i,j)].append((i+r[3],j+c[3]))  
            
BFS(adj_list,src,dest)

SHOW()
