import math


def get_next(stalls):

    start = None
    end = None
    empty_stalls = []
    for i, s in enumerate(stalls):
        if s == 0:
            if not start:
                start = i
                end = i
            else:
                end = i
        else:
            if start and end:
                empty_stalls.append( [end-start+1, start, end] )
                start = None
                end = None

    empty_stalls.sort( key=lambda item: -item[0] )

    length, start, end = empty_stalls[0]

    result = start + (length/2) - 1

    return int( math.ceil( result ) )

assert( get_next( [1, 0, 0, 0, 0, 1] ) == 2 )
assert( get_next( [1, 0, 1, 0, 0, 1] ) == 3 )
assert( get_next( [1, 0, 0, 0, 0, 0, 1] ) == 3 )
assert( get_next( [1, 0, 0, 1, 0, 0, 1] ) == 1 )
assert( get_next( [1, 0, 0, 0, 0, 0, 0, 1] ) == 3 )
assert( get_next( [1, 0, 0, 1, 0, 0, 0, 1] ) == 5 )


def solve(n, k):

    if n == k:
        return [0, 0]

    stalls = [1] + [0] * n + [1]

    for i in range(k):

        next_pos = get_next(stalls)

        stalls[next_pos] = 1

    last_pos = next_pos

    to_left = last_pos - 1
    to_right = last_pos + 1

    l = 0
    while stalls[to_left] != 1:
        l += 1
        to_left -= 1

    r = 0
    while stalls[to_right] != 1:
        r += 1
        to_right += 1

    # print()
    # print(stalls)
    # print(n, k)
    # print(last_pos)

    return [ max( l, r ), min(l, r) ]

assert( solve( 4, 2 ) == [1, 0] )
assert( solve( 5, 2 ) == [1, 0] )
assert( solve( 6, 2 ) == [1, 1] )
assert( solve( 1000, 1000 ) == [0, 0] )
assert( solve( 1000, 1 ) == [500, 499] )


t = int( input() )

for casenum in range(1, t+1):

    n, k = input().split()
    n = int(n)
    k = int(k)

    empty_max, empty_min = solve(n, k)

    print( 'Case #{}: {} {}'.format( casenum, empty_max, empty_min ) )
