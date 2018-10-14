import sys

def recycle(a, b):
        d1 = []
        d2 = []
        A, B = a, b
        while(a):
                d1.append(a % 10)
                a /= 10
        while(b):
                d2.append(b % 10)
                b /= 10

        d1.reverse()
        d2.reverse()
        if(d1.sort() != d2.sort()):
                return 0

        s1, s2 = len(d1), len(d2)
        if(s1 != s2):
                return 0
        mul = 10**(s1-1)
        for i in range(s1):
                A = (A/10) + mul*(A%10)
                if(A == B):
                        return 1
        return 0
                    
n = int(raw_input())
for i in range(n):
        cnt = 0
        a, b = [int(x) for x in raw_input().split()]
        for j in range(a, b+1):
                for k in range(j+1, b+1):
                        if(recycle(j, k)):
                                cnt += 1
        sys.stdout.write("Case #%d: %d\n" % ((i+1), cnt))
        sys.stdout.flush()
