#!/usr/bin/env python

def mbf(m, n):
    list = []
    for i in xrange(m,n+1):
        tmp = str(i)
        l = len(tmp)
        for ii in xrange(l):
            str1 = tmp[0:ii]
            str2 = tmp[ii:l]
            if str2.startswith("0"):
                pass
            else:
                nstr = str2+str1
            if int(nstr)<=n and m < int(nstr):
                if i < int(nstr):
                    if [i,int(nstr)] not in list: list.append([i,int(nstr)])
                elif i > int(nstr):
                    if [int(nstr),i] not in list: list.append([int(nstr),i])
    return list
                           
        
        
if __name__ == '__main__':
    f = open("C-small-attempt0.in")
    dat = f.readlines()
    lnum = int(dat[0])
    for i in xrange(1,lnum+1):
        d = dat[i].split(" ")
        print "Case #%d: %d" % (i,len(mbf(int(d[0]),int(d[1]))))