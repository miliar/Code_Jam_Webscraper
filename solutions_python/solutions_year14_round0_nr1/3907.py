def magic(n1, l1, n2, l2):
    return list(set(l1[n1-1]) & set(l2[n2-1]))


f = open("A-small-attempt2.in", "r")
out = open("results.out", "w")
contents = f.readlines()

T = int(contents[0])

i = 1
count = 1
while(T > 0):
    n1 = int(contents[i])
    l11 = map(int, contents[i+1].split(' '))
    l12 = map(int, contents[i+2].split(' '))
    l13 = map(int, contents[i+3].split(' '))
    l14 = map(int, contents[i+4].split(' '))
    l1 = [l11, l12, l13, l14]
    n2 = int(contents[i+5])
    l21 = map(int, contents[i+6].split(' '))
    l22 = map(int, contents[i+7].split(' '))
    l23 = map(int, contents[i+8].split(' '))
    l24 = map(int, contents[i+9].split(' '))
    l2 = [l21, l22, l23, l24]
    result = magic(n1, l1, n2, l2)
    out.write("Case #" + str(count) + ": ")
    if (len(result) == 1):
        out.write(str(result[0]))
    elif (len(result) == 0):
        out.write("Volunteer cheated!")
    else:
        out.write("Bad magician!")
    out.write("\n")
    i += 10
    T -= 1
    count += 1
out.close()