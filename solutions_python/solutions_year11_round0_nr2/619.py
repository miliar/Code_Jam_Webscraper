import csv
import os
import sys

def solve(d_combine, d_opposed, invoke):
    elements = []
    to_oppose = {}

    for e in invoke:
        while True:
            combined = elements \
                and d_combine.get((e, elements[-1])) \
                or None

            if combined:
                _ = elements.pop()
                e = combined

                oppose = d_opposed.get(_)
                if oppose and oppose in to_oppose:
                    to_oppose[oppose] += -1
                    if to_oppose[oppose] == 0:
                        del to_oppose[oppose]

            elif e in to_oppose:
                elements = []
                to_oppose = {}
                break

            else:
                elements.append(e)

                oppose = d_opposed.get(e)
                if oppose:
                    to_oppose.setdefault(oppose, 0)
                    to_oppose[oppose] += 1
                break

    return elements

def read_line(r):
    columns = iter(r)

    d_combine = {}
    C = int(columns.next())
    for i in range(C):
        a,b,c = columns.next()
        d_combine[(a, b)] = c
        d_combine[(b, a)] = c

    d_opposed = {}
    D = int(columns.next())
    for i in range(D):
        a,b = columns.next()
        d_opposed[a] = b
        d_opposed[b] = a

    N = int(columns.next())
    invoke = columns.next()

    assert N == len(invoke)
    try:
        columns.next()
        print "error in reading input file"
        raise SystemExit
    except StopIteration:
        pass

    return d_combine, d_opposed, invoke

def main(src, dst):
    reader = csv.reader(src, delimiter=" ")

    T = int(reader.next()[0])

    for t in range(T):
        r = reader.next()

        d_combine, d_opposed, invoke = read_line(r)

        elements = solve(d_combine, d_opposed, invoke)
        answer = '[' + ', '.join(elements) + ']'
        
        dst.write("Case #%d: %s\n" % (t + 1, answer))

    assert src.read() == ""

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: python solve.py input output"
        raise SystemExit

    src_path = os.path.abspath(sys.argv[1])
    src = open(src_path, "r")

    
    dst_path = os.path.abspath(sys.argv[2])
    if os.path.exists(dst_path):
        print "already exists: %s" % dst_path
        raise SystemExit
    dst = open(dst_path, "w")

    try:
        main(src, dst)
    finally:
        src.close()
        dst.close()
