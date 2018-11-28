def solver(s, k):
    s_len = len(s)
    if k > s_len:
        if s == "+" * s_len:
            return 0
        else:
            return "IMPOSSIBLE"

    count = 0
    s_lst = list(s)
    for sind in range(s_len - k + 1):
        if s_lst[sind] == "+":
            continue

        count += 1
        for sind2 in range(sind, sind+k):
            s_lst[sind2] = "-" if s_lst[sind2] == "+" else "+"

    if s_lst[s_len-k:] == ["+"]*k:
        return count
    return "IMPOSSIBLE"

def wrapper():
    num_tests = int(input())
    for tn in range(1, num_tests+1):
        s, ks = input().split()
        k = int(ks)
        print("Case #{}: {}".format(tn, solver(s, k)))

if __name__ == "__main__":
    wrapper()

