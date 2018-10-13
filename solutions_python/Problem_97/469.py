def generate_recycled(number):
    str_num = str(number)
    for i in xrange(1, len(str_num)):
        yield int(str_num[i:] + str_num[:i])


def generate_pairs(A,B):
    for n in xrange(A,B+1):
        for m in generate_recycled(n):
            if n<m and m<=B:
                yield (n,m)

def count_pairs(A,B):
    pairs = generate_pairs(A,B)
    return len(set(pairs))

with open("recycled_pairs.txt") as f:
    n = int(f.readline().strip())
    for i in range(n):
        a,b = [int(x) for x in f.readline().strip().split(' ')]
        print "Case #%d: %d" % (i+1,count_pairs(a,b))
