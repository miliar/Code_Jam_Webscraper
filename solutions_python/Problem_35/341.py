#!/usr/bin/python
import sys
import re

def main():
    f = open(sys.argv[1])
    num_of_map = int(f.readline())
    #print num_of_map
    for i in range(num_of_map):
        bmap = []
        (h, w) = f.readline().split()
        #print h,w
        h = int(h)
        w = int(w)
        for j in range(h):
            row = [int(x) for x in f.readline().split()]
            bmap.append(row)
        #print bmap
        bmap2 = [['.']*w for row in range(h)]

        mark = 'a'
        
        #print bmap2
    
        beg = (0,0)
        total_searchs = []
        while True:
            searchs = []
            wraps = []
            while True:
                searchs.append(beg)
                bmap2[beg[0]][beg[1]] = mark
                beg = flowto(bmap, beg[0], beg[1], wraps)
                if beg == (None, None):
                    break
                else:
                    bmap2[beg[0]][beg[1]] = mark
            #print searchs
            wraps = list(set(wraps)-set(searchs) - set(total_searchs))
            while True:
                wraps, searchs = wrapit(wraps, searchs, bmap, bmap2, mark)
                if wraps == []:
                    break

            beg = findbeg(bmap2)
            mark = chr(ord(mark)+1)

            if beg == None:
                break
            total_searchs.extend(searchs)

        print 'Case #%d:' % (i+1)
        printmap(bmap2)
    f.close()

def findbeg(bmap2):
    for i,j in enumerate(bmap2):
        for m,n in enumerate(j):
            if n == '.':
                return (i,m)
    return None

def wrapit(wraps, searchs, bmap, bmap2, mark ):
    nwraps = wraps[:]
    nsearchs = searchs[:]
    wraps = []
    wrap = []
    dels = []
    maybes = []
    news = []
    for i in nwraps:
        ret = flowto(bmap, i[0], i[1], wrap)
        if ret in nsearchs:
            bmap2[i[0]][i[1]] = mark
            news.append(i)
            wraps.extend(wrap)
        else:
            maybes.append(i)
        wrap = []
    found = True
    while found:
        found = False
        for i in maybes[:]:
            ret = flowto(bmap, i[0], i[1], wrap)
            if ret in news:
                bmap2[i[0]][i[1]] = mark
                news.append(i)
                wraps.extend(wrap)
                found = True
                maybes.remove(i)
            wrap = []
    
    wraps = list(set(wraps)-set(searchs).union(set(news)) - set(maybes))
    searchs = list(set(searchs).union(set(news)))
    return wraps, searchs


def printmap(bmap2):
   for r in bmap2:
       for c in r:
           print c,
       print


def flowto(bmap, row, col, wrap):
    bmin = ['','','','']
    pos = [(row-1,col),(row,col-1),(row,col+1),(row+1,col)]
    for m,n in enumerate(pos):
        #print 'n0,n1',n[0],n[1]
        if (n[0] < 0) or (n[0] >= len(bmap)) or (n[1] < 0) or (n[1] >= len(bmap[0])):
            continue
        bmin[m] = bmap[n[0]][n[1]]
    #print bmin
    m = ''
    for x in bmin:
        if x < m:
            m = x

    d = bmin.index(m)
    if m < bmap[row][col]:
        for i,j in enumerate(bmin):
            if j != '':
                wrap.append(pos[i])
        return (pos[d][0], pos[d][1])
    for i,j in enumerate(bmin):
        if j != '':
            wrap.append(pos[i])
    return (None, None)


if __name__ == '__main__':
    main()
