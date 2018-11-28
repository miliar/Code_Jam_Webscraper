import sys
import numpy as np
import itertools as it
from collections import Counter, defaultdict

def nums_line(f):
    return np.array([int(k) for k in f.readline().strip().split()])

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    filename = argv[0] if argv else 'test.in'

    with open(filename) as f:
        num_cases = int(f.readline())
        for case_no in xrange(1, num_cases+1):
            k, n = nums_line(f)
            keys = nums_line(f)
            if len(keys) != k:
                print >> sys.stderr, "Error: wrong number of starting keys."
            keys_list = keys
            keys = Counter(keys)
            chests = []
            reqs = []
            cs = []
            for i in xrange(n):
                nums = nums_line(f)
                req = nums[0]
                qty = nums[1]
                c = nums[2:]
                if qty != len(c):
                    print >> sys.stderr, "Error: wrong no. of keys in chest."
                chests.append(Chest(i+1, req, c))
                reqs.append(req)
                cs.append(c)
            #if case_no == 12:
            #    with open('a.in', 'w') as fa:
            #        print >> fa, 1
            #        print >> fa, k, n
            #        print >> fa, ' '.join([str(k) for k in keys_list])
            #        for i in xrange(n):
            #            print >> fa, reqs[i], len(cs[i]),
            #            print >> fa, ' '.join([str(k) for k in cs[i]])
            answer = solve(keys, chests)
            print "Case #{}:".format(case_no),
            if answer is not None:
                print ' '.join([str(x) for x in answer[::-1]])
            else:
                print "IMPOSSIBLE"


class Chest(object):
    def __init__(self, num, lock, keys):
        self.num = num
        self.lock = lock
        self.keys = Counter(keys)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "Chest({!r}, {!r}, {!r})".format(self.num, self.lock, dict(self.keys))

    def __cmp__(self, other):
        return cmp(self.num, other.num)

    def __eq__(self, other):
        return self.num == other.num

    def __hash__(self):
        return self.num

def solve(keys, chest_list, display=False):
    n = len(chest_list)
    openable = set()
    chests = defaultdict(set)
    num_needed = Counter()
    num_contained = Counter()
    num_othered = Counter()

    for chest in chest_list:
        chests[chest.lock].add(chest)
        num_needed[chest.lock] += 1

        for key, amount in chest.keys.iteritems():
            num_contained[key] += amount
            if chest.lock != key:
                num_othered[key] += amount

    if display:
        for k, v in chests.items():
            print >> sys.stderr, k, v

        print >> sys.stderr, ""
        print >> sys.stderr, "NEED:", num_needed
        print >> sys.stderr, "KEYS:", keys
        print >> sys.stderr, "INSI:", num_contained
        print >> sys.stderr, "OTHE:", num_othered
    
    for key in num_needed:
        if keys[key] + num_contained[key] < num_needed[key]:
            # print "Not enough of", key
            return None

    for k in keys:
        openable.update(chests[k])
    return solve2(keys, n, chests, openable, 
            num_needed, num_contained, num_othered)

def solve2(keys, n, chests, openable, 
        num_needed, num_contained, num_othered):
    if n <= 0:
        return []
    elif not openable:
        return None

    for chest in sorted(list(openable)):
        lock = chest.lock
        if keys[chest.lock] <= 0:
            print >> sys.stderr, "ERROR!!!"
            continue
        if (keys[chest.lock] == 1 and chest.lock not in chest.keys and
                num_othered[chest.lock] == 0 and
                num_needed[chest.lock] > 1):
            continue

        openable2 = openable.copy()
        keys2 = keys.copy()
        chests2 = defaultdict(set)
        num_needed2 = num_needed.copy()
        num_contained2 = num_contained.copy()
        num_othered2 = num_othered.copy()

        num_needed2[lock] -= 1
        for k, v in chest.keys.iteritems():
            num_contained2[k] -= v
            if k != lock:
                num_othered2[k] -= v


        for k, v in chests.iteritems():
            chests2[k] = v.copy()

        if keys2[lock] == 1 and lock not in chest.keys:
            openable2.difference_update(chests2[lock])
            del keys2[lock]
        else:
            keys2[lock] -= 1
            openable2.remove(chest)
        chests2[lock].remove(chest)
        for k in chest.keys:
            if k not in keys2:
                openable2.update(chests2[k])
            keys2[k] += chest.keys[k]

        answer = solve2(keys2, n-1, chests2, openable2,
                num_needed2, num_contained2, num_othered2)
        if answer is not None:
            answer.append(chest.num)
            return answer

    return None

if __name__ == '__main__':
    main()
