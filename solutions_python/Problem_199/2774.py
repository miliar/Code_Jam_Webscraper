# encoding=utf-8
f = open('A-large.in','r')
w = open('A-large.out','w')

t = int(f.readline())
#t = int(raw_input())

for i in range(t):
    line = f.readline().split()
    #line = raw_input().split()

    s =  line[0]
    k =  int(line[1])
    a = 0

    for j in range(len(s)-k+1):
        #print "pasada", j
        if s[j] == '-':
            r = ''
            a += 1
            for h in range(k):
                if s[j + h] == '-':
                    r += '+'
                else:
                    r += '-'
            #print "valor r:",r
            #print "valor s1:",s
            s = s[:j] + r + s[j + k:]
            #print "valor s2:", s

    for j in range(len(s)):
        if s[j] == '-':
            a = -1

    if a == -1:
        #print "Case #{}: IMPOSSIBLE".format(i+1)
        w.write("Case #{}: IMPOSSIBLE".format(i+1) + '\r')
    else:
        #print "Case #{}: {}".format(i+1,a)
        w.write("Case #{}: {}".format(i+1,a) + '\r')

f.close()
w.close()