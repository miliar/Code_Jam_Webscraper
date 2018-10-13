import sys
fileinput = sys.stdin

# import StringIO
# fileinput = StringIO.StringIO(inputstr)

T=int(fileinput.readline())
for t in range(T):
    #N=int(fileinput.readline().strip())    
    tidy=True
    N=fileinput.readline().strip()
    d = list(N)
#     if '0' in d:
#         print "Case #%s: %s" % (t+1, '9'*(len(d)-1))
#         continue
    for i in range(len(d)-1):
        if d[i]>d[i+1]:
            tidy=False
            break
    if tidy:
        print "Case #%s: %s" % (t+1, ''.join(d))
        continue
    while i>0 and (d[i-1]==d[i]):
        i -= 1
    d[i]=str(int(d[i])-1)
    for j in range(i+1,len(d)):
        d[j]='9'
    if d[i]=='0':
        d.pop(i)
    print "Case #%s: %s" % (t+1, ''.join(d))
        