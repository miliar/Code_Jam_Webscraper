fin = open('A-small-attempt3.in', 'r')
fout = open('output.out', 'w')
if not fin:
    print('error with file input')
cases = int(fin.readline())

for x in range(1, cases + 1):
    m1, m2, result = [], [], []
    row1 = int(fin.readline()) - 1
    for _ in range(4):
        m1.append(fin.readline().strip().split(' '))
    row2 = int(fin.readline()) - 1
    for _ in range(4):
        m2.append(fin.readline().strip().split(' '))
    result = [val for val in m1[row1] if val in m2[row2]]

    s = ''
    if not result:
        s = ("Case #" + str(x) + ": " + "Volunteer Cheated!")
        print(s)
        fout.write(s+'\n')
    elif len(result) > 1:
        s = ("Case #" + str(x) + ": " + "Bad Magician!")
        print(s)
        fout.write(s+'\n')
    elif result:
        s = ("Case #" + str(x) + ": " + str(result[0]))
        print(s)
        fout.write(s+'\n')
    else:
        continue
    # print("Case #{0}: {1!r}".format((x + 1), result))
fin.close()
fout.close()
