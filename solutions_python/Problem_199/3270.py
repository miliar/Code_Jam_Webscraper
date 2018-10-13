import math

def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n

def twos_comp(val, bits):
    """compute the 2's compliment of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is

def flip(n, bits, start, k):
    if (start + k) > bits:
        return 'UNFLIPPABLE'
    upper = bits - start
    lower = upper - k
    return n ^ ((1<<upper)-1)&~((1<<lower)-1)


cases = int(input())  # read a line with a single integer
for c in range(1, cases + 1):
    pancakes, K = input().split(" ")
    K = int(K)
    num = len(pancakes)
    pancakes =  b''.join([b'1' if s.strip()=='+' else b'0' for s in pancakes])
    # print(pancakes)
    p = int(pancakes, 2)
    # print(p)
    full = 2**num - 1
    if p == full: # all '1's
        print("Case #{}: {}".format(c, 0))
        continue
    if K >= num: # pancake flipper size greater or equal to num of pancakes
        if p == 0:
            print("Case #{}: {}".format(c, 1))
            continue
        else:
            print("Case #{}: {}".format(c, 'IMPOSSIBLE'))
            continue

    flips = 0
    while p < full:
        # get first pancake
        inverted = bit_not(p, num)
        # BELOW... UGH:
        # twos comp of it is inverted inverted plus 1
        # inverted inverted is original p... plus 1
        #twos = twos_comp(inverted, num)
        # twos = p + 1
        # print("twos", bin(twos))
        # found = inverted & twos
        # print("found", bin(found))
        # pos = int(math.log(found, 2))
        # flip K pancakes starting from pos

        # find pos of msb of inverted
        pos = math.floor(int(math.log(inverted, 2)))
        start = num - pos - 1
        p = flip(p, num, start, K)
        if p == 'UNFLIPPABLE':
            flips = 'IMPOSSIBLE'
            break
        # print(bin(p))
        flips += 1        
    print("Case #{}: {}".format(c, flips))
