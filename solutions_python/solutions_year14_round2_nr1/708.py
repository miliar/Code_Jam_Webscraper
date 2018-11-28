__author__ = 'Shailesh'

with open("../files/A-small-attempt1.in", 'r') as inp, open("../files/outputA.txt", 'w') as out:
    t = int(inp.readline())
    for i in xrange(t):
        string = "Case #" + str(i+1) + ": "
        n = int(inp.readline())
        lines = []

        for j in xrange(n):
            lines.append(inp.readline().strip())

        first = lines[0]
        order = [first[0]]
        for l in xrange(1, len(first)):
            ch = first[l]
            if ch == order[-1]:
                continue
            order.append(ch)

        error = False
        for l in xrange(1, len(lines)):
            line = lines[l]
            index = 0
            for ch in line:
                if index < len(order) and ch == order[index]:
                    index += 1
                elif ch != order[index-1]:
                    error = True
                    break

            if error or index != len(order):
                error = True
                break
        if error:
            out.write(string + "Fegla Won\n")
            continue

        counts = [[0]*n for i in xrange(len(order))]
        for l in xrange(len(lines)):
            line = lines[l]
            index = 1
            counter = 1
            for ch in line[1:]:
                if index < len(order) and ch == order[index]:
                    counts[index-1][l] = counter
                    index += 1
                    counter = 1
                else:
                    counter += 1
            counts[index-1][l] = counter
        answer = 0
        for count in counts:
            val = int(round(sum(count)*1.0/n))
            for num in count:
                answer += abs(num - val)

        out.write(string + str(answer) + "\n")


