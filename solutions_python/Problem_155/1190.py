import codecs
with codecs.open('1.txt', 'r', 'utf-8') as f:
    a = f.readlines()
output = ''
for i in range(len(a[1:])):
    line = a[i+1]
    standing = 0
    needed = 0
    for j in range(len(line.split(' ')[1].strip())):
        number = int(line.split(' ')[1][j])
        th = 0
        if standing < j:
            th = j - standing
            needed += th
        standing += number + th
    output += 'Case #%d: %d\n' % (i + 1, needed)
with codecs.open('1_o.txt', 'w', 'utf-8') as f:
    f.write(output)
