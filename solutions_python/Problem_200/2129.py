def tidy(N, index):
    if index == len(N) - 1:
        return N
    else:
        if N[index] > N[index + 1]:
            result = N[0: index] + str(int(N[index]) - 1)
            for i in range(len(N) - index - 1):
                result = result + "9"
            if result[0] == "0" :
                return result[1:]
            return tidy(result, 0)

        else:
            return tidy(N, index + 1)
print("132", 0)
with open("E:\Python\CodeJam\B-large.in", "r") as f:
    data = f.readlines()[1:]
f.close()
with open("E:\Python\CodeJam\B-large.txt", "w") as w:
    for i in range(len(data)):
        print(data[i])
        w.write("Case #" + str(i + 1) + ": " + str(tidy(data[i].split()[0], 0)) + "\n")