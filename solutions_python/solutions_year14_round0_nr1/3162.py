import sys

def main():
    with open(sys.argv[1]) as f:
        num = int(f.readline())
        for i in range(num):
            mat = []
            first = int(f.readline())
            for j in range(4):
                mat.append(map(int, f.readline().split(' ')))
            second = int(f.readline())
            for j in range(4):
                mat.append(map(int, f.readline().split(' ')))
            first_line_set = set(mat[first - 1])
            second_line_set = set(mat[second + 3])
            result = first_line_set.intersection(second_line_set)
            if len(result) == 1:
                print 'Case #%d: %d' % (i + 1, result.pop())
            elif len(result) < 1:
                print 'Case #%d: Volunteer cheated!' % (i + 1)
            else:
                print 'Case #%d: Bad magician!' % (i + 1)


if __name__ == '__main__':
    main()
