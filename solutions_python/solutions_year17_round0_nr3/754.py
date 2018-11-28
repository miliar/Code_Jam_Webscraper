#!/usr/bin/env python3

def main():
    #"The first line of the input gives the number of test cases, T."
    t = int(input())
    for i in range(t):
        "Each line describes a test case with two integers N and K, as described above."
        n, k = map(int, input().split())
        
        "For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is max(LS, RS), and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S."
        y, z = solve(n, k)
        print("Case #%d: %s %s" % (i+1, y, z))


from collections import Counter
def solve(n, k):
    #Multiset of chains of empty stalls.
    empties = Counter([n])
    while k > 0:
        # Get longest chain of empty stalls.
        best = max(empties.keys())
        count = empties[best]
        ls = (best - 1) // 2
        rs = (best + 0) // 2
        if count >= k: #everyone else will use this number of stalls.
            return rs, ls
        # Assign this many people at a time.
        k -= count
        # Remove this chain
        del empties[best]
        # Add back the new chains
        if ls:
            empties[ls] += count
        if rs:
            empties[rs] += count
    return rs, ls #switch order because first rv is bigger


main()
