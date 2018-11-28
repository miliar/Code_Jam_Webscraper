from math import sqrt, trunc

def palindrome(a):
    s = str(a)

    # Check if integer (some sqrt are not)
    float = s.split(".")
    if (len(float) == 2):
        if float[1] != '0':
            return False
        else:
            s = float[0]

    for i in range(0, len(s)/2):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True

def process_case(case, a, b):
    n = 0
    for i in range(a, b+1):
        if (palindrome(i) and palindrome(sqrt(i))):
            n = n + 1
    print "Case #"+ str(case) +": " + str(n)

with open("C-small-attempt0.in") as f:
    content = f.readlines()

for i in range(0, int(content[0].rstrip())):
    l = content[i+1].rstrip().split()
    process_case(i+1, int(l[0]), int(l[1]))
