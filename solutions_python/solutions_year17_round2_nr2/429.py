from __future__ import division

lines = open('b.in').read().splitlines()
test = int(lines[0].strip())
out = open('output.txt', 'w')

lno = 0
tot = 0
for testno in range(test):
    lno += 1
    n,r,o,y,g,b,v = map(int, lines[lno].strip().split())
    # print n,r,o,y,g,b,v
    # r,y,b
    colors = [r,y,b]
    colors.sort(reverse=True)
    f,s,t = None, None, None
    if not f:
        if colors[0]==r:
            f = 'R'
        elif colors[0]==y:
            f = 'Y'
        else:
            f = 'B'
    if not s:
        if colors[1]==r and f!='R':
            s = 'R'
        elif colors[1]==y and f!='Y':
            s = 'Y'
        else:
            s = 'B'
    if not t:
        if colors[2]==r and f!='R' and s!='R':
            t = 'R'
        elif colors[2]==y and f!='Y' and s!='Y':
            t = 'Y'
        else:
            t = 'B'
    r, b, y= colors
    s, t = t, s
    soln2 = ''
    flag= True
    turn = True
    for i in range(r):
        soln2+=f
        # if testno==1:
            # print soln2
        if i!=r-1 and y==0 and b==0:
            flag = False
            break
        if y!=0:
            soln2+=s
            y-=1
        elif b!=0:
            soln2+=t
            b-=1

    if y!=0:
        flag = False

    if flag is False:
        case = "Case #%d: IMPOSSIBLE" %(testno+1,)
        print case
        out.write(case+'\n')
        continue

    soln3 = ''
    pos = 0
    while b!=0:
        soln3 += soln2[pos]
        pos+=1
        if pos<len(soln2) and soln2[pos]==t:
            flag = False
            break
        soln3+=t
        b-=1
    # print soln2, soln3
    soln3 += soln2[pos:]

    if flag is False or soln2[0]==soln2[-1]:
        case = "Case #%d: IMPOSSIBLE" %(testno+1)
        print case
        out.write(case+'\n')
        continue

    tot+=1
    soln = ''
    case = "Case #%d: %s" %(testno+1, soln3)
    print case
    out.write(case+'\n')
# print 'Total',tot
out.close()

