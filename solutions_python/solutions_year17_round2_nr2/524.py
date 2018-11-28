import math

def main(n,r,o,y,g,b,v):
    if (o > 0 and  o > b - 1) or (g > 0 and g > r - 1) or (v > 0 and v > y - 1):
        if o == b and o + b == n:
            return 'OB' * (n//2)
        if g == r and g + r == n:
            return 'GR' * (n//2)
        if v == y and v+y==n:
            return 'VY' * (n//2)
        return "IMPOSSIBLE"
    b1 = b-o
    r1 = r-g
    y1 = y-v
    n1 = n-o-g-v
    if b1*2 > n1 or r1*2 > n1 or y1*2 > n1:
        return "IMPOSSIBLE"

    l = sorted([(b1, 'B'), (r1,'R'), (y1,'Y')],key=lambda x: x[0])
    answer=[]
    x = l[2][0] - l[1][0]
    for i in range(x):
        answer.append(l[0][1])
        answer.append(l[2][1])
        answer.append(l[1][1])
        answer.append(l[2][1])
    for i in range(l[1][0]-l[0][0]):
        answer.append(l[1][1])
        answer.append(l[2][1])
    for i in range(l[0][0]-x):
        answer.append(l[0][1])
        answer.append(l[1][1])
        answer.append(l[2][1])

    aaa = ''.join(answer)
    bbb = 'BO' * o + 'B'
    yyy = 'YV' * v + 'Y'
    rrr = 'RG' * g + 'R'

    return aaa.replace('B', bbb, 1).replace('Y',yyy,1).replace('R',rrr,1)


for c in range(int(input())):
    print("Case #%d: %s" % (c+1, main(*map(int, input().split()))))