with open("/Users/dwang/Downloads/A-large.in") as f:
    with open("/Users/dwang/Downloads/out.txt", "w") as out:
        count = -1
        for line in f:
            count += 1
            if count == 0:
                T = int(line)
                continue
            print line

            items = line.strip().split(' ')
            if len(items) != 2:
                continue

            k = int(items[1])
            v = [c for c in items[0]]
            ans = 0
            for i in range(len(v)):
                if v[i] == '-':
                    if i + k <= len(v):
                        ans += 1
                        for j in range(k):
                            if v[i+j] == '-':
                                v[i+j] = '+'
                            else:
                                v[i+j] = '-'
            success = True
            for i in range(len(v)):
                success = success and (v[i] == '+')
            if success:
                out.write("Case #%d: %d\n" % (count, ans))
            else:
                out.write("Case #%d: IMPOSSIBLE\n" % count)
