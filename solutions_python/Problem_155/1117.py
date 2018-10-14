def StandingOvation():
    """docstring for S"""
    f = open("A-large.in")
    i = 0
    T = 0
    res = []
    for line in f:
        if i == 0:
            i = i + 1
            T = int(line)
            continue
        max, array = line.split()
        max = int(max)
        res.append(calculate(max, array))
    return T, res

def calculate(maximum, array):
    """docstring for claculate"""
    count = 0
    sum = 0
    for i in range(maximum + 1):
        cur = int(array[i])
        if i - sum > 0 and cur > 0:
            count = max(count, i - sum)
        sum += cur
    return count

if __name__ == "__main__":
    T, res = StandingOvation()
    f = open('output.txt','w')
    for i in range(1, T+1):
        f.write("Case #" + str(i) + ": " + str(res[i-1]) + "\n")
    f.close()
        
