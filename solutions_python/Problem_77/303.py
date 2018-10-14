import sys, os
import random
from itertools import permutations

def stats(list):
    in_place = in_pairs = in_disorder = 0
    for i in range(len(list)):
        if i == list[i]:
            in_place += 1 
        elif i == list[list[i]]:
            in_pairs += 1
        else:
            in_disorder += 1
    return (in_place, in_pairs, in_disorder)
    
class GoroSort(object):
    
    def __init__(self, list):
        self.zero_indexed = [val - 1 for val in list]
        self.in_place, self.in_pairs, self.in_disorder = stats(self.zero_indexed)
        
    def __str__(self):
        return "list: %s\nin place: %s, in pairs: %s, in disorder: %s" % \
            (self.zero_indexed, self.in_place, self.in_pairs, self.in_disorder)

    def count(self):
        return float(len(self.zero_indexed) - self.in_place)
                     
def solve(filename):
    fname = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(fname) as data:
        first = True
        case = 1
        count = 0
        for line in data:
            if first:
                games = int(line)
                first = False
            else:
                count += 1
                if count % 2: continue
                list = [int(i) for i in line.split(" ")]
                goro = GoroSort(list)
                print "Case #%s: %.6f" % (case, goro.count())
                case += 1
                        
if __name__ == "__main__":
    solve("D-large.in")
    
""" 

Code I used to realize how easy this was.

def sub_solve(count):
    # solves a problem of size count, by breaking it up into probabilities
    # writing and running this problem yields sub_solve(n) = n.
    # sigh, at least i learned something.
    
    if count == 0:
        return float(0)
    perms = permutations(range(count))
    total_tries = float(0)
    total_recursions = float(0)
    total_cases_handled = float(0)
    total_cases = float(0)
    for p in perms:
        total_cases += 1
        in_place, in_pairs, in_disorder = stats(p)
        if in_disorder == 0:
            # solved!
            # either broken down into pairs or done
            total_tries += 1
            total_tries += float(in_pairs) # conventiently each pair adds 2 tries
            total_cases_handled += 1
        elif in_place or in_pairs:
            total_tries += 1
            total_tries += float(in_pairs)
            total_tries += sub_solve(count - in_pairs - in_place)
            total_cases_handled += 1
        else:
            # this is the recursive case
            total_recursions += 1
    # now we have an equation
    # x = (handled/total)(total_tries/handled) + (recursive/total)(1 + x)
    # x = (total_tries/total) + (recursive/total) + (recursive/total)(x)
    # (1 - recursive/total)x = (total_tries/total) + (recursive/total) 
    # x = [(total_tries + recursive)/total)] / (1 - recursive/total)
    val = ((total_tries + total_recursions)/total_cases) / (1 - total_recursions / total_cases)
    return val
    
    print "total tries: %s, handled: %s, outstanding: %s, value: %s" % \
        (total_tries, total_cases_handled, total_recursions, val)
    
             
def solve(filename):
    fname = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(fname) as data:
        first = True
        case = 1
        count = 0
        for line in data:
            if first:
                games = int(line)
                first = False
            else:
                count += 1
                if count % 2: continue
                list = [int(i) for i in line.split(" ")]
                goro = GoroSort(list)
                #print goro
                #print list
                print "Case #%s: %.6f" % (case, goro.count())
                case += 1
                
ONE_SIXTH = float(1) / float(6)
ONE_THIRD = float(1) / float(3)
TWO_THIRDS = float(2) / float(3)

def probability(tries):
    # solve the three number variant
    random.seed()
    def random_count():
        r = random.random()
        if r < ONE_SIXTH:
            # all three
            return float(1)
        elif r < TWO_THIRDS:
            # base case - one right boils down to two
            return float(1 + 2)
        return 1 + random_count()
    total = 0
    for i in range(tries):
        total += random_count()
        
    return float(total) / float(tries)
    
def do_tries():
    for tries in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
        print "tries: %s, value: %s" % (tries, probability(tries))
"""