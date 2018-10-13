fin = open('A-small-attempt1.in', 'rb')
fout = open('output.txt', 'wb')

T = int(fin.readline().strip())

refr = 'y n f i c w l b k u o m x s e v z p d r j g t h a q'.split()
repl = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
D = dict(zip(refr, repl))
print [(x, D[x]) for x in sorted(D)]

for case in range(1, T + 1):
    line = fin.readline().strip()
    for c in D:
        line = line.replace(c, D[c])
    line = line.lower()

    fout.write('Case #' + str(case) + ': ' + line + '\n')
fout.close()
