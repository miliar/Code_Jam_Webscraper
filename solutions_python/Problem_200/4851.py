f = open('B-small-attempt0.in', 'r')
g = open('output.in', 'w')
test = int(f.readline())
array = []
array2 = []
array3 = []
array4 = []
for i in range(0, test):
    array.append(int(f.readline()))
for j in range(0, len(array)):
    array2 = [int(d) for d in str(array[j])]
    array4 = sorted(array2)
    if  array4 == array2:
        g.write('Case #' + str(j + 1) + ': ' + str(array[j]) + "\n")
    else:
        for k in range(array[j], 0, -1):
            array2 = [int(d) for d in str(k)]
            array4 = sorted(array2)
            if  array4 == array2:
                g.write('Case #' + str(j + 1) + ': ' + str(k) + "\n")
                break
            else:
                continue
f.close()
g.close()
