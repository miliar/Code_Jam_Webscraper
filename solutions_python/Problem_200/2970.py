def readFile(filename):
    result = []
    with open(filename) as file:
        for line in file:
            s = line.strip()
            result.append(s)
    return result

def see(num):
    num = list(num)
    for i in range(len(num) - 1, 0, -1):
        if num[i] < num[i-1]:
            num[i-1] = str(int(num[i-1]) - 1)
            for j in range(i, len(num)):
                num[j] = "9"
    num = "".join(num)
    if num[0] == "0":
        num = num[1:]
    return num
def tidy():
    states = readFile("tidyLarge.txt")
    states = states[1:]
    for i in range(0, len(states)):
        print("Case #" +  str(i+1) + ": " + see(states[i]))
tidy()
