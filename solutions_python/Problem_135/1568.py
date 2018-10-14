import sys

def main():
    T = int(sys.stdin.readline())
    for prob in range(T):
        A1 = int(sys.stdin.readline())
        rows1 = [sys.stdin.readline() for r in range(4)]
        vals1 = [[int(i) for i in l.split()] for l in rows1]
        row1 = vals1[A1 - 1]
        A2 = int(sys.stdin.readline())
        rows2 = [sys.stdin.readline() for r in range(4)]
        vals2 = [[int(i) for i in l.split()] for l in rows2]
        row2 = vals2[A2 - 1]
        result = set(row1).intersection(set(row2))
        print "Case #%d:" % (prob + 1),
        lr = len(result)
        if lr == 1:
            print result.pop()
        elif lr == 0:
            print "Volunteer cheated!"
        else:
            print "Bad magician!"

main()
