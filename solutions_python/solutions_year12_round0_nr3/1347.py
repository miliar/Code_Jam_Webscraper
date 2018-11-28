def main():
    n = input()

    for case in range(1, n + 1):

        (x, y) = [int(_) for _ in raw_input().split(" ")]

        result = 0
        for i in range(x, y + 1):
            s_i = str(i)
            recycled = set()

            for j in range(1, len(s_i)):
                s_swapped = s_i[j:] + s_i[0:j]
                swapped = int(s_swapped)

                if swapped == i:
                    continue

                if len(s_swapped) == len(str(swapped)) and x <= swapped <= y:
                    recycled.add(int(s_swapped))

            result += len(recycled)

        print("Case #%s: %s" % (case, result / 2))

if __name__ == "__main__":
    main()
