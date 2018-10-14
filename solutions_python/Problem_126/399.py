import pdb
from string import maketrans

to_bin = maketrans("".join([chr(j) for j in range(ord("a"), ord("z") + 1)]),
                   "".join([str(1 if chr(j) in "aeiou" else 0) for j in range(ord("a"), ord("z") + 1)]))

def str2bin(s):
    return s.translate(to_bin)

def get_level(s, n):
    #pdb.set_trace()
    level = "0"*n
    if level not in s:
        return 0
    start = s.find(level)
    end = start + n
    return (start + 1)*(len(s)-end + 1) + get_level(s[start + 1:], n) + get_level(s[:end-1], n)

def main(args):    
    in_f = open(args[1])
    out_f = open(args[1]+".out", 'wt')
    cases = int(in_f.readline())
    for i in xrange(1, cases + 1):
        #pdb.set_trace()
        l = in_f.readline().split()
        s = str2bin(l[0])
        n = int(l[1])
        #pdb.set_trace()
        out_f.write("Case #%d: %d\n" % (i, get_level(s, n)))
    out_f.close()
    print "DONE!"

if __name__ == '__main__':
    import sys
    main(sys.argv)
        