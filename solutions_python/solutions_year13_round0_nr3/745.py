from sys import stdin
import itertools as it
import heapq

# merge from: http://wordaligned.org/articles/merging-sorted-streams-in-python
def merge(subsequences):
    # prepare a priority queue whose items are pairs of the form
    # (current-value, iterator), one each per (non-empty) subsequence
    heap = [  ]
    for subseq in subsequences:
        iterator = iter(subseq)
        for current_value in iterator:
            # subseq is not empty, therefore add this subseq's pair
            # (current-value, iterator) to the list
            heap.append((current_value, iterator))
            break
    # make the priority queue into a heap
    heapq.heapify(heap)
    while heap:
        # get and yield lowest current value (and corresponding iterator)
        current_value, iterator = heap[0]
        yield current_value
        for current_value in iterator:
            # subseq is not finished, therefore add this subseq's pair
            # (current-value, iterator) back into the priority queue
            heapq.heapreplace(heap, (current_value, iterator))
            break
        else:
            # subseq has been exhausted, therefore remove it from the queue
            heapq.heappop(heap)

def first(n, it):
    "First n elements of iterator it"
    if n <= 0: return
    for elmt in it:
        yield elmt
        n -= 1
        if n <= 0: break

def mirror(s, evenly):
    "Mirror string"
    if evenly: return int(s + s[::-1])
    else: return int(s[:-1] + s[::-1])

def pals(d):
    "Generate palindromes with length d"
    if d % 2 == 0: half_d = d/2
    else: half_d = (d+1) / 2

    for n in xrange(10 ** (half_d - 1), 10 ** (half_d)):
        s = str(n)
        yield mirror(s, not d%2)

def low_pals(d):
    "Generate 0-1-2 palindromes with length d"
    if d == 1:
        yield 0; yield 1; yield 2; yield 3; return
        
    if d % 2 == 0: half_d = d/2
    else: half_d = (d+1) / 2

    s = '1' + '0' * (half_d - 1)
    while True:
        yield mirror(s, not d%2)
        next = s
        up(t)

    for n in xrange(10 ** (half_d - 1), 10 ** (half_d)):
        s = str(n)
        if d % 2 == 0: yield int(s + s[::-1])
        else: yield int(s[:-1] + s[::-1])

def onify(digits, tup):
    s = ['0']*digits
    for i in tup:
        s[-i-1] = '1'
    return ''.join(s)

def cheap_pals(d):
    "Generate 0-1-2 palindromes with 'digit cost' < 10"
    if d < 1: return
    if d == 1: yield 0; yield 1; yield 2; yield 3; return

    even = (d%2 == 0)
    if d % 2 == 0: half_d = d/2
    else: half_d = (d-1) / 2

    # Stage 1: start with a 1
    strings = merge(
        [
            (onify(half_d - 1, p) for p in it.combinations(range(half_d-1), n))
            for n in xrange(4)
        ]
    )
    for s in strings:
        if even:
            yield mirror('1' + s, even)
        else:
            yield mirror('1' + s + '0', even)
            yield mirror('1' + s + '1', even)
            if s.count('1') < 3: yield mirror('1' + s + '2', even)

    # Stage 2: start with a 2
    
    yield mirror('2' + '0' * ((d-1)/2), even)
    if not even: yield mirror('2' + '0' * ((d-3) / 2) + '1', even)

from math import floor, sqrt

def all_pals(lower, upper):
    low_d = len(str(int(sqrt(lower))))
    high_d = len(str(int(sqrt(upper))))
    for d in xrange(low_d, high_d + 1):
        for val in cheap_pals(d):
            if lower <= val*val and upper >= val*val:
                yield val

def is_pal(n):
    s = str(n)
    return s == s[::-1]

def check(it):
    for n in it:
        if is_pal(n) and is_pal(n*n):
            yield n

def run_range(bot, top):
    count = 0
    for val in check(all_pals(bot, top)):
        count += 1
    return count

if __name__ == '__main__':
    cases = int(stdin.readline().strip())
    for case in xrange(1, cases +1):
        [low, high] = [int(s) for s in stdin.readline().strip().split()]
        val = run_range(low, high)
        print "Case #%d: %d" % (case, val)
