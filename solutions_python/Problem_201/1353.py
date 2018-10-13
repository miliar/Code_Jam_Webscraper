import math


def process():
    t = int(input())
    for i in range(1, t + 1):
        n, k = [int(i) for i in input().split(" ")]
        l, r = last_stall_values(n, k)
        print("Case #{}: {} {}".format(i, l, r))


def last_stall_values(n_stalls, k_people):
    while k_people > 1:
        rem = 0 if k_people % 2 == 0 else 1
        n_stalls = (n_stalls - rem)//2
        k_people //= 2

    return math.ceil((n_stalls-1)/2), (n_stalls-1)//2

if __name__ == "__main__":
    process()