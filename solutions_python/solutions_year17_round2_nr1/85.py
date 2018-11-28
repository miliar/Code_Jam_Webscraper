import fileinput

inp = fileinput.input()

num_cases = int(inp.readline())
for t in range(1, num_cases + 1):
    D, N = (int(x) for x in inp.readline().split())
    lat_arr_time = 0
    for _ in range(N):
        K, S = (int(x) for x in inp.readline().split())

        arr_time = (D-K) / S
        if lat_arr_time < arr_time:
            lat_arr_time = arr_time

    print("Case #{}: {:.6f}".format(t, D / lat_arr_time))