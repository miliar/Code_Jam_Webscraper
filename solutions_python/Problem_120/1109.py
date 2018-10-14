'''
Problem solution
----------------

The area of the k-th black ring is:

    pi * (2r + 4k - 3)

If we now sum all the area of N rings (from k=1):

    pi * (2r + 1)
    pi * (2r + 5)
    pi * (2r + 9)
    ...
    ...

we get:

    N * pi * 2r + pi * (2N^2 - N) =
  = pi * (2Nr + 2N^2 - N) =
  = pi * (2N^2 + (2r - 1)N)

We now equal this to pi * t, which is the maximum area
we can cover with paint:

    pi * (2N^2 + (2r - 1)N) = pi * t
    2N^2 + (2r - 1)N - t = 0

Applying the quadratic formula we finally get:

         1 - 2r + sqrt(4r^2 - 4r + 1 + 8t)
    N = -----------------------------------
                         4

We take the floor of N and we are done.
'''


def number_of_rings(r, t):
    '''Returns the maximum number of complete rings one can draw,
    starting with a central circle of radius `r` and `t` milliliters
    of black paint.'''
    return int((1 - 2 * r + (4 * r ** 2 - 4 * r + 1 + 8 * t) ** .5) / 4)


if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'w') as out:
        total = int(sys.stdin.readline())
        for i in range(1, total + 1):
            r, t = map(int, sys.stdin.readline().split())
            out.write('Case #{0}: {1}\n'.format(i, number_of_rings(r, t)))
