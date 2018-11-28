
def process(R, k, list, ii):
    temp = []
    sum = 0
    for i in range(0, R):
        s = 0
        list1 = list[:]
        for j in list:
            if s+j <= k:
                s += j
                temp.append(list1.pop(0))
            else:
                break
        sum += s
        for l in temp:
            list1.append(l)
        list = list1[:]
        temp = []
    t = "Case #" + str(ii) + ": " + str(sum) + "\n"
    fr.writelines(t)

f = open("d:/test/small.txt", 'r')
ntestcase = int(f.readline())
data = []
k = 0
for i in f.readlines():
    p = i.split(" ")
    for j in range(0, len(p)):
        p[j] = int(p[j])
    data.append(p)

f.close()
i = 0
ii = 1
fr = open("d:/test/result.txt", 'w')
while i < 2 * ntestcase:
    process(data[i][0], data[i][1], data[i+1], ii)
    i += 2
    ii += 1

fr.close()
