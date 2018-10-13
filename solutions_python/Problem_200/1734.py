filename = input()
f = open(filename + ".in")
o = open(filename + ".out", "w")
T = int(f.readline())

for i in range(0, T):
    N = int(f.readline())
    N_str = str(N)
    if N < 10:
        print("Case #" + str(i + 1) + ": " + N_str)
        o.write("Case #" + str(i + 1) + ": " + N_str + "\n")
        continue
    N_arr = [int(N_str[j]) for j in range(0, len(N_str))]
    while True:
        flg = False
        for j in range(0, len(N_arr) - 1):
            if flg:
                N_arr[j + 1] = 0
            elif (N_arr[j] > N_arr[j + 1]):
                N_arr[j + 1] = 0
                flg = True
        if flg:
            N = int("".join(map(str, N_arr))) - 1
            N_str = str(N)
            N_arr = [int(N_str[k]) for k in range(0, len(N_str))]
        else:
            break
    print("Case #" + str(i + 1) + ": " + N_str)
    o.write("Case #" + str(i + 1) + ": " + N_str + "\n")
f.close()
o.close()
