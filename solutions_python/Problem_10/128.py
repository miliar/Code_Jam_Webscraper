import sys
fr = None
fw = None

def setup():
    if len(sys.argv) <= 1:
        print "Usage: \n\tpython <program name> <input file path>"
        return
    
    in_file = sys.argv[1]
    i = in_file.rfind('.')
    out_file = in_file[0:i] + '.out'
    global fr
    global fw
    fr = open(in_file, 'r')
    fw = open(out_file, 'w')

def done():
    fr.close()
    fw.close()

def solve(p, k, l, frq):
    #print p, k, l, frq
    p_c = 1
    key_c = 0
    t = 0
    for f in frq:
        #print f, t, p_c, key_c, k
        if key_c < k:
            key_c += 1
        else:
            p_c += 1
            key_c = 1
        t = t + p_c*f

    return str(t)
    

def write(i, s):
    fw.write("Case #" + str(i+1) + ": " + s + "\n")

def cmp1(a, b):
    return -cmp(a, b)

def main():
    setup()
    num_cases = int(fr.readline().strip())
    for i in xrange(num_cases):
        lt = [int(ig) for ig in fr.readline().strip().split(" ")]
        p = lt[0]
        k = lt[1]
        l = lt[2]
        frq = [int(ig) for ig in fr.readline().strip().split(" ")]
        frq.sort(cmp1)
        r = solve(p, k, l, frq)
        #print r
        write(i, str(r))
    done()

main()
