import math
DEBUG = False

def get_area(pancakes):
    area = 0
    pancakes = sorted(pancakes, key=lambda x: x['r'], reverse=True)
    for i in range(len(pancakes)):
        pancake = pancakes[i]
        r = pancake['r']
        h = pancake['h']
        area += (math.pi * r**2) + (2.0 * math.pi * r * h)
        if i != len(pancakes) - 1:
            area -= math.pi * pancakes[i + 1]['r']**2

    return area

ncase = int(raw_input())

for cidx in range(ncase):
    n, k = map(int, raw_input().split())

    idx = -1
    max_area = 0
    pancakes = []
    for i in range(n):
        r, h = map(float, raw_input().split())
        area = (math.pi * r**2) + (2.0 * math.pi * r * h)
        if area > max_area:
            idx = i
            max_area = area
        pancake = {'r': r, 'h': h}
        pancakes.append(pancake)

    result = []
    result.append(pancakes.pop(idx))
    k -= 1
    while k > 0:
        idx = -1
        max_area = 0
        for i in range(len(pancakes)):
            pancake = pancakes[i]
            tmp = list(result)
            tmp.append(pancake)
            area = get_area(tmp)
            if area > max_area:
                max_area = area
                idx = i

        k -= 1
        result.append(pancakes.pop(idx))
    if DEBUG:
        print pancakes;
    print 'Case #{}: {}'.format(cidx + 1, get_area(result))
