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

def write(i, s):
    fw.write("Case #" + str(i+1) + ": " + s + "\n")

def rev_cmp(a, b):
    return -cmp(a, b)
    
def main():
    setup()
    num_cases = int(fr.readline().strip())
    for i in xrange(num_cases):
        size = int(fr.readline().strip())
        v1 = [int(l) for l in fr.readline().strip().split(" ")]
        v2 = [int(l) for l in fr.readline().strip().split(" ")]

        v1.sort()
        v2.sort(rev_cmp)
        r = 0
        #print v1, v2
        for j in xrange(size):
            r = r + v1[j]*v2[j]
        #print r

        write(i, str(r))

    done()

main()
