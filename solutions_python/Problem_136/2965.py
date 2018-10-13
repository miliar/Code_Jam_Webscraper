import sys

infile = open('B-large.in','r')
outfile = open('B-large.out','w')

t = int(infile.readline())
for case in range(1,t+1):
    c,f,x = [float(x) for x in infile.readline().split()]

    cps = 2
    factories = 0
    total_t = x/cps
    factory_t = 0
    factory_count = 0

    while 1 > 0:
        cps = 2 + f*factory_count
        old_total_t = total_t
        total_t = x/cps + factory_t
        factory_t += c/cps
        if total_t > old_total_t:
            lowest_t = old_total_t
            break
        factory_count += 1

    outline = 'Case #' + str(case) + ': ' + str(lowest_t) + '\n'
    outfile.write(outline)
