import math

def combine_lists(a, b):
    combined = []
    count_a = 0
    count_b = 0
    while count_a < len(a) and count_b < len(b):
        if a[count_a][1] < b[count_b][0]:
            count_a += 1
        elif b[count_b][1] < a[count_a][0]:
            count_b += 1
        elif a[count_a][0] >= b[count_b][0] and a[count_a][0] <= b[count_b][1]:
            combined.append((max(a[count_a][0], b[count_b][0]), min(a[count_a][1], b[count_b][1])))
            count_a += 1
            count_b += 1
        elif b[count_b][0] >= a[count_a][0] and b[count_b][0] <= a[count_a][1]:
            combined.append((max(a[count_a][0], b[count_b][0]), min(a[count_a][1], b[count_b][1])))
            count_a += 1
            count_b += 1
    return combined




t = int(input())
for cases in range(1, t + 1):
    n, p = [int(s) for s in input().split(" ")]
    r = [int(s) for s in input().split(" ")]
    packages = []
    for i in range(n):
        packages.append([int(s) for s in input().split(" ")])
    counts = []
    for ingred_i, ingredient in enumerate(packages):
        counts_ingred = []
        for package_vol in ingredient:
            max_90 = math.floor(package_vol / (r[ingred_i] * 0.9))
            max_110 = math.ceil(package_vol / (r[ingred_i] * 1.1))
            if max_90 < max_110:
                pass #not doable for package
            else:
                counts_ingred.append((max_110, max_90))
        counts_ingred.sort()
        counts.append(counts_ingred)
    counts.sort(key=len)
    answer = 0;
    combined = []
    if (len(counts) == 1):
        answer = len(counts[0])
    else:
        combined = combine_lists(counts[0], counts[1])
        for i in range(2, len(counts)):
            combined = combine_lists(combined, counts[i])
        answer = len(combined)
    
    #print(counts)
        
    print("Case #{}: {}".format(cases, answer))