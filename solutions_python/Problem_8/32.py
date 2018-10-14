# Uses NZMath library available under BSD from
# http://tnt.math.metro-u.ac.jp/nzmath/

# Uses Pysco for performance

import sys
from nzmath.factor.methods import factor
import psyco

class DisjointSet(object):

    # Adapted from activestate recipe 387776
    def __init__(self, init=[]):
        mapping = self._mapping = {}
        for x in init:
            mapping[x] = [x]
          
    def join(self, a, *args):
        mapping = self._mapping
        set_a = mapping.setdefault(a, [a])

        for arg in args:
            set_b = mapping.get(arg)
            if set_b is None:
                set_a.append(arg)
                mapping[arg] = set_a
            elif set_b is not set_a:
                if len(set_b) > len(set_a):
                    set_a, set_b = set_b, set_a
                set_a.extend(set_b)
                for elem in set_b:
                    mapping[elem] = set_a

    def joined(self, a, b):
        mapping = self._mapping
        try:
             return mapping[a] is mapping[b]
        except KeyError:
             return False

    def __iter__(self):
        seen = set()
        for elem, group in self._mapping.iteritems():
             if elem not in seen:
                  yield group
                  seen.update(group)

def get_factor_set(factors):
    f_set = set()
    for f in factors:
        f_set.add(f[0])
    return f_set

# read the whole file specified as an argument into memory
filename = "number_sets.in"
if len(sys.argv) > 1:
    filename = sys.argv[1]
lines = [line.strip() for line in open(filename)]

# process the cases
cases = int(lines[0])
offset = 1
for case in range(1, cases + 1):

    # extract the details
    tokens = lines[offset].split(" ")
    A = int(tokens[0])
    B = int(tokens[1])
    P = int(tokens[2])

    # get the prime factors of P into a set
    P_factors = get_factor_set(factor(P))
    
    # process the range
    nums = range(A, B+1)
    groups = DisjointSet(nums)
    for num1i in range(0, len(nums)):
        for num2i in range(1+num1i, len(nums)):
             if groups.joined(nums[num1i], nums[num2i]):
                 continue
             num1_factors = factor(nums[num1i])
             num1_factor_set = get_factor_set(num1_factors)
             num2_factors = factor(nums[num2i])
             num2_factor_set = get_factor_set(num2_factors)
             common = False
             for num1_factor in num1_factors:
                 if num1_factor[0] < P:
                     continue
                 if num1_factor[0] in num2_factor_set:
                     common = True
                     break
             if not common:
                 for num2_factor in num2_factors:
                     if num2_factor[0] < P:
                          continue
                     if num2_factor[0] in num1_factor_set:
                          common = True
                          break
             if common:
                 groups.join(nums[num1i], nums[num2i])

    # output the results
    print "Case #%d: %d" % (case, len(list(groups)))

    offset = offset + 1
