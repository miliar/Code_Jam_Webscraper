#/usr/bin/python
# -*- encoding: utf-8 -*-

filename = 'A-large.in.txt'

with open(filename, 'r') as f:
    content = f.read().splitlines()
    l =  int(content[0])
    result = []
    # print l
    for i in range(l):
        # do something to determine how many we need to invete
        line = content[i+1].split()
        Smax = int(line[0])
        Si = [int(x) for x in line[1]]
        # print Si
        need = 0
        for inx in range(Smax+1):
            if inx > sum(Si[:inx:]):
                cha = inx - sum(Si[:inx:])
                need += cha
                Si[inx-1] += cha
        result.append(need)
        print Si
    # print result


# Output
with open('Asmall.output', 'w') as the_file:
    for line in range(l):
        the_file.write('Case #{}: {}\n'.format(line+1, str(result[line])))
