with open("/Users/dwang/Downloads/B-large.in") as f:
    with open("/Users/dwang/Downloads/out.txt", "w") as out:
        count = -1
        for line in f:
            count += 1
            if count == 0:
                T = int(line)
                continue

            task = long(line)
            ans = 0l
            base = 1l
            while base <= task / 10:
                base = base * 10 + 1
            while base > 0:
                if ans + base <= task and ans % 10 != 9:
                    ans += base
                else:
                    base /= 10
            out.write("Case #%d: %d\n" % (count, ans))
