T = int(input())
for t in range(1,T+1):
    signed_input, flipper = input().split()
    flipper = int(flipper)
    ans_count = 0
    store = [0 for i in range(len(signed_input))]
    for i in range(len(store)):
        if signed_input[i] == '-':
            store[i] = 1
    for i in range(len(store) - flipper):
        if store[i] % 2 == 1:
            ans_count += 1
            for j in range(flipper):
                store[i+j] += 1
    exit_flag = False
    if store[-1] % 2 == 1:
        ans_count += 1
    for i in range(len(store)-flipper, len(store)):
        if store[i] % 2 != store[-1] % 2:
            exit_flag = True
            break
    if exit_flag:
        print("Case #" + str(t) + ": " + "IMPOSSIBLE")
    else:
        print("Case #" + str(t) + ": " + str(ans_count))