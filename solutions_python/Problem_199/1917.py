def flip( s ):
    ss = s
    ss = ss.replace('-', '/')
    ss = ss.replace('+', '-')
    ss = ss.replace('/', '+')
    return ss

def solve(s, k):
    ss = s
    flips = 0
    for i in range( len(ss)-k+1 ):
        if( k == len(ss) ):
            break
        if ss[i] == '-':
            ss = ss[:i] + flip( ss[i: i+k] ) + ss[i+k:]
            flips = flips + 1

    if ss[-k:].find('-') > -1:
        if( k == len(ss) ):
            ss = flip(ss)
        if ss[-k:].find('-') > -1:
            return [False, 0]
        else:
            return [True, 1]
    else:
        return [True, flips]

t = int(input())

for i in range(1, t+1):
    c, k =[ str(s) for s in input().split(" ") ]
    k = int(k)
    [solvable, flips] = solve(c, k)
    if solvable:
        print( "Case #{}: {}".format(i, flips))
    else:
        print( "Case #{}: IMPOSSIBLE".format(i))