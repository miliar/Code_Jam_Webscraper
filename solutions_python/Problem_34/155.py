#!/usr/bin/python

infile = "A-large.in"
outfile = "A-large.out"

fin = open(infile)
fout = open(outfile, "w+")

(L, D, N) = (int(i) for i in fin.readline().split())

#create dict
dict = []
for i in range(0, D):
    dict.append(fin.readline().strip())

for i in range(0,N):
    s = fin.readline().strip()
#    print s
    
    l = [[] for tempi in range(0,L)]
    li = -1
    flag = 0
    for j in range(0, len(s)):
        if s[j] =='(':
            flag = 1
            li += 1
        
        if flag and s[j] == ')':
            flag = 0
        
        if (not flag) and str.isalpha(s[j]):
            li += 1
        
        if str.isalpha(s[j]):
            l[li].append(s[j])
#    print l
    
    count = 0
    for d in dict:
        flag = 1
        k = 0
        while flag and k<len(d):
            if d[k] not in l[k]:
                flag = 0
            k += 1
        if flag:
            count += 1
#            print "Match: %s" % (d)
    fout.write( "Case #%d: %d\n" % (i+1, count))

