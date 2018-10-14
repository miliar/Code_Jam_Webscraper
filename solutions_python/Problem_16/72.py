#!/usr/bin/python

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

for case in range(int(input())):
    k=int(raw_input())
    s = raw_input()
    ss=[]
    kk=[]
    for i in range(k):
        kk.append(i)
    
    for p in all_perms(kk):
        e=""
        index=0
        for j in range((len(s)/k)):
            for i in  range(len(p)):
                e += s[index+p[i]]
            index=index+k
        ss.append(e)
    
    
    sizes=[]
    for i in ss:
        size=0
        prv=""
        for j in range(len(i)):
            if i[j]!=prv:
                prv= i[j]
                size=size+1
        sizes.append(size)
        

    print "Case #%i: %i" % (case+1,min(sizes))
