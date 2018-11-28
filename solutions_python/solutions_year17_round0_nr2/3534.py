def main():
    T = int(input())
    outputs = []
    for t in range(1, T+1):
        n = input()
        yes = False
        for a, b in zip(n, n[1:]):
            if a > b:
                yes = True
        if yes:
            end = 0
            for i in range(len(n)-1):
                if n[i] < n[i+1]:
                    end = i+1
                elif n[i] > n[i+1]:
                    break
            trail = len(n) - end - 1
            out = int(n[:end] + str(int(n[end])-1) + "9"*(trail) if trail else n)
        else:
            out = n

        outputs.append("Case #%d: %s" % (t, out))
    print("\n".join(outputs))


if __name__ == '__main__':
    main()
