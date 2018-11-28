# f = ['132\n',
     # '1000\n',
     # '7\n',
     # '111111111111111110\n']

f = open('B-small-attempt0.in', 'r+')
f.readline()

w = open('out.out', 'w+')

cnt = 1

for i in f:
    for n in range(int(i), -1, -1):
        is_tidy = False
        n = str(n)+chr(58)
        for c1, c2 in zip(n, n[1:]):
            if ord(c1) > ord(c2):
                is_tidy = False
                break
        else:
            is_tidy = True
            
        if is_tidy:
            w.write('Case #{}: {}\n'.format(cnt, n[:-1]))
            cnt += 1
            break