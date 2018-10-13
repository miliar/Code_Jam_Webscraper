import sys

def padd(x,y):
    x = '{0:b}'.format(x)
    y = '{0:b}'.format(y)
    xy= []

    width = max(len(x), len(y))
    x = '{0:0>{1}}'.format(x, width)
    y = '{0:0>{1}}'.format(y, width)
    
    for z in range(len(x)):
        if x[z] == y[z]:
            xy.append('0')
        else:
            xy.append('1')
    
    return int(''.join(xy), 2)


fin = open('C-large.in', 'r')
sys.stdout = open('C-large.out', 'w')

t = int(fin.readline())

for x in range(t):
    n = int(fin.readline())
    values = [int(y) for y in fin.readline().split(' ')]

    psum = 0
    for y in values:
        psum = padd(psum, y)

    ans = None
    if psum == 0:
        ans = str(sum(values) - min(values))
    else:
        ans = 'NO'

    print('Case #'+str(x+1)+': '+ans)

sys.stdout.close()
fin.close()
