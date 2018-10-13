'''
Created on 8 May 2010

@author: Jirasak.Chirathivat
'''

def calc(r, k, groups):
    euro = 0
    qs = 0
    size = len(groups)
    for i in range(r):
        count = 0
        for j in range(size):
            if count + groups[qs] > k:
                break
            count += groups[qs]
            qs += 1
            if(qs >= size):
                qs %= size
        euro += count
    return euro

if __name__ == '__main__':
    readfile = file('c.in')
    lines = readfile.readlines()
    
    i = 1
    lines = lines[1:]
    length = len(lines)
    for jj in range(0, length, 2):
        lineA = lines[jj].strip()
        lineB = lines[jj + 1].strip()
        r, k, n = [int(x) for x in lineA.split(' ')]
        groups = [int(x) for x in lineB.split(' ')]
        value = calc(r, k, groups)
#        n, k = [int(x) for x in line.strip().split(' ')]
#        value = checkOnOrOff(n, k)
        print 'Case #%s: %s' % (i, value)
        #print 'Case #%s:' % (i)
        i += 1 
    
    readfile.close()