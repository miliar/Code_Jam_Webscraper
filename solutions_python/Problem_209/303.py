#Problem A - round 1C
from math import pi

def main():
    t = int(input())
    case_list = []
    for i1 in range(t):
        n, k = tuple([int(i2) for i2 in input().split()])
        pancakes = []
        for i3 in range(n):
            pancakes.append(tuple([int(i3) for i3 in input().split()]))
        case_list.append((n, k, pancakes))

    for case_num in range(t):
        n, k, pancakes = case_list[case_num]
        surface_area = 0
        max_rad = 0

        for i4 in range(k):
            p_max = 0
            p_max_num = 0
            for p_num in range(len(pancakes)):
                r, h = pancakes[p_num]
                if r <= max_rad:
                    p_area = 2*pi*r*h
                else:
                    p_area = 2*pi*r*h + pi*r*r - pi*max_rad*max_rad
                if p_area > p_max:
                    p_max = p_area
                    p_max_num = p_num
            surface_area += p_max
            max_rad = max(max_rad, pancakes[p_max_num][0])
            del pancakes[p_max_num]

        print("Case #{0}: {1}".format(case_num + 1, surface_area))

main()
