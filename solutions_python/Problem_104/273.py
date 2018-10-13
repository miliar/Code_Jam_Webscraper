subsets = {}

def equal(l):
    def calculate_sum(subset):
        s = 0
        for i in xrange(len(l)):
            s += subset[i] * l[i]
        return s
    def helper(i, subset):
        if i == len(l):
            return None
        subset[i] = 1
        s = calculate_sum(subset)
        if s in subsets and subsets[s] != subset:
            return subsets[s], subset
        else:
            subsets[s] = list(subset)
            res = helper(i+1, subset)
            if res:
                return res
            subset[i] = 0
            res = helper(i+1, subset)
            if res:
                return res
    subsets = {}
    res = helper(0, [0 for x in l])
    real_res = ([], [])
    for i in xrange(len(res[0])):
        if res[0][i] == 1:
            real_res[0].append(l[i])
    for i in xrange(len(res[1])):
        if res[1][i] == 1:
            real_res[1].append(l[i])
    return real_res

if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        ns = map(int, raw_input().split(' '))
        print "Case #%d:" % (i+1)
        res = equal(ns[1:])
        if res:
            (a, b) = res
            print ' '.join(map(str, a))
            print ' '.join(map(str, b))
        else:
            print 'Impossible'

