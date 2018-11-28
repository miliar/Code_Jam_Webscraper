import sys

def espal(string):
    for i in range(0,len(string)):
        if string[i]!=string[-(i+1)]:
            return False
    return True

def FairSquareSimple(fname,sname):
    with open(fname) as file:
        with open(sname,'w') as salida:
            line = file.readline()
            T=int(line)
            for case in range(1,T+1):
                [A,B]=[int(i) for i in file.readline().split()]
                total=0
                for n in range(A,B+1):
                    if espal(str(n)):
                        raiz=int(n**(0.5))
                        while raiz*raiz<n:
                            raiz+=1
                        if (raiz*raiz)==n and espal(str(raiz)):
                            total+=1
                salida.write("Case #{0}: {1}\n".format(case,total))
        salida.close()
    file.close()
