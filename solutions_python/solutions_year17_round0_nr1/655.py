import sys
sys.setrecursionlimit(1500)

dict = {'+':1,'-':0}

def process(s,k):
    if not 0 in s:
        return (True, 0)
    else:
        i = s.index(0)
        if i+k-1 >= len(s):
            return (False, -1)
        else:
            snew = [1 - x for x in s[i:i+k]] + s[i+k:]
            (possible, flips) = process(snew,k)
            return (possible, flips+1)
    



t = int(input())
for i in range(1, t+1):
    inp = input().split()
#   print(inp)
    s = str(inp[0])
    k = int(inp[1])
    s = [dict [x] for x in list(s)]
#   print(s)
    (possible, flips) = process(s, k)
    if possible:
        answer = flips
    else:
        answer = 'IMPOSSIBLE'
    print("Case #{}: {}".format(i,answer))


    
    



