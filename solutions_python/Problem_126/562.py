import sys
import unittest

def solve(name, n):
    # Find consonants positions
    vowels = "aeiou" 
    consonants = []
    for i, c in enumerate(name):
        substr = name[i : i+n]
        if len(substr) == n and all(c not in vowels for c in substr):
            consonants.append(i)
    
    #print consonants

    res = 0
    l = len(consonants)
    for i, pos in enumerate(consonants):
        posend = pos + n - 1
        right = len(name) - 1

        if i >= 1:
            left = consonants[i-1] + 1
        else:
            left = 0

        #print left, ",", right, pos, posend
        #res += 1
        A = pos - left
        B = right - posend + 1
        res += (A + 1) * B
        #print "current res = ", res, "(", A, ", ", B,")"

    return res


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(solve("tsetse", 2), 11)
        self.assertEqual(solve("quartz", 3), 4)
        self.assertEqual(solve("straight", 3), 11)
        self.assertEqual(solve("gcj", 2), 3)


if __name__ == '__main__':
    #unittest.main()

    t = int(input())
    for i, line in enumerate(sys.stdin,1):
        name, n = line.split()
        res = solve(name, int(n))
        print "Case #{}: {}".format(i, res)


