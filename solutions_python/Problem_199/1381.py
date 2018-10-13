fname = input().strip()
with open(''.join([fname, '.in']), 'r') as rfile, \
     open(''.join([fname,'.out']), 'w') as wfile:
    t = int(rfile.readline())
    d = {'+':'-', '-':'+'}
    for i in range(1, t + 1):
        row, k = rfile.readline().split()
        row = list(row)
        k = int(k)

        j, count = 0, 0
        while j <= len(row)-k:
            if row[j] == '-':
                row[j:j+k] = [d[e] for e in row[j:j+k]]
                count += 1
            j += 1
        if '-' in row: count = 'IMPOSSIBLE'
        print("Case #{}: {}".format(i, count), file=wfile)
