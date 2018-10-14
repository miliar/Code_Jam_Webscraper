from sys import argv
from bisect import bisect_right


def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return (i, a[i])
    raise ValueError

def naomi_msg(n, klst):
    if (len(klst) == 1) or (n >= klst[-1]):
        return n

    if n > klst[0]:
        return 1

    (k1,k2) = klst[-2:]
    return k2 - ((k2 - k1) / 2.0)

def ken_choice(nmsg, klst):
    try:
        choice = find_gt(klst, nmsg)
    except:
        choice = (0, klst[0])

    klst.pop(choice[0])
    return choice[1]

def nwin_lie(n, klst):
    nm = naomi_msg(n, klst)
    kc = ken_choice(nm, klst)
    return (nm, 1) if nm > kc else (nm, 0)

def nwin_truth(n, klst):
    return 1 if n > ken_choice(n, klst) else 0

def run_test(naomi, ken):
    nlst = sorted(naomi)
    klst = sorted(ken)
    klst2 = klst[:]

    if_lie = []
    msg = []
    if_truth = []

    for n in nlst:
        # from pudb import set_trace; set_trace() 
        ll = nwin_lie(n, klst)
        tt = nwin_truth(n, klst2)
        if_lie.append(ll[1])
        if_truth.append(tt)

    return (sum(if_lie), sum(if_truth))
        

def response(n, result):
    return 'Case #{}: {} {}'.format(n+1, result[0], result[1])


if __name__ == '__main__':
    INPUT = open(argv[1] if len(argv) > 1 else "/tmp/shiner")
    lines = [x.strip() for x in INPUT.readlines()]

    num_tests = lines.pop(0)
        
    for i in xrange(0, len(lines), 3):
        (nblocks, naomi, ken) = lines[i:i+3]
        print response(i/3, run_test([float(x) for x in naomi.split(' ')],
                                   [float(x) for x in ken.split(' ')]))

