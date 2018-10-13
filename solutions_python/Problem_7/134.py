#!/usr/bin/python
# Google Code Jam 2008

def solve(vertexes):
    count = 0
    combos = []
    for a in vertexes:
        x = vertexes[:]
        x.remove(a)
        for b in x:
            y = x[:]
            y.remove(b)
            for c in y:
                combos.append((a, b, c))
    for combo in combos:
        ((x0, y0), (x1, y1), (x2, y2)) = combo
        mid = ((x0 + x1 + x2)/3.0, (y0 + y1 + y2)/3.0)
        if (x0 + x1  + x2) % 3 == 0 and  (y0 + y1 + y2) % 3 == 0:
            count += 1

    return  count/6 
            

def parse_test(data):
    line = 0
    [n, A, B, C, D, x0, y0, M] = [int(num) for num in data[line].split(" ")]
    line += 1
    X = x0
    Y = y0
    vertexes = [(X, Y)]

    for i in range(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        vertexes.append((X, Y))

    return (line, [vertexes]) 

def main():
    import sys
    filename = sys.argv[1]
    input = open(filename)
    data = [line.strip() for line in input.readlines()]
    num_testcases = int(data[0])
    line = 1
    for i in range(1, num_testcases+1):
        (lines, test) = parse_test(data[line:])
    #    print test
        answer = apply(solve, test)
        print "Case #%d: %d" % (i, answer)
        line = line + lines
    input.close()

if __name__ == "__main__":
    main()


