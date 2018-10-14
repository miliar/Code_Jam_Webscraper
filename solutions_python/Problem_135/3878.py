import sys

def process(g1, g2, m1, m2):
    count = 0
    value = None
    for item in m1[g1]:
        if item in m2[g2]:
            count +=1
            value = item
    return ([count, value])

def output(count, value):
    if count == 0:
        return ('Volunteer cheated!')
    elif count >=2:
        return ('Bad Magician!')
    else:
        return (str(value))

infileStr = sys.argv[1]
infile = open (infileStr)
outfile = open ('q1out.txt', 'w')
cases = infile.readline()
print (cases)
cases = int(cases)
for i in range (cases):
    g1 = int(infile.readline())-1
    m1 = []
    for j in range (4):
        line = list(infile.readline().split())
        line = list(map(int,line))
        m1.append(line)
    g2 = int(infile.readline())-1
    m2 = []
    for j in range (4):
        line = list(infile.readline().split())
        line = list(map(int,line))
        m2.append(line)
    print (g1)
    print (g2)
    print (m1)
    print (m2)
    c,v = process(g1,g2,m1,m2)
    print('Case #{0}: {1}'.format(i+1, output(c,v)))
    outfile.write('Case #{0}: {1}\n'.format(i+1, output(c,v)))
outfile.close()
