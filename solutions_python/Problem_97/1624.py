import sys


with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()

T = int(lines[0])

results=[]
i=1
case = 1

def get_number_of_recycled_pairs(A, B):
    """
    100
    101 110
    102 210
    103 310
    104 410
    105
    110
    112 211 121


    """
    min = A
    max = B+1
    results = {}
    for k in range(min, max):
        results[k] = 0
    for target_num in range(min, max):
        ts = str(target_num)
        if len(ts) == 1:
            continue
        for index in range(1, len(ts)):
            recycled = int(ts[index:]+ts[:index])
            if recycled<A or recycled>B:# or results[recycled]==1:
                continue
            if target_num < recycled:
                results[target_num] += 1

    number_of_recycled_pairs = 0
    for v in results.values():
        number_of_recycled_pairs += v

    return number_of_recycled_pairs


for line in lines[1:]:
    A,B = map(int, line.split(" "))
    results.append(get_number_of_recycled_pairs(A, B))
    i += 1


with open("out", "w") as f:
    for i,result in enumerate(results):
        print "Case #{0}: {1}\n".format(i+1, result)
        f.write("Case #{0}: {1}\n".format(i+1, result))


