# To change this template, choose Tools | Templates
# and open the template in the editor.

import random
__author__="nsho"
__date__ ="$2010/05/08 8:00:25$"

debug=False

# resume
def get_nr_need(n):
    ret = k = 1
    for i in xrange(1, n):
        k = k * 2 + 1
    ret = k
    return ret

def print_snappers(snappers):
    for snapper in snappers:
        w = "0"
        if snapper:
            w = "1"
        print w,
    print ""

def snapper_chain_simu(nr_snapper, nr_time):
    snappers = list()
    is_on = "ON"
    for i in range(0, nr_snapper):
        snappers.append(False)
    for i in range(0, nr_time):
        connected = True
        if debug:
            print "%3d: " % i,
            print_snappers(snappers)
        for j in range(0, len(snappers)):
            if not connected:
                break
            if not snappers[j]:
                connected = False
            snappers[j] = not snappers[j]
    for snapper in snappers:
        if not snapper:
            is_on = "OFF"
    if debug:
        print_snappers(snappers)
    return is_on


def snapper_chain(nr_snapper, nr_time):
    is_on = "OFF"
    if debug:
        print "NR_snapper=%d, nr_time=%d" % (nr_snapper, nr_time)
    if nr_snapper > nr_time:
        return is_on
    nr_need = get_nr_need(nr_snapper)
    nr_rest = nr_time - nr_need
    if debug:
        print "NR_need=%d, NR-rest=%d" % (nr_need, nr_rest)
    if nr_rest == 0:
        is_on = "ON"
    elif nr_rest > 0 and nr_rest % (nr_need + 1) == 0:
        is_on = "ON"
    return is_on

def generate_nk():
    N = random.randint(1, 30)
    K = random.randint(10 ** 6, 10 ** 8)
    return N, K

if __name__ == "__main__":
    print "Hello World"
    fname = "A-small.in"
    outf = fname + ".out"
    with open(fname, 'r') as fp:
        line = fp.readline()
        nr_case = int(line)
        #nr_case = 10000
        case = 1
        with open(outf, 'w') as out_fp:
            for i in xrange(0, nr_case):
                N, K = fp.readline().split()
                #N, K = generate_nk()
                is_on = snapper_chain(int(N), int(K))
                outline = "Case #%d: %s\n" % (case, is_on)
                out_fp.write(outline)
                #print outline,
                case += 1
    print "Finished"




