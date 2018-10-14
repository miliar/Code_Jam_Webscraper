infile = open('taskA.txt','r')
n = infile.readline()
for i in range(0,int(n)):
    line = infile.readline()
    k = line[0]
    s = line[2:]
    if i < int(n)-1:
        s = s[:-1]
    out = 0
    need = 0
    for j in range(int(k)+1):
        if j > out:
            need = need + j - out
            out = j
        out = out + int(s[j])
    print 'Case #'+str(i+1)+':',need

infile.close()
