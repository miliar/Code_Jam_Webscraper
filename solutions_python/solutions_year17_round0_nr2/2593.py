with open("input.in", 'r') as f:
    with open("output.out", 'w') as g:
        T = int(f.readline())
        for r in range(T):
            n = list(f.readline().strip())
            # find first point where decreasing
            for i in range(1, len(n)):
                if int(n[i]) < int(n[i-1]):
                    break
            else:
                g.write("Case #%d: %s\n" % (r + 1, ''.join(n)))
                continue

            # find point before i where all are the same
            j = i-1
            while j > 0 and n[j-1] == n[j]:
                j -= 1

            n[j] = str(int(n[j]) - 1)
            for k in range(j+1, len(n)):
                n[k] = '9'

            if n[0] == '0':
                n = n[1:]

            g.write("Case #%d: %s\n" % (r + 1, ''.join(n)))