import math

def problem(case_num):
    N, K = input().split()
    N = int(N)
    K = int(K)

    cakes = []
    for o in range(N):
        R, H = input().split()
        R = float(R)
        H = float(H)

        side_surface = 2.0 * math.pi * R * H
        up_surface = 1.0 * math.pi * R * R
        # print(side_surface, up_surface)
        cakes.append((side_surface, up_surface))

    # print("--")
    cakes = sorted(cakes, key=(lambda x: x[1]),reverse = True)

    max_val = 0.0
    for i, cake in enumerate(cakes):
        stack = cakes[i+1:]
        stack = sorted(stack, key=lambda x: x[0], reverse = True)
        sum_side = sum([pair[0] for pair in stack[:K-1]])
        sum_side += cake[0]
        up_side = cake[1]
        # print(sum_side, up_side)
        max_val = max(max_val, sum_side + up_side)

    print("Case #%d: %.9f"% (case_num, max_val))


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        problem(i+1)
