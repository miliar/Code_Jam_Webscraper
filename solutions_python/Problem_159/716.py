# Mushroom monster

filename = 'A-small-attempt0 (1).in'

# Method 1:
def method_1(mushroom_counts):
    res = 0
    for i in range(len(mushroom_counts) - 1):
        if mushroom_counts[i + 1] < mushroom_counts[i]:
            res += mushroom_counts[i] - mushroom_counts[i + 1]
    return res

# Method 2:
def method_2(mushroom_counts):
    res = 0

    # find the largest decrease.
    dec = max(mushroom_counts[i] - mushroom_counts[i + 1] for i in range(len(mushroom_counts) - 1))

    for i in range(len(mushroom_counts) - 1):
        if mushroom_counts[i] > dec:
            res += dec
        else:
            res += mushroom_counts[i]

    
    return res

if __name__ == "__main__":
    file = open(filename)
    fileout = open(filename.split('.')[0] + '.out', 'w')
    
    t = int(file.readline())
    for i in range(t):
        n = file.readline() 
        a = [int (i) for i in file.readline().split()]
        fileout.write("Case #{}: {} {}\n".format(i + 1, method_1(a), method_2(a)))
    
    fileout.close()
    print("done")
