import sys

f = open(sys.argv[1])
t = f.readline()

o = open('o.txt', 'w')

for i in range(int(t)):
    n = f.readline().strip()
    n = list(n)
    for j in range(len(n)):
        if j + 1 < len(n):
            if n[j] > n[j + 1]:
                a = n.index(n[j])
                b = n.index(n[j]) + 1
                n[a] = str(int(n[a]) - 1)
                k = len(n[b:])
                n = n[:b]
                for _ in range(k):
                    n.append('9')
    n = ''.join(n).lstrip('0')
    o.write('Case #' + str(i+1) + ': ' + str(n) + '\n')

o.close()
