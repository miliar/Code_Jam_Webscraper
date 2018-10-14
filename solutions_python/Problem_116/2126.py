fname="A-large"
file=open(fname+".in","r").read().splitlines()
out=open(fname+".out","w")
limit=1000
T=int(file[0])
if T>limit: T=limit
T=T*5
file=file[1:T]
file.append('')
array=[];arr=[]
c=0

def rot(x):
    new=[];c=3
    for i in range(4):
        ar=x[0][c]+x[1][c]+x[2][c]+x[3][c]
        new.append(ar)
        c-=1
    ar=x[0][0]+x[1][1]+x[2][2]+x[3][3]
    new.append(ar)
    ar=x[3][0]+x[2][1]+x[1][2]+x[0][3]
    new.append(ar)
    return new

for i in range(len(file)):
    arr=[file[c],file[c+1],file[c+2],file[c+3]]
    w=rot(arr)
    array.append(arr+w)
    c+=5
    if c>=T: break

def findw(x):
    dot=0
    winner='Game has not completed'
    for i in range(len(x)):
        dot+=x[i].count('.')
        c=x[i].count('X')
        if dot==0:
            winner='Draw'
        if dot!=0:
            winner='Game has not completed'
        if c>=3:
            if (x[i].count('X')==4) or 'T' in x[i]:
                winner='X won'
                break
        v=x[i].count('O')
        if v>=3:
            if x[i].count('O')==4 or 'T' in x[i]:
                winner='O won'
                break
    return winner

for p in range(len(array)):
    win=findw(array[p])
    out.write('Case #'+str(p+1)+': '+win+'\n')
out.close()
