#!/usr/bin/python

import sys
from pprint import pprint
#from collections import deque
from collections import defaultdict

def solve(string):
    #pprint(bffs)

    nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    counter = defaultdict(lambda: 0)
    for c in string:
        counter[c] += 1

    ans = {}
    uniq_chars = {"Z":nums[0], "W":nums[2], "X":nums[6], "G":nums[8]}
    for u_char, num in uniq_chars.items():
        if u_char in counter:
            n = counter[u_char]
            ans[nums.index(num)] = n
            for char in num:
               counter[char] -= n

    if "H" in counter and counter["H"] > 0:
        n = counter["H"]
        ans[3] = n
        for char in nums[3]:
           counter[char] -= n

    if "R" in counter and counter["R"] > 0:
        n = counter["R"]
        ans[4] = n
        for char in nums[4]:
           counter[char] -= n
    if "O" in counter and counter["O"] > 0:
        n = counter["O"]
        ans[1] = n
        for char in nums[1]:
           counter[char] -= n
    if "F" in counter and counter["F"] > 0:
        n = counter["F"]
        ans[5] = n
        for char in nums[5]:
           counter[char] -= n
    if "S" in counter and counter["S"] > 0:
        n = counter["S"]
        ans[7] = n
        for char in nums[7]:
           counter[char] -= n
    if "I" in counter and counter["I"] > 0:
        n = counter["I"]
        ans[9] = n
        for char in nums[9]:
           counter[char] -= n

    #pprint(counter)
    ans_str = ""
    for n, c in sorted(ans.items()):
        ans_str += str(n) * c
    return ans_str

if __name__ == '__main__':

    case_N = int(sys.stdin.readline().strip())
    #pprint(case_N)
    for n in xrange(case_N):
        string = sys.stdin.readline().strip()
        ans = solve(string)
        print 'Case #' + str(n+1) + ': ' + str(ans)
