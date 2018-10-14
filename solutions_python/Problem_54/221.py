def gcd(a,b):
    while b > 0:
        a,b = b,a%b
    return a

f = open("jamcode.txt","r")
out = open("test.out","w")

c = int(f.readline())
for case in range(1,c+1):
    vals = [int(x) for x in f.readline().split()]
    N = vals[0]
    solution=abs(vals[2] - vals[1])
    for i in range(2,N):
        solution = gcd(abs(vals[i+1]-vals[i]),solution)
    solution = (solution - vals[1])%solution
    out.write("Case #{0}: {1}\n".format(case,solution))
out.close()
