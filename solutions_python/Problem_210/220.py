if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        Ac, Aj = map(int, input().split())
        L = [tuple(map(int, input().split())) for _ in range(Ac + Aj)]
        ret = 0
        if Ac == 1 or Aj == 1:
            ret = 2
        else:
            L.sort()
            start_1, stop_1 = L[0]
            start_2, stop_2 = L[1]
            if stop_2 - start_1 <= 720 or (24 * 60 - start_2) + stop_1 <= 720:
                ret = 2
            else:
                ret = 4
        print("Case #{x}: {y}".format(x=t, y=ret))