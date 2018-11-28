from _hashlib import new

fin = open('a.in', 'r')
out = open('a.out','w')
n = int(fin.readline())
print(n)

for i in range(n):
    line = fin.readline()
    c, f, x = map(float, line.split())
    print('%f %f %f' % (c, f, x))

    t_farm = 0
    v = 2
    t = x / v
    while True:
        t_farm += c / v
        v += f
        new_time = t_farm + x / (v)
        if new_time > t:
            out.write('Case #%d: %f\n' % (i+1, t))
            break
        t = new_time

fin.close()
out.close()
