tc = int(input())
def check(n):
    for i in range(1,len(str(n))):
        if int(n[i-1]) > int(n[i]):
            return False
    return True

for i in range(tc):
    lp = int(input())
    for j in range(lp,-1,-1):
        if check(str(j)):
            print("Case #{}: {}".format(i+1,j))
            break
    