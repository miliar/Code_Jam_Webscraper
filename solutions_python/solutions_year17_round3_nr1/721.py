import math

def base_surface(p):
    r, h = p
    return math.pi * r**2 + 2 * math.pi * r * h

def circumference(p):
    r, h = p
    return 2 * math.pi * r * h

"""
def calculate_surface_area(l, k):
    l.sort(key = lambda x: best_surface(*x))
    p_r, p_h = l.pop()
    surface_area = math.pi * p_r**2 + 2 * math.pi * p_r * p_h
    for i in range(k-1):
        p_r, p_h = l[i]
        surface_area += 2 * math.pi * p_r * p_h
    return surface_area
"""

def calculate_surface_area(l, k):
    sizes = []
    if k == 1:
        for p in l:
            sizes.append(base_surface(p))
    else:
        for p in l:
            new_l = l[::]
            new_l.remove(p)
            sizes.append(surface_area(new_l, k-1, p, 0) + base_surface(p))
    return max(sizes)

def surface_area(l, k, p, a):
    if l and k:
        sizes = []
        for pancake in l:
            r, h = pancake
            if r <= p[0]:
                new_l = l[::]
                new_l.remove(pancake)
                sizes.append(surface_area(new_l, k-1, pancake, circumference(pancake)))
        return a + (max(sizes) if sizes else 0)
    else:
        return circumference(p)


def print_cases(func):
    for i in range(1, int(input())+1):
        n, k = map(int, input().split())
        l = []
        for _ in range(n):
            r, h = map(int, input().split())
            l.append((r, h))
        output = func(l, k)
        print("Case #{}: {}".format(i, output))

if __name__ == "__main__":
    print_cases(calculate_surface_area)

