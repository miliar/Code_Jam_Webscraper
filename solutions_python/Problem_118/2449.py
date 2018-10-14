from math import sqrt

with open("C-small-attempt0.in") as f:
    n = int(f.readline().rstrip())
    for (c, line) in enumerate(f):
        interval = line.rstrip()
        (a,b) = tuple(map(int, interval.split(' ')))
        results = [0]*(b + 1 - a)
        # 1: fair, 2: square, 4: fair&square
        
        def isPalindrome(n):
            s = str(n)
            l = len(s)
            z = int(l/2)
            for i in range(z):
                if s[i] != s[l-i-1]:
                    return False
            return True

        counter = 0
        for i in range(a, b + 1):
            root = int(sqrt(i))
            if root * root == i:
                results[i-a] |= 2
                #print("%i is square" % i)
            if isPalindrome(i):
                results[i-a] |= 1
                #print("%i is fair" % i)
            if root < a:
                if isPalindrome(root):
                    results[i-a] |= 4
            elif (results[root - a] & 1) == 1:
                #print("root %i of %i is fair" % (root, i))
                results[i-a] |= 4
            if results[i-a] & 7 == 7:
                #print("%i is fair & square" % i)
                counter = counter + 1
        print("Case #%i: %i" % (c + 1, counter))


