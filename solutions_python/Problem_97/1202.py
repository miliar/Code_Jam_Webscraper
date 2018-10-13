
def cycle(num, A, B):
    digits = str(num)
    c = 0
    other = set()
    for kk in xrange(1, len(digits)):
        if digits[kk] == 0: continue
        new_num = int(digits[kk:] + digits[:kk])

        if num < new_num and new_num >= A and new_num <= B:
            other.add(new_num)
    return len(other)
    
def solve(A, B):
    s = 0
    for kk in xrange(A, B+1):
        s += cycle(kk, A, B)
    return s
    
def run(inputfile):
    junk = inputfile.readline()
    case = 1
    for line in inputfile:
        xs = line.split()
        A, B = map(int, xs)
        print "Case #%d: %d" % (case, solve(A, B))
        case += 1


if __name__ == "__main__":
    import sys
    run(open(sys.argv[1]))



    
