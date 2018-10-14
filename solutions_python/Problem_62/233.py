INPUT = {
    'wires': (('int', 'int'),'array')
}

TEST = ('''\
4
3
1 10
5 5
7 7
2
1 1
2 2
4
0 0
1 1
2 2
3 3
5
0 5
1 1
2 2
3 3
6 0
''','''\
Case #1: 2
Case #2: 0
Case #3: 0
Case #4: 7
''')

def intersect(a, b):
    return ((a[0] > b[0] and b[1] > a[1]) or (a[1] > b[1] and b[0] > a[0]))

def main(wires):
    intersects = 0
    for a in xrange(wires.length):
        for b in xrange(a):
            intersects += 1 if intersect(wires[a], wires[b]) else 0
            
            
    return intersects