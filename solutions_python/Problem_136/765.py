file = open('B-large.in', mode = 'r')
outfile = open('output.out', mode = 'w')
n = int(file.readline()[:-1])
result = []
for k in range(n):
    data = file.readline()[:-1].split(' ')
    c = float(data[0])
    f = float(data[1])
    x = float(data[2])
    i = 0
    s = 0
    cur = x/2
    prev = x
    while cur < prev:
        s = s + c/(2+i*f)
        prev = cur
        cur = s + x/(2+(i+1)*f)
        i += 1
    result.append(prev)

for i in range(n):
    outfile.write('Case #'+str(i+1)+': '+str(result[i])+'\n')

file.close()
outfile.close()
