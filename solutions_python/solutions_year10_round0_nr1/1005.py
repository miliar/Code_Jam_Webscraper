__author__="martyhu"
__date__ ="$May 8, 2010 11:25:20 AM$"

import re

if __name__ == "__main__":
    f = open('block', 'r')
    contents = f.readlines();
    o = open('output', 'w');

    s = re.compile(r'[\n]')

    for ln, line in enumerate(contents[1:]):

        l = s.split(line)
        l = line.split(' ')
        n = int (l[0])
        k = int (l[1])

        a = [0] * n

        for j in range(k):
            for i in range(n):
                if (0 == a[i]):                    
                    a[i] = 1
                    break
                else:
                    a[i] = 0

        result = "ON"
        for i in range(n):
            if (a[i] == 0): result = "OFF"

        line = 'Case #%s: %s' % (ln+1, result)
        o.write(line+'\n');