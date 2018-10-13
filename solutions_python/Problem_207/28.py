def solve_ryb(r, y, b):
    if r > y+b or y > r+b or b > r+y:
        return 'IMPOSSIBLE'
    d = {'r': r, 'y': y, 'b': b}
    if r >= y and r >= b:
        big = 'r'
        if b >= y:
            mid = 'b'
            small = 'y'
        else:
            mid = 'y'
            small = 'b'
    if y >= r and y >= b:
        big = 'y'
        if b >= r:
            mid = 'b'
            small = 'r'
        else:
            mid = 'r'
            small = 'b'
    if b >= r and b >= y:
        big = 'b'
        if r >= y:
            mid = 'r'
            small = 'y'
        else:
            mid = 'y'
            small = 'r'

    ryb = '{}{}{}'.format(big, mid, small)*(d[small]-d[big]+d[mid])
    ryb = ryb + '{}{}'.format(big, mid)*(d[big]-d[small])
    ryb = ryb + '{}{}'.format(big, small)*(d[big]-d[mid])

    return ryb

def f(n, r, o, y, g, b, v):
    if o >= b and o != 0:
        if o==b and n == (o+b):
            return 'ob'*o
        return 'IMPOSSIBLE'
    if g >= r and g != 0:
        if g==r and n == (g+r):
            return 'gr'*g
        return 'IMPOSSIBLE'
    if v >= y and v != 0:
        if v==y and n == (v+y):
            return 'vy'*v
        return 'IMPOSSIBLE'
    o_chunk = 'b' + 'ob'*o
    g_chunk = 'r' + 'gr'*g
    v_chunk = 'y' + 'vy'*v
    b = b-o  # actual remaining b's is one less than this, replace with o_chunk at end
    r = r-g
    y = y-v

    ryb = solve_ryb(r, y, b)
    if ryb == 'IMPOSSIBLE':
        return ryb

    b_loc = ryb.find('b')
    if b_loc != -1:
        ryb = ryb[:b_loc] + o_chunk + ryb[b_loc+1:]

    r_loc = ryb.find('r')
    if r_loc != -1:
        ryb = ryb[:r_loc] + g_chunk + ryb[r_loc+1:]

    y_loc = ryb.find('y')
    if y_loc != -1:
        ryb = ryb[:y_loc] + v_chunk + ryb[y_loc+1:]

    return ryb



if __name__ == '__main__':

    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        cake = []
        n, r, o, y, g, b, v = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

        res = f(n, r, o, y, g, b, v)
        print "Case #{}: {}".format(i, res)
        # check out .format's specification for more formatting options