__author__ = 'alex'


T = input()

for tests in range(0, int(T)):
    l, s = input().split()

    standing = 0
    added = 0
    i = 0
    while i < len(s):
        num = int(s[i])
        if i == 0 or not standing < i:
            standing += num
            i += 1
        else:
            added += 1
            standing += 1

    print('Case #'+str(tests+1)+': '+str(added))
