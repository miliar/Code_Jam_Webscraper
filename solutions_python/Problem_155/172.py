import sys

in_file = open(sys.argv[1], "r")

out_file = open("output.out", "w")

t = int(in_file.readline())

for i in range(t):
    params = in_file.readline().split(' ')

    c_max = int(params[0])
    c_rest = params[1]

    ans = 0
    inte = 0
    pos = 0
    for m in c_rest.strip():
        num = int(m)
        if inte < pos:
            ans += pos - inte
            inte = pos
        inte += num
        pos += 1

    out_file.write("Case #" + str(i + 1) + ": " + str(ans))

    out_file.write("\n")

in_file.close()
out_file.close()
