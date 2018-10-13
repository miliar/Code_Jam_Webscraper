import random
def solve(n):
    done = False
    if(len(n) == 1):
        return n
    else:
        while(done == False):
            done = True
            current = len(n)-1
            for b in range(current):
                diff = len(n)-1
                if(diff != current):
                    n = "0" + n
                now = n[b]
                after = n[b+1]
                if(now > after):
                    done = False
                    n = str((int(n)-1))
        return str(int(n))
t = int(input())
for i in range(1,t+1):
    n = input()
    print("Case #{}: {}".format(i,solve(n)))
