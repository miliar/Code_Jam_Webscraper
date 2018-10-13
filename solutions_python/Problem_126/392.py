# GOOGLE CODE JAM 2013 ROUND 1C
# PROBLEM A
import sys

def get_num_consec_consonants(s):
    best = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    stager = 0
    for letter in s:
        if letter not in vowels:
            stager += 1
        else:
            if stager > best:
                print best, letter
                best = stager
            stager = 0
        if stager > best: best = stager
    return best
    

def get_answer(s, n):
    result = 0
    for i in range(len(s)):
        sub = s[i:]
        j = len(sub)
        while j > 0:
            if get_num_consec_consonants(sub[:j]) >= n:
                #print sub[:j]
                result += 1
            j -= 1
    return result
            
def solve():
    t = int(raw_input())
    for x in range(t):
        s, n = raw_input().split()
        print 'Case #%d: %d' % (x + 1, get_answer(s, int(n)))

if __name__ == "__main__":
    solve()
    sys.exit(0)
    

                                
        
