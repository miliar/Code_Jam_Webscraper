#!/usr/bin/env python

if __name__=='__main__':
    in_file = open('input')
    out_file = open('output', 'w')
    T = int(in_file.readline())
    for t in range(1, T + 1):
        out_file.write('Case #%d:\n' % t)
        line = in_file.readline()
        l = line.split()
        r = int(l[0])
        c = int(l[1])
        graph = []
        count = 0
        out_g = []
        for i in range(0, r):
            graph.append(str(in_file.readline()))
            for j in range(0, c):
                if '#' == graph[i][j]:
                    count += 1
            out_g.append('.' * c)
        if count % 4 != 0:
            out_file.write('Impossible\n')
            continue
        remain = count
        for i in range(0, r - 1):
            for j in range(0, c - 1):
                if '#' == graph[i][j]:
                    if '#' == graph[i + 1][j] and \
                       '#' == graph[i][j + 1] and \
                       '#' == graph[i + 1][j + 1] and \
                       '.' == out_g[i][j] and \
                       '.' == out_g[i + 1][j] and \
                       '.' == out_g[i][j + 1] and \
                       '.' == out_g[i + 1][j + 1]:
                        out_g[i] = out_g[i][:j] + '/\\' + out_g[i][j + 2:]
                        out_g[i + 1] = out_g[i + 1][:j] + '\\/' + out_g[i + 1][j + 2:]
                        remain -= 4
        if remain:
            out_file.write('Impossible\n')
            continue
        for line in out_g:
            out_file.write(line + '\n')
    in_file.close()
    out_file.close()
