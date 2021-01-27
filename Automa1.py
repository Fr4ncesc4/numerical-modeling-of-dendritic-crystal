import numpy as np
import matplotlib.pyplot as plt
import random
#=============================================================================================
#DEFINIZIONI DELLE FUNZIONI


###UPDATE PRENDE I VALORI DI X E Y DEI PIXEL DI SUPERFICIE E AGGIORNA LO STATO DELLA GRIGLIA
# pos 
def Update(grid,pos):
    XY = random.choice(pos) #estrae un pixel a caso da positions
    grid[XY[0],XY[1]] = False

###TROVA LE X E Y DEI PIXEL SULLA SUPERFICIE
def SurfPoints(grid):
    pos = []
    for i in range(N):
        for j in range(N):
            if ( grid[i,j] == False ):
                #periodi boundary conditiond
                if(i+1 == N):
                    ii = -1
                    if( grid[ii+1,j] == True ):
                        pos.append([ii+1,j])
                else:
                    if( grid[i+1,j] == True ):
                        pos.append([i+1,j])
                if(i == 0):
                    ii = N
                    if( grid[ii-1,j] == True ):
                        pos.append([ii-1,j])
                else:
                    if( grid[i-1,j] == True ):
                        pos.append([i-1,j])
                if(j+1 == N):
                    jj = -1
                    if( grid[i,jj+1] == True ):
                        pos.append([i,jj+1])
                else:
                    if( grid[i,j+1] == True ):
                        pos.append([i,j+1])
                if(j == 0):
                    jj = N
                    if( grid[i,jj-1] == True ):
                        pos.append([i,j-1])
                else:
                    if( grid[i,j-1] == True ):
                        pos.append([i,j-1])         
                    
    new_pos = []
    for elem in pos:
        if elem not in new_pos:
            new_pos.append(elem)
    pos = new_pos
    return pos

#============================================================================================
#MAIN

N = 250 #numero di pixel per asse della griglia
Ng = 70  #NUMERO INIZILE DI GERMI DI CRESCITA
T = 250 #numero di step di aggiornamento, tempo fisico della simulazione
dim = [N,N] #dimensioni della griglia di simulazione
grid = np.ones(dim,dtype=np.bool) #griglia di simulazione: pixel di valore binario,
                                  #True == 1 corrisponde a cella vuota
                                  #False == 0 corrisponde a cella piena

random.seed(0)        
        
K = range(N)

RandX = random.choices(K,k=Ng)
RandY = random.choices(K,k=Ng)

for i in range(Ng):
    grid[RandX[i],RandY[i]] = False

### PLOT DELLO STATO ATTUALE DELLA GRIGLIA
plt.imshow(grid) 
plt.show()

for t in range(T):
    Positions = SurfPoints(grid) #pixel dei primi vicini vuoti della superficie (pixel che possono essere colorati)
    Update(grid,Positions)

plt.figure(figsize=(10,10))
plt.imshow(grid) 
plt.show()
