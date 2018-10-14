__author__ = 'lexplua'
fin = open("input.txt", 'r')
fout = open("out.txt", 'w')

n_cases = int(fin.readline().strip())
for n in range(n_cases):
    c, f, x = [float(x) for x in fin.readline().strip().split()]
    cur = 2.0
    total = 0.0
    time = 0.0
    fout.write("Case #{}: ".format(n+1))
    while True:
        without_farm = (x - total)/cur
        with_farm = (c/cur) + (x - total)/(cur+f)
        time_diff = (c/cur)
        if without_farm > with_farm:
            time += time_diff
            total += time_diff*cur
            cur += f
            total -= c
            if total >= x:
                fout.write("%.7f\n" % (time - time_diff+with_farm))
                break
            continue
        else:
            fout.write("%.7f\n" % (time+without_farm))
            break
fin.close()
fout.close()
