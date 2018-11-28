from DomainModel.TestCase import TestCase

def getPrimes(mm):
    primes = {x for x in range(3,mm,2)}
    primes.add(2)
    for x in range(3,mm):
        if x in primes:
            for y in range(x**2,mm,x*2):
                if y in primes:
                    primes.remove(y)
    return primes


class CoinSolver:
    def Test(self):
        f=open(r'c:\downloads\C-small.in.out2','rt')
        f.readline()
        mul = []
        for i in range(2,11):
            a=[i**x for x in range(32)]
            mul.append(a)
        cnt=0
        while True:
            line=f.readline()
            if not line:
                break
            cnt+=1
            a = line.split()
            b=a[0]
            b=b[::-1]
            val=list([0 for x in range(len(mul))])
            for k in range(len(mul)):
                for i in range(len(b)):
                    if b[i]=='1':
                        val[k]+=mul[k][i]
            for k,x in enumerate(val):
                dv = int(a[k+1])
                if x%dv!=0:
                    print ('{} = {}'.format(a[0],'failed'))
                    break
        print ("processed {}".format(cnt))

    def Solve(self):
        tests = int(input())
        for test in range(tests):
            n,jj = [int(x) for x in input().split()]
            m = n-2
            mul = []
            for i in range(2,11):
                a=[i**x for x in range(n)]
                mul.append(a)
            mm = int(sum(mul[len(mul)-1]) ** 0.5)+1
            primes = getPrimes(1000)
            b=[]
            for i in range(0,1<<(m)):
                vec = []
                for k in range(len(mul)):
                    val = mul[k][0] + mul[k][n-1]
                    for j in range(0,m):
                        if i&(1<<j):
                            val+=mul[k][j+1]
                    for x in primes:
                        if(val%x==0):
                            vec.append(x)
                            break
                if(len(vec)==9):
                    b.append((bin(1+(1<<(n-1))+(i<<1))[2:],vec))
                    if len(b)>=jj:
                        break

            print("Case #{}:".format(test+1))
            for i in range(len(b)):
                print("{} {}".format(b[i][0],' '.join([str(x) for x in b[i][1]])))

    def Solve2(self):
        tests = int(input())
        for test in range(tests):
            n,jj = [int(x) for x in input().split()]
            m = n-2
            mul = []
            for i in range(2,11):
                a=[i**x for x in range(n)]
                mul.append(a)
            mm = int(sum(mul[len(mul)-1]) ** 0.5)+1
            primes = {x for x in range(3,mm,2)}
            primes.add(2)
            for x in range(3,mm):
                if x in primes:
                    for y in range(x**2,mm,x*2):
                        if y in primes:
                            primes.remove(y)

            primes = sorted(primes)
            b=[]
            for i in range(0,1<<(m)):
                found=True
                vec = []
                for k in range(len(mul)):
                    val = mul[k][0] + mul[k][n-1]
                    for j in range(0,m):
                        if i&(1<<j):
                            val+=mul[k][j+1]
                    if val in primes:
                        found=False
                        break
                    else:
                        vec.append(val)
                if found:
                    vec2=[]
                    for y in vec:
                        for x in primes:
                            if y%x==0:
                                vec2.append(x)
                                break
                    if(len(vec2)==9):
                        b.append((bin(1+(1<<(n-1))+(i<<1))[2:],vec2))
                        if len(b)>=jj:
                            break

            print("Case #{}:".format(test+1))
            for i in range(jj):
                print("{} {}".format(b[i][0],' '.join([str(x) for x in b[i][1]])))

    def Tests(self):
        yield TestCase("""1
6 3
16 50
""","""Case #1:
100011 5 13 147 31 43 1121 73 77 629
111111 21 26 105 1302 217 1032 513 13286 10101
111001 3 88 5 1938 7 208 3 20 11
""")