f = open('A-large.in', 'r')
g = open('output.txt', 'w')

num = int(f.readline())
for i in range (num):
    data = f.readline().split()
    length = data[0]
    string = data[1]
    standing = 0
    extra = 0
    total = 0
    for pos in range(len(string)):
        extra = pos - standing
        if extra > 0:
            total += extra
            standing += extra
        standing += int(string[pos])
    s = "Case #" + str(i+1) + ": " + str(total) + '\n'
    g.write(s)

f.close()
g.close()
