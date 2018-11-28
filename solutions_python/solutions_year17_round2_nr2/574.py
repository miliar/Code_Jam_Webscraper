#Round 1b 2017 Problem B
#from collections import deque

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        n,r,o,y,g,b,v = [int(s) for s in raw_input().split(" ")]
        print "Case #{}: {}".format(i, smallinput(n,r,o,y,g,b,v))


def smallinput(n,r,o,y,g,b,v):
    assert o == 0 and g == 0 and v == 0
    l = []
    color = [[r,'r'],[y,'y'],[b,'b']]
    color.sort(reverse = True)
    l.extend([color[0][1],'']*color[0][0])
    for i in xrange(len(l)):
        if l[i] == '':
            if color[1][0] != 0:
                l[i] = color[1][1]
                color[1][0] -= 1
            elif color[2][0] != 0:
                l[i] = color[2][1]
                color[2][0] -= 1
    #overflow
    if color[2][0] > 0:
        i = 1
        while color[2][0] > 0:
            l.insert(3*i-1,color[2][1])
            color[2][0] -= 1
            i+=1
        return ''.join(l)
    if '' in l:
        return 'IMPOSSIBLE'
    else:
        return ''.join(l)

def input():
     t = int(raw_input())
     for i in xrange(1, t+1):
        n,r,o,y,g,b,v = [s for s in raw_input().split(" ")]
        print "Case #{}: {}".format(i, ''.join([n,r,o,y,g,b,v]))

if __name__ == '__main__':
   main()
