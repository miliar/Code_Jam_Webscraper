def answer(d, horses):
    max_time = 0
    for k, s in horses:
        max_time = max(max_time, (d - k) / s)
    return d / max_time


def main():
    t = int(input())
    for i in range(1, t + 1):
        d_str, n_str = input().split(" ")
        horses = []
        for j in range(int(n_str)):
            k_str, s_str = input().split(" ")
            horses.append((int(k_str), int(s_str)))

        result = answer(int(d_str), horses)
        print("Case #{}: {:.6f}".format(i, result))


if __name__ == "__main__":
    main()
