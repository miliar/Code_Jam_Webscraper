#!/usr/bin/python
t = int(raw_input())
r = []
rr = []

def comm(r, rr):
    return [ele for ele in r if ele in rr]
def getg():
    guess = int(raw_input())
    matrix = []
    for j in range(0,4):
        s = raw_input()
        row = map(int,s.split()) 
        matrix.append(row)
        
    return matrix[guess-1]
    
for i in range(0,t):
    r = getg()
    rr = getg()
    sol = comm(r, rr)
    if (len(sol) == 1):
        print ("Case #"+str(i+1)+": "+str(sol[0]))
    elif (len(sol) == 0):
        print ("Case #"+str(i+1)+": Volunteer cheated!")
    else:
        print ("Case #"+str(i+1)+": Bad magician!")
            
            

 
 
        
