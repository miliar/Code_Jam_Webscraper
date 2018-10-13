input = file("input.txt")
output = file("output.txt", "w")
result = []

temp = input.readline()
n=int(temp)

phase = "welcome to code jam"
dictionary = {}
for j in range(len(phase)):
    ch = phase[j]
    if ch not in dictionary:
        dictionary[ch] = []
    dictionary[ch].append(j)

for i in range(n):
    count = [0] * len(phase)
    temp = input.readline()[:-1]
    for ch in temp:
        for j in dictionary.get(ch, []):
            if j > 0:
                count[j] += count[j-1]
            else:
                count[0] += 1
    result.append(count[len(phase)-1])

for i in range(n):
    num = result[i] % 10000
    
    print  >> output, "Case #%d: %s" % ((i+1), "%04d" % num)
    
input.close()
output.close()
