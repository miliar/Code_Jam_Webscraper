#!/usr/bin/env python

if __name__=='__main__':
    in_file = open('input')
    out_file = open('output', 'w')
    T = int(in_file.readline())
    for t in range(1, T + 1):
        line = in_file.readline()
        l_list = line.split()
        n = int(l_list[0])
        l = int(l_list[1])
        h = int(l_list[2])
        f_list = []
        line = in_file.readline()
        for f in line.split():
            f_list.append(int(f))
        for i in range(l, h + 1):
            found = True
            for j in f_list:
                if j % i != 0 and i % j != 0:
                    found = False
                    break
            if found:
                break
        out_file.write('Case #%d: ' % t)
        if found:
            out_file.write('%d\n' % i)
        else:
            out_file.write('NO\n')
    in_file.close()
    out_file.close()
