def tidy(n):
    while n >0:
        if n%10 < (n//10)%10:
            return False
        n//=10
        #print(n)
    return True

def maketidy(n):
    tp=1
    while not tidy(n):
        n -= (n % (10 ** tp) // (10 ** (tp - 1))) * 10 ** (tp - 1)
        n -= (10 ** (tp - 1))
        tp += 1
    return n


inp = (input())
inp = int(inp)

for i in range(inp):
    tmpi = input()
    tmpi=int(tmpi)
    if tidy((tmpi)):
        print('Case #' + str(i + 1) + ': ' + str(tmpi))
    else:
        tmpi = maketidy(tmpi)
        print('Case #' + str(i + 1) + ': ' + str( maketidy(tmpi)))
