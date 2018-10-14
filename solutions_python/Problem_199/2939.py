def count_flip_time(faces, k):
    count = 0
    for idx in range(len(faces)):
        face = faces[idx]
        if face == "+":
            continue
        # can not flip anymore
        if idx + k > len(faces):
            return -1

        # flip K pancakes starting from the first blank one
        count += 1
        for j in range(idx, idx + k):
            faces[j] = "+" if faces[j] == "-" else "-"
    return count


def main():
    """The main driver"""
    n_tests = int(input())
    for i in range(n_tests):
        inp = input().split()
        faces = list(inp[0])
        k = int(inp[1])
        times = count_flip_time(faces, k)
        output = str(times) if times >= 0 else "IMPOSSIBLE"
        print("Case #{}: {}".format(i + 1, output))


if __name__ == "__main__":
    main()
