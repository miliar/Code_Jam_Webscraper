import sys

def check(l):
    for linea in l:
        cantx=0
        canty=0
        for col in linea:
            if(col=='T'):
                cantx+=1
                canty+=1
            if(col=='X'):
                cantx+=1
            if(col=='O'):
                canty+=1
        if(cantx == 4):
            return 1
        if(canty == 4):
            return 2
    return 0
 
def solve(a,b,c,d):
    l=[a,b,c,d]
    sol = check(l)
    if(sol!=0): return sol
    transposed=[]
    for i in [0,1,2,3]:
        tmp = ""
        for j in [0,1,2,3]:
            tmp += l[j][i]
        transposed.append(tmp)
    sol = check(transposed)
    if(sol!=0): return sol
    diag=['....']*4

    diag[0]=""
    for i in [0,1,2,3]:
        diag[0]+=l[i][i]
    sol = check(diag)
    if(sol!=0): return sol

    diag[0]=""
    for i in [0,1,2,3]:
        diag[0]+=l[i][3-i]
    sol = check(diag)
    if(sol!=0): return sol
 

    haylibres = 0+sum([1 for i in l if '.' in i])
    if(sol==0 and haylibres>0):
        sol=4
    return sol

def main():
    inputo = sys.stdin.readlines()
    n = int(inputo[0])
    for x,i in enumerate(inputo):
        inputo[x]=i.strip()
    for i in range(1,n+1):
        index = (i-1)*4+1+(i-1)
        sol = solve(inputo[index], inputo[index+1], inputo[index+2], inputo[index+3])
        case= "Case #"+str(i) + ": "
        if sol==4:
            print case + "Game has not completed"
        if sol==1:
            print case + "X won"
        if sol==2:
            print case + "O won"
        if sol==0:
            print case + "Draw"

    return 



if __name__=='__main__':
    main()
