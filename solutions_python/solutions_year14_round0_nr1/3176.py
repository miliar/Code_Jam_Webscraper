f = open("1a.txt")

def chunks(xs, size):
    for i in xrange(0, len(xs), size):
        yield xs[i:i+size]

def parse_game(lines):
    board = map(lambda line: line.strip().split(" "), lines[1:])
    return (int(lines[0]), board)

def solve_game(arg):
    i, lines = arg
    [(r1, g1), (r2, g2)] = map(parse_game, chunks(lines, 5))
    results = filter(lambda num: num in g1[r1-1], g2[r2-1])
    result = str(results[0]) if len(results) > 0 else ""
    option = 2 if len(results) > 1 else len(results)
    output = ["Volunteer cheated!", result, "Bad magician!"][option]
    return "Case #%d: %s" % (i+1, output)

lines = f.readlines()
print "\n".join(map(solve_game, enumerate(chunks(lines[1:], 10))))
