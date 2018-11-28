
fin = open('in.txt','r')
fout = open('out.txt','w')
data = fin.read()
data = data.split()
cases = int(data[0])
data = data[1:]
for i in range(cases):
    smax = int(data[0])
    data = data[1:]
    cumsum = 0
    to_add = 0
    for j in range(smax+1):
        if cumsum + to_add < j:
            to_add = j - cumsum
        cumsum += int(data[0][j])
    data = data[1:]
    fout.write('Case #'+ str(i+1) + ': ' + str(to_add) + '\n')

