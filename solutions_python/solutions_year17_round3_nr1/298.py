import sys
import numpy as np

input_file = "A-large.in"
output_file = "A-large.out"

# def calculate_surface(start_r, start_h, r, h):
#     surface = np.pi*start_r**2 + 2*np.pi*start_r*start_h
#     for i in range(1, len(h)):
#         surface += 2*np.pi*r[i]*h[i]
#     return surface


def solve(tt):
    n, k = [int(j) for j in input().split(" ")]
    r = [0]*n
    h = [0]*n
    for i in range(n):
        r[i], h[i] = [int(j) for j in input().split(" ")]
    sorted_r, sorted_h = zip(*sorted(zip(r, h), reverse=True))
    max_surface = 0
    for start_index in range(n-k+1):
        start_r = sorted_r[start_index]
        start_h = sorted_h[start_index]
        surface = np.pi * start_r ** 2 + 2 * np.pi * start_r * start_h
        if start_index+1 < len(sorted_r):
            sorted_rh = sorted([a*b for a,b in zip(sorted_r[start_index+1:],sorted_h[start_index+1:])], reverse=True)
            # sorted_r2, sorted_h2 = zip(*sorted(zip(sorted_h[start_index+1:]*sorted_r[start_index+1:], sorted_h[start_index+1:], sorted_r[start_index+1:]), reverse=True))
        for i in range(k-1):
            surface += 2*np.pi*sorted_rh[i]
        # max_surface = calculate_surface(start_r, start_h, sorted_r2[:k-1], sorted_h2[:k-1])
        if surface > max_surface:
            max_surface = surface
    return max_surface

def main():
    t = int(input())
    for tt in range(1, t + 1):
        answer = solve(tt)
        print("Case #{}: {}".format(tt, answer))


if __name__ == "__main__":
    sys.stdin = open(input_file)
    sys.stdout = open(output_file, 'w+')
    main()