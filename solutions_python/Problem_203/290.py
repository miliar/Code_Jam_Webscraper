def show(i, val):
    print "Case #%s:" % i
    for row in val:
        print "".join(row)


def sol(cake, r, c):
    is_empty = lambda x: all(map(lambda y: y == "?", x))
    
    for i, row in enumerate(cake):
        if not is_empty(row):
            break

    j = 0
    while j < i:
        cake[j] = cake[i]
        j += 1



    for i in xrange(r):
        if is_empty(cake[i]):
            cake[i] = cake[i - 1]
            continue

        j = 0
        while j < c and cake[i][j] == "?":
            j += 1
                
        for k in xrange(j):
            cake[i][k] = cake[i][j]

        prev = cake[i][j]
        for k in xrange(j + 1, c):
            if cake[i][k] == "?":
                cake[i][k] = prev
            else:
                prev = cake[i][k]

    return cake


if __name__ == "__main__":
    T = int(raw_input().strip())

    for i in xrange(1, T + 1):
        r, c = map(int, raw_input().strip().split())
        cake = []
        for _ in xrange(r):
            cake.append(list(raw_input().strip()))
        show(i, sol(cake, r, c))

