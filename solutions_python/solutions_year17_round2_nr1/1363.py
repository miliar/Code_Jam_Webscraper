fp = open('/Users/hareesh/Desktop/out.txt',"w")
for t in range(input()):
    d, n = map(int, raw_input().split())
    l = []
    for i in range(n):
        l.append( map(int, raw_input().split()) )
    ans =  float(d)/max([(d - p) / float(s) for (p, s) in l])
    fp.write(('Case #{}: '+str(ans)+'\n').format(t+1))
fp.close()