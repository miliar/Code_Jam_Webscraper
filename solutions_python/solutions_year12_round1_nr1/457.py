'''
Created on Apr 28, 2012
@author: moemen
pupbished under creative commons
'''



def debug(*args):
    print " ".join(str(arg) for arg in args)

def memoizing(func):
    """Function decorator to cache a function's output."""
    memos = dict()
    def memoize(*args):
        if args in memos:
            return memos[args]
        res = func(*args)
        memos[args] = res
        return res
    return memoize

def multi(list):
    res = 1
    for i in list: res *= i
    return res

def process_file(fin, fout):
    cases = int(fin.readline())
    for case in range(1, cases + 1):
        A, B = map(int, fin.readline().strip().split())
        P = map(float, fin.readline().strip().split())
        comp_pos = multi(P)
        comp_cost = comp_pos * (B - A + 1) + (1 - comp_pos) * ((B - A + 1) + B + 1)
        back_pos = []
        for i in xrange(1, A + 1):
            back_pos.append(multi(P[:-i]))
        back_cost = []
        for i, pos in enumerate(back_pos):
            suc_cost = B - A + 2 * i + 3
            f_cost = suc_cost + B + 1
            back_cost.append((pos * (suc_cost)) + ((1 - pos) * f_cost))
#            back_cost.append(back_pos[i] * (i + B - (A - i + 1) + 1) + (1 - back_pos[i]) * (i + (B - (A - i + 1) + 1) + B + 1))
            
        reenter_cost = B + 2
        debug(comp_cost, back_cost, reenter_cost)
        res = comp_cost
        for i in back_cost:
            if res > i: res = i
        if reenter_cost < res: res = reenter_cost
        fout.write("Case #%d: %.6f\n" % (case, float(res)))
    

if __name__ == '__main__':
    from sys import argv
    process_file(open(argv[1]), open(argv[1].replace("in", "out"), "w"))
