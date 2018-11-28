import re

L, D, N = raw_input().split(' ')

L = int(L)
D = int(D)
N = int(N)

Dictionary = []

for k in range(0, D):
    Dictionary.append(raw_input())

Tests = []

for k in range(0, N):
    Tests.append(raw_input().replace('(', '[').replace(')', ']'))

for index, test in enumerate(Tests):
    Matches = 0
    Pattern = re.compile(test)

    for word in Dictionary:
        if re.match(Pattern, word):
            Matches += 1
    print 'Case #' + str((index + 1)) + ': ' + str(Matches)
