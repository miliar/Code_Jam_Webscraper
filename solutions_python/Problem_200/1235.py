fin = open("B-large.in", "r")
fout = open("output.txt", "w")

tc = int(fin.readline())
for t in range(0, tc):
    numbers = list(fin.readline().strip())
    result = ""
    if len(numbers) == 1:
        result = numbers[0]
    else:
        while True:
            isChanged = False
            for i in range(1, len(numbers)):
                if numbers[i-1] > numbers[i]:
                    isChanged = True
                    numbers[i-1] = chr(ord(numbers[i-1]) - 1)
                    for j in range(i, len(numbers)):
                        numbers[j] = '9'
                    break
            if not isChanged:
                break
        while True:
            if numbers[0] == '0':
                numbers.pop(0)
            else:
                break
        for ch in numbers:
            result = result + ch
    fout.write("Case #" + str(t+1) + ": " + str(result) + "\n")

fin.close()
fout.close()