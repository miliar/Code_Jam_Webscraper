# 2^{S - K + 1} patterns to flip since flipping on the same spot will end up being the same.
def flip(pancakes, K, k):
    #pancakes[:i]
    flipped = ""
    for s in list(pancakes[k:k+K]):
        if s == "+":
            flipped += "-"
        else:
            flipped += "+"
    #pancakes[i+K:]
    return pancakes[:k] + flipped + pancakes[k+K:]

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    pancakes, K_str = input().split()  # read a list of integers, 2 in this case
    K = int(K_str)
    #print("Case #{}: {} {}".format(i, pancakes, K))
    min_flips = 10000000000000
    for j in range(2** (len(pancakes) - K + 1)):
        pancakes_temp = pancakes
        #print(j)
        binary_bits = "{0:b}".format(j).zfill(len(pancakes) - K + 1)
        #print(binary_bits)
        for k, bit in enumerate(list(binary_bits)):
            if bit == "1":
                pancakes_temp = flip(pancakes_temp, K, k)
        #print(pancakes)
        if pancakes_temp == "".join(["+"] * len(pancakes)):
            flips = 0
            for bit in list(binary_bits):
                if bit == "1":
                    flips += 1
            min_flips = min(min_flips, flips)

    if min_flips != 10000000000000:
        print("Case #{}: {}".format(i, flips))
    else:
        print("Case #{}: {}".format(i, "IMPOSSIBLE"))
                
