import math

T = raw_input()
T = int(T)
cases = []

def is_palindrome(x):
    x = str(x)
    if len(x) == 1:
        return True
    if len(x) == 2:
        if x[0] != x[1]:
            return False
        else:
            return True
    for index in range((len(x) / 2), 0, -1):
        if x[index - 1] != x[-index]:
            return False

    return True

for i in range(T):
    A_AND_B = raw_input()
    A, B = A_AND_B.split(' ')
    cases.append((A, B))

m = 1
for case in cases:
    lower_bound = case[0]
    higher_bound = case[1]

    how_many = 0
    for i in range(int(lower_bound), int(higher_bound)+1):
        if is_palindrome(i):
            square_root = math.sqrt(i)
            if square_root % 1 == 0:
                if is_palindrome(int(math.sqrt(i))):
                    how_many += 1

    print 'Case #%d: %d' % (m, how_many)
    m = m + 1

