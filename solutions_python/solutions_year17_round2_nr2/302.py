T = int(raw_input())

def canAdj(a,b):
    if a < 0 or b < 0:
        return True
    if abs(a-b) <= 1 or abs(a-b) == 5:
        return False
    return True

# memo = dict()
# def find(rest, final,depth=1):
#     if depth > 1000:
#         print depth
#     global memo
#     if rest == (0,0,0,0,0,0):
#         memo[(rest,final)] = 1
#         return 1
#     if (rest,final) in memo:
#         return memo[(rest,final)]
#     left = list(rest)
#     ans = 0
#     for i in range(6):
#         if left[i] > 0 and canAdj(i,final):
#             left[i] -= 1
#             ans += find(tuple(left),i,depth+1)
#             left[i] += 1
#     memo[(rest,final)] = ans
#     return ans


# def findpath(start,left):
#     global memo
#     s = [start]
#     l = [0]*6
#     while(left != tuple(l)):
#         for i in range(6):
#             if canAdj(i,s[-1]) and (tuple(l),i) in memo and memo[(tuple(l),i)] > 0:
#                 s += [i]
#                 l[i] += 1
#                 break
#     return s

def tokenize(i):
    l = "ROYGBV"
    return l[i]
for x in range(T):
    N = map(int, raw_input().split(' '))
    colors = N[1:]
    N = N[0]
    memo = dict()
    start = 0
    while colors[start] == 0:
        start += 1
    colors[start] -= 1
    s = [start]
    N-=1
    while N > 0:
        best = 0
        for i in range(6):
            if canAdj(i,s[-1]) and colors[i] > best:
                best = colors[i]
                besti = i
        if best == 0:
            s = []
            break
        s.append(besti)
        colors[besti] -= 1
        N -= 1
    if s and not canAdj(s[0],s[-1]):
        s = []
    print "Case #"+str(x+1)+":",
    if s == []:
        print("IMPOSSIBLE")
    else:
        print("".join(map(tokenize,s)))
