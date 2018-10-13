

def f(X,F,C,n):
    return sum(C/(2+F*i) for i in range(n)) + X/(2+F*n)

def solution1(X,F,C):
    n = 1
    f_1 = f(X,F,C,0)
    f_2 = f(X,F,C,1)
    while(f_1 > f_2 ):
        n += 1
        f_1 = f_2
        f_2 = f(X,F,C,n)
    return n-1

filein = open( "B-small-attempt0.in", "r" )
out = open( "B_small.out", "w")

#Test cases
n = int(filein.readline())

for i in range(n):
    row = filein.readline().split()
    C = float(row[0])
    F = float(row[1])
    X = float(row[2])
    sol = solution1(X,F,C)
    print sol
    text = "Case #"+str(i+1)+": "+str(round(f(X,F,C,sol),6))+"\n"
    print text
    out.write(text)
    
filein.close()
out.close()
