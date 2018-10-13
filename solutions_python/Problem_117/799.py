import sys
import copy

class Swath():
    def __init__(self, height):
        self.height = height
        self.cut = False

def get_max(data):
    m = 0
    for i in data:
        if i.height > m:
            m = i.height
    return m

def check(data):
    h = get_max(data)
    for i in data:
        if i.height == h:
            i.cut = True

def solve(lawn, n, m):
    # check through rows
    for row in lawn:
        check(row)

    # check through columns
    for i in range(m):
        column = []
        for j in range(n):
            column.append(lawn[j][i])
        check(column)

    for row in lawn:
        for i in row:
            if i.cut == False:
                return 'NO'
    return 'YES'     

def main():
    try:
        path = sys.argv[1]
        results = []
        with open(path, 'r') as f:
            cases = int(f.readline())

            for i in range(cases):
                n, m = f.readline().split(' ')
                n, m = int(n), int(m)

                lawn = []
                row = []
                for j in range(n):
                    row = f.readline().split(' ')
                    lawn.append([Swath(int(x)) for x in row])
                results.append('Case #{0}: {1}{2}'.format(i + 1, solve(lawn, n, m), '\n' if i < cases - 1 else ''))
        with open(path + '-results', 'w') as fr:
            fr.write(''.join(results))
    except FileNotFoundError:
        print("Couldn't find file!")
    except IndexError:
        print("usage: lawnmower.py <path_to_file>")

main()
