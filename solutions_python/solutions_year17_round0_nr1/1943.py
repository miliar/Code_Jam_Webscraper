import sys

def flip(s,k,i):
    for l in range(k):
        if s[l+i]=='+':
            s[l + i]='-'
        else:
            s[l + i] = '+'
    return s



f1 = open('A-large.in', 'r')
# print f1
T=f1.readline()
#print f1.readline(2)
print T
for t,line in enumerate(f1):
    # print ''
    # print line
    [s,k]= line.split()
    count=0
    s=list(s)
    # sys.stdout = open('pancake.txt', 'w')
    # sys.stdout = 'pancake.txt'
    for i in range(len(s)-int(k)+1):
        if s[i]=='-':
            count=count+1
            s=flip(s,int(k),i)
    if s.count('+') == len(s):

        # print 'test'
        sys.stdout = open('pancake.txt', 'a')
        print 'Case #%d: %d' %(t+1,count)
        # print 'Value is "%d", but math.pi is %.2f' % (value, math.pi)
    else:
        # print 'Case #',t+1, ': IMPOSSIBLE'
        # sys.stdout = open('pancake.txt', 'w')
        sys.stdout = open('pancake.txt', 'a')
        print 'Case #%d: IMPOSSIBLE' % (t + 1)
