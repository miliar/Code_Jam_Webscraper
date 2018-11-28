def main():
    """
        docstring for main
    """
    exit_values = []
    N = int(raw_input())
    for case in range(1,N+1):
        matrix = []
        rang = raw_input()
        rang = rang.split()
        N = int(rang[0])
        M = int(rang[1])
        for r in range(0,N):
            row = raw_input()
            row = row.split()
            row = map(int,row)
            matrix.append(row)
        value = check(matrix, N, M)
        exit_values.append((case,value))
    for value in exit_values:
        print "Case #%d: %s" % (value[0], value[1])

def check(matrix, N, M):
    for n in range(0,N):
        for m in range(0,M):
            if all_same(matrix[n],matrix[n][m]) == False:
                if all_same([row[m] for row in matrix],matrix[n][m]) == False:
                    return "NO"
    return "YES"

def all_same(items, it):
    return all(x <= it for x in items)

if __name__ == '__main__':
    main()
