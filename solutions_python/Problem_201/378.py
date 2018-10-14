f = open("e.in")
fout = open("e.out", "w")

input_str = f.readline()
t = int(input_str)

for case in range(1, t + 1):
    input_str = f.readline()
    splitted = input_str.split()
    n = int(splitted[0])
    k = int(splitted[1])

    mx = mn = 0

    cntr = dict({n: 1})
    while k > 0:
        next_q = max(cntr.keys())
        mn = (next_q - 1) // 2
        mx = next_q // 2

        val = cntr.pop(next_q)
        if val >= k:
            break
        k -= val
        cntr[mx] = val + cntr.get(mx, 0)
        cntr[mn] = val + cntr.get(mn, 0)
    fout.write("Case #%d: %d %d\n" % (case, mx, mn))

f.close()
fout.close()
