def solve(s, k):
    # caso base
    
    if len(s) < k:
        return 0 if all([i == '+' for i in s]) else -1
    if len(s) == k:
        return 0 if all([i == '+' for i in s]) else 1 if all([i == '-' for i in s]) else -1

    # caso ricorsivo
    
    i = 1
    start = s[0]
    while i < k and s[i] == s[0]:
        i += 1
    if start == '-':
        list_s = list(s)
        for j in range(k):
            list_s[j] = "+" if s[j] == '-' else "-"
        s = "".join(list_s)
    rec_call = solve(s[i:], k)
    if rec_call == -1:
        return -1
    is_pos = 0 if start == '+' else 1
    return is_pos + rec_call


T  = int(input().strip())
for i in range(T):
    st, k = [z for z in input().strip().split(" ")]
    k = int(k)
    sol = solve(st, k)
    if sol != -1:
        print("Case #" + str(i + 1) + ":", sol)
    else:
        print("Case #" + str(i + 1) + ": IMPOSSIBLE")
