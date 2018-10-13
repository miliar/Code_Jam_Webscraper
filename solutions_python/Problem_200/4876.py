import itertools
text = open('B-small-attempt0.txt', 'r').read().split('\n')
count = int(text[0])


def isinc(num):
    for i in xrange(num, 0, -1):
        if int("".join(j for j in sorted(str(i)))) == i:
            break
    return i


fid = open('output.txt', 'w')
for j in xrange(1, count + 1):
    val = (isinc(int(text[j])))
    fid.write("Case #{}: {}\n".format(j, val))
fid.close()
