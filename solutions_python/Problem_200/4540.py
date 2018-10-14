
# TIDY Brute FORCE:

n = int(input())

def ordertest(i,s):
    x = [int(x) for  x in str(s)]
    if sorted(x) == x:
        print("Case #{0}: {1}".format(i, s))
    else:
        ordertest(i,s-1)

for i in range(n):
    s=int(input())
    res=ordertest(i+1,s)
