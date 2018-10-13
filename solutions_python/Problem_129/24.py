import sys

mod = 1000002013

casen = int(sys.stdin.readline())
for casei in range(casen):
    line = sys.stdin.readline().split()
    n = int(line[0])
    m = int(line[1])
    add = []
    remove = []
    original = 0
    for i in range(m):
        line = sys.stdin.readline().split()
        s = int(line[0])
        t = int(line[1])
        p = int(line[2])
        add.append((s, p))
        remove.append((t, p))
        l = t - s
        amt = p * (n * l - l * (l - 1) // 2)
        original += amt
        sys.stderr.write(str(amt) + '\n')
    add.sort()
    remove.sort()
    
    sys.stderr.write('original = ' + str(original) + '\n')
    
    tickets = []
    saved = 0
    i = 0
    j = 0
    while i < m or j < m:
        cur = n
        if i < m:
            cur = min(cur, add[i][0])
        if j < m:
            cur = min(cur, remove[j][0])
        while i in range(len(add)) and add[i][0] == cur:
            tickets.append(add[i])
            i += 1
        while j in range(len(remove)) and remove[j][0] == cur:
            while remove[j][1] != 0:
                amt = min(remove[j][1], tickets[-1][1])
                remove[j] = (remove[j][0], remove[j][1] - amt)
                tickets[-1] = (tickets[-1][0], tickets[-1][1] - amt)
                l = cur - tickets[-1][0]
                saved += amt * (n * l - l * (l - 1) // 2)
                if tickets[-1][1] == 0:
                    tickets.pop()
            j += 1
    sys.stderr.write('saved = ' + str(saved) + '\n')
    sys.stdout.write('Case #' + str(casei + 1) + ': ' + str((original - saved) % 1000002013) + '\n')