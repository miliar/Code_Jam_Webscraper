

def isNonDecresing(n):
    current = -1
    for c in str(n):
        candidate = int(c)
        if candidate < current:
            return False
        current = candidate
    return True

# print( isNonDecresing( 8 ) )
# print( isNonDecresing( 139 ) )
# print( isNonDecresing( 111111111111111110 ) )
# print( isNonDecresing( 9999999999999 ) )
# print( isNonDecresing( 123456789 ) )
# print( isNonDecresing( 12345342566 ) )

def maxLeftNum(n):
    pos = -1
    maximum = -1
    for idx, c in enumerate( str(n) ):
        candidate = int(c)
        if candidate > maximum:
            pos = idx
            maximum = candidate
        elif candidate < maximum:
            break
    return [pos, maximum]

# print( maxLeftNum( 111111111111111110 ) )
# print( maxLeftNum( 9999999999999 ) )
# print( maxLeftNum( 123456789 ) )
# print( maxLeftNum( 12345342566 ) )
# print( maxLeftNum( 9876548210 ) )
# print( maxLeftNum( 12345678987654321 ) )


def solve(n):
    n_str = str(n)
    n_len = len(n_str)

    if isNonDecresing(n):
        return n

    m = maxLeftNum(n)

    if m[0] == 0 and m[1] <= 1:
        return '9' * (n_len-1)

    numCharList = []

    for idx, c in enumerate(n_str):
        if idx == m[0]:
            numCharList.append( str( int(c)-1 ) )
        elif idx > m[0]:
            numCharList.append( str(9) )
        else:
            numCharList.append(c)

    return ''.join(numCharList)

# print( solve( 132 ) )
# print( solve( 1000 ) )
# print( solve( 7 ) )
# print( solve( 111111111111111110 ) )
# print( solve( 9876548210 ) )
# print( solve( 12345678987654321 ) )
# print( solve( 608 ) )


t = int( input() )

for casenum in range(1, t+1) :

    n = int( input() )

    result = solve(n)

    # if not isNonDecresing(result):
    #     print(n)

    print( 'Case #{}: {}'.format( casenum, result ) )
