# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer

IMPOSSIBLE = "IMPOSSIBLE"

def solve(N, manes):
    key_max = max(manes)
    if manes[key_max] > N/2:
        result = IMPOSSIBLE
        return result
    temp_pattern = {}
    # double color >
    result = ""
    #print manes
    if manes["O"] > 0 and manes["O"] < manes["B"]:
        N -= (2*manes["O"] )
        temp_pattern["B"] = "BO"*manes["O"]+"B"
        manes["B"] -= manes["O"]
        manes["O"] = 0

    elif manes["O"] == manes["B"] and manes["O"] * 2 == N:
        result = "BO"*manes["O"]
        return result;
    elif manes["O"] > manes["B"]:
        result = IMPOSSIBLE
        return result
    #print manes
    if manes["G"] > 0 and manes["G"] < manes["R"]:
        N -= (2 * manes["G"] )
        temp_pattern["R"]= "RG"*manes["G"]+"R"
        manes["R"] -= manes["G"]
        manes["G"] = 0

    elif manes["G"] == manes["R"] and manes["G"] * 2 == N:
        result = "RG"*manes["G"]
        return result;
    elif manes["G"] > manes["R"]:
        result = IMPOSSIBLE
        return result
    #print manes

    if manes["V"] > 0 and manes["V"] < manes["Y"]:
        N -= (2 * manes["V"] )
        temp_pattern["Y"]= "YV"*manes["V"]+"Y"
        manes["Y"] -= manes["V"]
        manes["V"] = 0
    elif manes["V"] == manes["Y"] and manes["V"] * 2 == N:
        result = "YV"*manes["V"]
        return result;
    elif manes["V"] > manes["Y"]:
        result = IMPOSSIBLE
        return result

    #print temp_pattern,manes
    key_max = max(manes,key = manes.get)
    if manes[key_max] > N/2:
        result = IMPOSSIBLE
        return result

    #for B,R,Y circles:
    front_key = key_max
    #print manes
    #print "front key:", front_key
    result += temp_pattern.get(key_max, key_max)
    N -= 1
    manes[front_key] -= 1
    #print manes
    while N > 0:
        key_list = sorted(manes, key=manes.get, reverse=True)
        key_max = key_list[0]
        # if N < 3:
        #     print key_list, manes, front_key
        if result[-1] == key_list[0]:
            key_max = key_list[1]
        elif manes[key_list[0]] == manes[key_list[1]] and key_list[1] == front_key and key_list[1]!=result[-1]:
            key_max = key_list[1]
        elif manes[key_list[0]] == manes[key_list[1]] == manes[key_list[2]] and key_list[2] == front_key and key_list[2]!=result[-1]:
            key_max = key_list[2]
        # if N < 3:
        #     print key_max
        result += temp_pattern.get(key_max, key_max)
        manes[key_max] -=1
        N -= 1
        #print manes
    return result

for i in xrange(1, t + 1):
    N, R, O, Y, G, B, V = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    manes = {"R":R, "O": O, "Y":Y, "G":G, "B":B, "V":V}
    n = N
    result = solve(N, manes)

    print "Case #{0}: {1} ".format(i, result)
    # check out .format's specification for more formatting options