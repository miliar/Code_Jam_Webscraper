import math
fo = open('C-small-attempt0.in','rU');
fr = open('results.txt','w');

numTests = int(fo.readline().strip())
k = 0
while (k < numTests ):
    numFound = 0
    line = fo.readline().strip()
    bounds = line.split(' ')
    for i in range(int(bounds[0]), int(bounds[1]) + 1):
        square = False
        palin = False
        if (math.sqrt(i) == int(math.sqrt(i))):
            p = int(math.sqrt(i))
            p_str = str(p)
            p_list = list(p_str)
            p_rlist = reversed(p_list)
            p_rstr = "".join(p_rlist)
            p_r = int(p_rstr)
            if (p == p_r):
                square = True
        i_str = str(i)
        i_list = list(i_str)
        i_rlist = reversed(i_list)
        i_rstr = "".join(i_rlist)
        i_r = int(i_rstr)
        if (i == i_r):
            palin = True
        if (square and palin):
            numFound += 1
    fr.write('Case #{0}: {1}\n'.format(k+1,numFound))
    k += 1
fr.close()
fo.close()
