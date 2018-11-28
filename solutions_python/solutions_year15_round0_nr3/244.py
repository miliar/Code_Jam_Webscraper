quat_mul_matrix = [
    [1, 2, 3, 4],
    [2, -1, 4, -3],
    [3, -4, -1, 2],
    [4, 3, -2, -1]
]

def quat_mul(a, b):
    sign = 1
    if a < 0:
        sign *= -1
    if b < 0:
        sign *= -1
    return sign * quat_mul_matrix[abs(a)-1][abs(b)-1]


ijk = quat_mul(quat_mul(2, 3), 4)

def find_prefix(string, value, X, rev=False):
    boundary_results = set()

    prefix_product = 1
    i = 0
    repeats = 1
    while True:
        if rev:
            prefix_product = quat_mul(string[i], prefix_product)
        else:
            prefix_product = quat_mul(prefix_product, string[i])

        if prefix_product == value:
            break
        i = i+1

        if i == len(string):
            if prefix_product in boundary_results:
                break

            boundary_results.add(prefix_product)
            i = 0
            repeats += 1
            if repeats > X:
                break

    return (prefix_product == value, i + (repeats-1) * len(string))
        

T = int(input())

for t in range(T):
    L, X = map(int, input().split())

    string = [ord(x) - ord('i') + 2 for x in input().strip()]

    product = string[0]
    for q in string[1:]:
        product = quat_mul(product, q)
    string_product = product


    product2 = 1
    for i in range(X % 4):
        product2 = quat_mul(product2, product)
    product = product2
    

    if product != ijk:
        print("Case #" + str(t+1) + ": NO")
        continue
    
    found1, pos1 = find_prefix(string, 2, X)
    found2, pos2 = find_prefix(list(reversed(string)), 4, X, rev=True)


    if found1 and found2 and (pos1 + pos2 + 2) < (len(string) * X):
        print("Case #" + str(t+1) + ": YES")
    else:
        print("Case #" + str(t+1) + ": NO")


        

