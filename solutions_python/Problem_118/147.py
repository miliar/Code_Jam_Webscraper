# This script generates the actual source code.
# The actual source code is over 1MB in size, so I could not submit it.

import sys

def isPalindrome(n):
    q = str(n)
    for i in range(len(q)/2):
        if (q[i] != q[len(q)-1-i]):
            return False
    return True

l = [1, 4, 9]
v = "2"
for x in range(25):
    q = v + v[::-1]
    z = int(q) ** 2
    if isPalindrome(z):
        l.append(z)
    q = v + "0" + v[::-1]
    z = int(q) ** 2
    if isPalindrome(z):
        l.append(z)
    q = v + "1" + v[::-1]
    z = int(q) ** 2
    if isPalindrome(z):
        l.append(z)
    v = v + "0"

BIG = 1 << 25
for x in range(BIG):
    q = bin(x)[2:]
    r_a = q + q[::-1]
    r_b = q + "0" + q[::-1]
    r_c = q + "1" + q[::-1]
    r_d = q + "2" + q[::-1]
    z = int(r_a) ** 2
    if isPalindrome(z):
        l.append(z)
    z = int(r_b) ** 2
    if isPalindrome(z):
        l.append(z)
    z = int(r_c) ** 2
    if isPalindrome(z):
        l.append(z)
    z = int(r_d) ** 2
    if isPalindrome(z):
        l.append(z)
    if (x & 65535 == 0):
        sys.stderr.write(str(x) + "\n")
        
sys.stderr.write(str(len(l)) + "\n")

print("L = [")
for i in l:
    print(str(i) + ", ")
print("]")
print("n = input()")
print("for i in range(n):")
print("\ta, b = raw_input().split()")
print("\ta = int(a)")
print("\tb = int(b)")
print("\tj = 0")
print("\tfor k in L:")
print("\t\tif (a <= k) and (k <= b):")
print("\t\t\tj += 1")
print('\tprint("Case #" + str(i+1) + ": " + str(j))');


