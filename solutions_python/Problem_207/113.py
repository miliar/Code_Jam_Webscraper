#!/usr/bin/env python
from __future__ import unicode_literals
import sys

def compute_easier(d):
    N = sum(d.values())
    m = max(d.values())
    if 2*m > N:
        return None
    repeats = min(d.values())
    s = 'RBY' * repeats
    for k in 'RBY':
        d[k] -= repeats
    remaining = sorted([v, k] for k, v in d.iteritems() if v > 0)
    if len(remaining) == 0:
        return s
    elif len(remaining) == 1:
        # don't forget to add the last too
        count, c_to_insert = remaining[0]
        # print count, c_to_insert
        sb = []
        for i, c in enumerate(s):
            prevc = s[i-1] if i >= 0 else s[-1]
            if c_to_insert != c and c_to_insert != prevc:
                sb.append(c_to_insert)
                count -= 1
            sb.append(c)
            if count == 0:
                sb.append(s[i+1:])
                return ''.join(sb)
        raise Exception("wtf")

    chars = ''.join(c for count, c in remaining)
    assert len(chars) == 2
    smaller_count = min(count for count, c in remaining)
    if chars[0] == 'Y' or chars[1] == 'R':
        chars = chars[1] + chars[0]
    s += chars*smaller_count
    count, c_to_insert = remaining[1]
    count -= smaller_count
    if count == 0:
        return s
    sb = []
    for i, c in enumerate(s):
        prevc = s[i-1] if i >= 0 else s[-1]
        if c_to_insert != c and c_to_insert != prevc:
            sb.append(c_to_insert)
            count -= 1
        sb.append(c)
        if count == 0:
            sb.append(s[i+1:])
            return ''.join(sb)
    assert False

def compute_result(r, o, y, g, b, v):
    if b > 0 and b == o:
        if r == 0 and y == 0 and g == 0 and v == 0:
            return 'BO' * b
        else:
            return None
    elif r > 0 and r == g:
        if o == 0 and y == 0 and b == 0 and v == 0:
            return 'RG' * r
        else:
            return None
    elif y > 0 and y == v:
        if r == 0 and o == 0 and g == 0 and b == 0:
            return 'YV' * y
        else:
            return None
    b -= o
    r -= g
    y -= v
    if b < 0 or r < 0 or y < 0:
        return None
    result = compute_easier({'R': r, 'B': b, 'Y': y})
    if result is None:
        return None
    assert len(result) == r + b + y
    # replace the first o B's with BOB
    sb = []
    for c in result:
        if c == 'B':
            if o > 0:
                sb.append('BO'*o + 'B')
                o = 0
            else:
                sb.append('B')
        elif c == 'R':
            if g > 0:
                sb.append('RG'*g + 'R')
                g = 0
            else:
                sb.append('R')
        elif c == 'Y':
            if v > 0:
                sb.append('YV'*v+'Y')
                v = 0
            else:
                sb.append('Y')
    return ''.join(sb)

def main(argv=sys.argv):
    infile = argv[1]
    outfile = argv[2]
    with open(infile) as f, open(outfile, 'w') as g:
        T = int(f.readline().strip())
        
        for case in xrange(1, T+1):
            N, r, o, y, G, b, v = map(int, f.readline().strip().split())
            result = compute_result(r, o, y, G, b, v)
            if result is not None:
                assert len(result) == N, [result, r, o, y, G, b, v, N, len(result)]
            if result is None:
                result = 'IMPOSSIBLE'
            g.write("Case #{}: {}\n".format(case, result))
    return 0

if __name__ == "__main__":
    status = main(argv=sys.argv)
    sys.exit(status)
