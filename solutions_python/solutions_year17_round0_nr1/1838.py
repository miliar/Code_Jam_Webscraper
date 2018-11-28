import sys

f = open(sys.argv[1])
t = f.readline()

o = open('o.txt', 'w')

for i in range(int(t)):
    l = f.readline()
    s, k = l.split(' ')
    k = int(k)
    s = list(s)
    r = 0
    e = 0
    while '-' in s:
        if r > 1000000000000000000 or e:
            r = 'IMPOSSIBLE'
            break
        for j in range(len(s)):
            if s[j] == '-':
                for z in range(k):
                    if j + k > len(s):
                        e = 1
                        break
                    if s[j + z] == '-':
                        s[j + z] = '+'
                    else:
                        s[j + z] = '-'
                r += 1
                j += k
    s = ''.join(s)
    o.write('Case #' + str(i+1) + ': ' + str(r) + '\n')

o.close()
