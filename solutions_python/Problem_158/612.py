V=[]

T="smallCaseD.txt"

with open(r'D-small-attempt0.in','rt') as arch:
	for line in arch:
		V.append([int(i) for i in line[0:-1].split()])

t=V.pop(0)[0]

def sirve(X,R,C):
    if (R*C)%X!=0:
        return 'RICHARD'
    else:
        area=R*C
        if X==1:
            return 'GABRIEL'
        elif X==2:
            return 'GABRIEL'
        elif X==3:
            if area<X:
                return 'RICHARD'
            elif area==3:
                return 'RICHARD'
            else:
                return 'GABRIEL'
        else:
            if area<10:
                return 'RICHARD'
            else:
                return 'GABRIEL'


filee=open(T,'w')

for i in range(t):
    X=V[i][0]
    R=V[i][1]
    C=V[i][2]
    F=sirve(X,R,C)
    filee.write('Case #%i: %s' %(i+1,F))
    filee.write('\n')

