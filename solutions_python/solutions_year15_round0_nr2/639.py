from collections import deque
import math

def solve_slow(diners, log=False):
    found = set()
    frontier = deque([(0, sorted(diners), [])])
    while True:
        minutes, diners, path = frontier.popleft()
        #print minutes, diners
        if sum(diners) == 0:
            if log:
                for stage in path:
                    print stage
            return minutes
        candidate = (minutes + 1, sorted([diner - 1 for diner in diners if diner > 0]))
        new_path = path + [candidate + ("normal",)]
        if str(candidate) not in found:
            found.add(str(candidate))
            frontier.append(candidate + (new_path,))
        for index, diner in enumerate(diners):
            for amount in xrange(1, diner):
                new_diners = diners[:]
                new_diners[index] -= amount
                new_diners += [amount]
                candidate = (minutes + 1, sorted(new_diners))
                new_path = path + [candidate + ("moved %s of %s" % (amount, diners[index]),)]
                if str(candidate) not in found:
                    found.add(str(candidate))
                    frontier.append(candidate + (new_path,))


# Code for large input:

def redistribute(diners, target):
    minutes = 0
    for diner in diners:
        minutes += (diner - 1) / target
    return target + minutes

def solve_fast(diners):
    best = max(diners) + 1
    for target in xrange(1, max(diners) + 1):
        score = redistribute(diners, target)
        if score < best:
            best = score
    return best

if __name__ == "__main__":
    count = int(raw_input())
    for case in xrange(1, count + 1):
        diner_count = int(raw_input())
        diners = [int(diner) for diner in raw_input().split(" ")]
        print "Case #%s: %s" % (case, solve_fast(diners))

