import sys

vowels = set(['a', 'e', 'i', 'o', 'u'])
cons   = set([chr(i) for i in range(ord('a'), ord('z') + 1)]) - vowels

def check_consec_cons(substr, n):
    consec_cons = 0
    for c in substr:
        consec_cons = consec_cons + 1 if not c in vowels else 0
        if consec_cons >= n:
            return True
    return False

def run_case(it):
    tok = it.next().split()
    name = tok[0]
    n = int(tok[1])
    m = {}
    return solve_sub_prob([name, n], [0, len(name)], m)
    
def solve_sub_prob(p, r, m):
    tr = tuple(r)
    nval = 0
    if not tr in m:
        for i in range(*r):
            for j in range(i + 1, r[1] + 1):
                if (check_consec_cons(p[0][i:j], p[1])):
                    nval += 1
                # print(p[0][i:j] + " " + str((i,j)))
        #m[tr] = 0
    return nval #m[tr]

def main(*args):
    lines = [line.strip() for line in sys.stdin]
    it = iter(lines)
    num_cases = int(it.next())
    for case_no in range(num_cases):
        try:
            output = run_case(it)
            if type(output) == list or type(output) == tuple :
                output = ' '.join(output)
            print("Case #%d: %s" % (case_no + 1, output))
        except StopIteration, e:
            print("Error: Input exhausted.")

if __name__ == '__main__':
    main(*sys.argv[1:])