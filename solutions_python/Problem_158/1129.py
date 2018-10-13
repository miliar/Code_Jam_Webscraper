X = []
R = [] 
C = []
I2 = [0,0] #stores 2nd input
inputfile = open('D-small-attempt4.in','r')
def ominous(x,r,c):
    if x>=7:
        return 'RICHARD'
    if (r*c)%x!=0:
        return 'RICHARD'
    if x==1 or x==2:
        return 'GABRIEL'
    if x==3:
        if r>c or r==c:
            if c==1:
                return 'RICHARD'
            else:
                return 'GABRIEL'
        else:
            if r==1:
                return 'RICHARD'
            else:
                return 'GABRIEL'
    if x==4:
        if r>c or r==c:
            if c==1 or c==2:
                return 'RICHARD'
            else:
                return 'GABRIEL'
        else:
            if r==1 or r==2:
                return 'RICHARD'
            else:
                return 'GABRIEL'           
    
        

for x in range(100):
    R.append(0)
    X.append(0)
    C.append(0)
while True:
    #C=int(input()) #Case numbers
    Cases=int(inputfile.readline())
    if 1<=Cases<=100: #Limits total case number
        for x in range(0,Cases):
                #i2 = input()
                i2=str(inputfile.readline())
                i2 = i2.rstrip('\n')
                I2 = i2.split(' ')
                X[x]=int(I2[0])
                R[x]=int(I2[1])
                C[x]=int(I2[2])
                
                
        for x in range(0,Cases):
            output = 'Case #'+str(x+1)+': '+ominous(X[x],R[x],C[x])
            print(output)
