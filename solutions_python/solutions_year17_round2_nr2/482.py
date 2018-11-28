import sys
'''
For small, just take more common allowed at each step
Impossible if that can't be done, usu. too many of one kind
For large, need to sub in OBO and related triples, based off of small answer
'''

if __name__  == '__main__':
    xx = sys.stdin.readline()
    num = 0
    while True:
        line = sys.stdin.readline()
        if not line: break
        num += 1
        (n,r,o,y,g,b,v) = line.strip().split()
        n = int(n)
        r = int(r)
        o = int(o)
        y = int(y)
        g = int(g)
        b = int(b)
        v = int(v)
        k = {} # count of each type
        k['R'] = r - g
        k['Y'] = y - v
        k['B'] = b - o
        #k['O'] = o
        #k['G'] = g
        #k['V'] = v
        # for each O G V, need BOB RGR YVY substitution
        # count each O as a B, knowing that one B has to be BOB, decrement O and B by one
        orig = dict(k)

        if max(k.values())*2 > n: # too many of one - impossible
            print 'Case #'+str(num)+': IMPOSSIBLE'
            continue
            
        ring = ''
        prev = ''
        while len(ring) < n:
            for x in sorted(k,key=lambda a: (k[a], orig[a]),reverse=True): # most common first
                if x == prev: continue
                if k[x] <= 0: continue
                k[x] -= 1
                ring += x
                prev = x
                if x == 'B' and o > 0: # do BOB
                    while o > 0: #add at once if possible -  may as well
                        ring += 'OB'
                        o -= 1
                elif x == 'R' and g > 0: # do BOB
                    while g > 0: #add at once if possible -  may as well
                        ring += 'GR'
                        g -= 1
                elif x == 'Y' and v > 0: # do BOB
                    while v > 0: #add at once if possible -  may as well
                        ring += 'VY'
                        v -= 1
                break
            else:
                if sum(k.values()) == 0: # emptied RGB - check for empty ring, remaining ogv
                    if o > 0:
                        ring += 'OB'*o
                        v = 0
                    elif g > 0:
                        ring += 'GR'*g
                        g = 0
                    elif v > 0:
                        ring += 'VY'*v
                        v = 0
                break
        if sum(k.values()) != 0 or o > 0 or g > 0 or v > 0:
            print 'Case #'+str(num)+': IMPOSSIBLE'
            #print k, o, g, v, ring
            continue
        print 'Case #'+str(num)+': '+ ring

        
