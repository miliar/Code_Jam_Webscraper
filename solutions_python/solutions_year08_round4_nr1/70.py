#!/usr/bin/python

in_file = "in.in"
out_file = "in.out"

try:
    f_in = open(in_file)
except IOError:
    print in_file, "can not be opened, plz check it out!"
    
try:
    f_out = open(out_file,"w+")
except IOError:
    print out_file, "can not be opened, plz check it out!"    
    
N = int(f_in.readline())
M = V = n_inner = 0
node = []
change = []


def min(a,b):
    if a<b:
        return a
    else:
        return b
    
def max(a,b):
    if a>b:
        return a
    else:
        return b

def minchange(n, V):
    if n >= n_inner:
        if V==node[n]:
            return 0
        else:
            return -1
    
    #if node[n]==V:
    left = minchange(2*n+1, V)
    right = minchange(2*n+2, V)   
             
    if left==-1 or right==-1:
        temp1 = -1
    else:
        temp1 = left+right    
        
    # if node[n]!=V:
    if left==-1 and right==-1:
        temp2 = -1
    elif min(left,right)>=0:
        temp2= min(left,right)
    elif left>=0:
        temp2= left
    else:
        temp2= right
        
    if change[n]==0:
        if node[n]==V:
            return temp1
        else:
            return temp2
    else:
        if node[n]==V:
            buhuan = temp1
            huan = temp2
        else:
            buhuan = temp2
            huan = temp1
        
        if buhuan==-1 and huan==-1:
            return -1
        if buhuan == -1:
            return huan+1
        if huan == -1:
            return buhuan
        return min(buhuan, huan+1)
        
        

for time in range(0,N):
    line = f_in.readline().split()
    M = int(line[0])
    V = int(line[1])
    n_inner = (M-1)/2
    
    node = [0 for x in range(0,M)]
    change = [0 for x in range(0,n_inner)]
    
    for i in range(0,M):
        line=f_in.readline().split()
        node[i] = int(line[0])
        if i < n_inner:
            change[i] = int(line[1])
#    print node
#    print change
    result = minchange(0,V)
    if result >= 0:
        f_out.write("Case #" + str(time+1) + ": " + str(result) + "\n")
    else:
        f_out.write("Case #" + str(time+1) + ": IMPOSSIBLE\n")

print "Done"
f_in.close()
f_out.close()





