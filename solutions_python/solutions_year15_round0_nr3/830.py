import random

def multiply(i, j):
    sign = 1
    while ( i.startswith('-') ):
        i = i[1:]
        sign *= -1

    while ( j.startswith('-') ):
        j = j[1:]
        sign *= -1

    table = {
        '1' : {'1': '1',  'i': 'i',  'j': 'j',  'k': 'k'   },
        'i' : {'1': 'i',  'i': '-1', 'j': 'k',  'k': '-j'  },
        'j' : {'1': 'j',  'i': '-k', 'j': '-1', 'k': 'i'   },
        'k' : {'1': 'k',  'i': 'j',  'j': '-i', 'k': '-1'  },
    }

    first = table[i][j]

    if ( sign < 0 ):
        first = first[1:] if ( first.startswith('-')) else '-' + first

    return first

def generate(l=0):
    l = l or random.randint(10, 100)

    return ''.join( [ random.choice('ijk') for x in xrange(l) ] )


def brute_force(str, search):
    if search == 'k':
        return reduce(multiply, str) == 'k'

    n = 'j' if search == 'i' else 'k'
    for x in xrange(1, len(str)):
        if ( reduce(multiply, str[:x]) == search ):
            if ( brute_force(str[x:], n ) ):
                return True
    return False

def solve_fast(lst):
    t = '1'
    i = 0
    found_i = found_j = found_k = False
    # search for an i
    while ( i < len(lst) ):
        t = multiply(t, lst[i])
        i+= 1

        if ( t == 'i' ):
            found_i = True
            break

    t = '1'
    # search for a j
    while ( i < len(lst) ):
        t = multiply(t, lst[i])
        i+= 1

        if ( t == 'j' ):
            found_j = True
            break

    t = '1'
    # the remaining should be a k
    while ( i < len(lst) ):
        t = multiply(t, lst[i])
        i+= 1

    if ( t == 'k' ):
        found_k = True

    return found_i and found_j and found_k

def solve_one ( data ):
    # for i in xrange(1000):
    #     if i % 10 == 0 : print i // 10

    #     a = generate()
    #     x = random.randint(50, 100) * 2 + 1

    #     r = reduce(multiply, a * x )

    #     if r == -1:
    #         print a, x




    l = int(data[0])
    x = int(data[1])
    s = data[2]

    # if ( l * x < 3 ):
    #     return 'NO'

    # if ( l * x == 3 and s == 'ijk'):
    #     return 'YES'

    # if ( x % 2 ):
    #     return 'NO'

    # if ( x % 4 == 0 ):
    #     return 'NO'

    return 'YES' if solve_fast(s * ( x )) else 'NO'




def solve( in_stream ):
    n = int(in_stream.readline())

    test_cases = [
        in_stream.readline().split() + [ in_stream.readline().strip() ]
        for t in xrange(n)
    ]
    s = 'Case #{0}: {1}\n'

    results = [
        s.format(i+1, solve_one(t))
        for i, t in enumerate(test_cases)
    ]

    return results


if __name__ == '__main__':
    import sys

    # read input
    in_resource = open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin
    with in_resource as in_stream:
        result = solve( in_stream )

    # write output
    out_resource = open(sys.argv[2], 'w') if len(sys.argv) > 2 else sys.stdout
    with out_resource as out_stream:
        out_resource.writelines(result)

