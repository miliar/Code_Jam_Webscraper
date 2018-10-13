''' 
April 22, 2017
'''
tc = int(raw_input())

for i in range(1,tc+1):
    print "Case #"+str(i)+':',
    d,n = map(int,raw_input().split())
    k,s = list(), list()
    tim=list()
#     print n,'is n'
    for _ in range(n):
        vals = map(int, raw_input().split())
#         print vals
        k.append(vals[0])
        s.append(vals[1])
        tim.append(float((d-vals[0])*1.0/vals[1]))
    mtim=max(tim)
    print str(round(float(d)/mtim,6) ) 