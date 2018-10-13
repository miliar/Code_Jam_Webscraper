
#print("Case #{}: {} {}".format(i, n + m, n * m))

def tidy(n):
    x = 0
    for i in n:
        if x>int(i):
            return False
        x = int(i)
    return True

for a in range(int(input())):
    n = input()
    while(not(tidy(n))):
        n = str(int(n)-1)
    print("Case #{}: {}".format(a+1, n))

