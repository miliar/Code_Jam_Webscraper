
#map(int,f.readline().split())

def readex(f):
    tests = []
    numex = int(f.readline())
    for i in range(numex):
        tests.append( f.readline() )
    print tests
    
    return tests


def assignmap(plain,crypto,d = None):
    if not d:
        d = {}
    for pos in range(len(crypto[0:-1])):
        d[crypto[pos]] = plain[pos]
    return d

f = open('test.txt','r')
tests =  readex(f)
f.close()

a = 'our language is impossible to understand'
b = 'there are twenty six factorial possibilities'
c = 'so it is okay if you want to just give up'

d = {}
d['q'] = 'z'
d['y'] = 'a'
d['e'] = 'o'
d['z'] = 'q'
d = assignmap(a,tests[0],d)
d = assignmap(b,tests[1],d)
d = assignmap(c,tests[2],d)

print d

f = open('test1.txt','r')
tests = readex(f)
f.close()

f = open('jout.txt','w')
count = 1
for line in tests:
    newl = ['1'] * (len(line))
    for pos in range(len(line)):
        if line[pos] in d:
            newl[pos] = d[line[pos]]
    for pos in range(len(newl)):
        if newl[pos] == '1':
            newl[pos] = '\n'
    print line,
    print ''.join(newl)
    f.write('Case #' + str(count) + ': ' + ''.join(newl) )
    count = count + 1
f.close()    
            
            


