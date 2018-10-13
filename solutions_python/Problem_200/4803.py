def isSorted(s):
    for j in range(1, len(s)):
        if int(s[j]) < int(s[j - 1]):
            return False
    return True

for i in range(1, int(input()) + 1):
    y = input()
    p = len(y)
    while not isSorted(y):
        y = str(int(y) - 1)
    print("Case #%s: %s" % (i, y))
