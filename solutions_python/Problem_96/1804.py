import fileinput

def possible_results_for_a_triplets(x):
    if x % 3 == 2:
        return (x/3+1,x/3+2)
    if x % 3 == 1:
        return (x/3+1,x/3+1)
    if x % 3 == 0 and x > 0:
        return (x/3,x/3+1)
    if x == 0:
        return (0,0)

def get_num_above_p(res,p,max_surprising):
    total = 0
    for r in res:
        pp = possible_results_for_a_triplets(r)
        if pp[0] >= p:
            total += 1
        elif pp[1] >= p and max_surprising > 0:
            max_surprising -= 1
            total += 1
    return total

def main():
    it = fileinput.input()
    numcases = int(it.next())
    for i,l in enumerate(it):
        params = [int(x) for x in l.split()]
        num_entries = params[0]
        max_surprising = params[1]
        p = params[2]
        res = params[3:]
        print "Case #%d: %d" % (i+1, get_num_above_p(res,p,max_surprising))

if __name__ == "__main__":
    main()

