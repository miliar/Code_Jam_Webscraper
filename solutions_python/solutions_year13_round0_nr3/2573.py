from math import sqrt

def isfairandsquare(n):
    if n==n[::-1] and int(sqrt(int(n)))**2==int(n):
        n=str(int(sqrt(int(n))))
        if n==n[::-1]:
            return True
    return False

if __name__=='__main__':
    challenge='C-small-attempt0.in'
    entrance=open(challenge,'r')
    solution=open('03solution.txt','w')
    cases=int(entrance.readline())
    for caso in range(1,cases+1):
        n=0
        lista=entrance.readline().split()
        for i in range(int(lista[0]),int(lista[1])+1):
            if isfairandsquare(str(i)):
                n=n+1
        solution.write('Case #%d: %d\n'%(caso,n))
    entrance.close()
    solution.close()
