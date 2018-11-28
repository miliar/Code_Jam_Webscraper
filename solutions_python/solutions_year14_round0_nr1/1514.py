#f =  open('input.txt', 'r')
#a = f.read()
#print (a)
#f.close()

def handle_output(caseno, list1, list2):
    matches = 0
    num = list1[0]
    for elem1 in list1:
        if elem1 in list2:
            matches += 1
            num = elem1

    if matches == 0:
        outstr = 'Case #' + str(caseno) + ': Volunteer cheated!\n'
    elif matches == 1:
        outstr = 'Case #' + str(caseno) + ': ' + str(num) + '\n'
    else:
        outstr = 'Case #' + str(caseno) + ': Bad magician!\n'
    with open('output.txt', 'a') as fo:
        fo.write(outstr)

with open('output.txt', 'w') as fo:
    pass

with open('input.txt') as fi:
    T = int(fi.readline())
    for t in range(1, T+1):
        ans1 = int(fi.readline())
        for i in range(1,5):
            if ans1==i:
                line1 = fi.readline()
            else:
                fi.readline()
        ans2 = int(fi.readline())
        for i in range(1,5):
            if ans2==i:
                line2 = fi.readline()
            else:
                fi.readline()
        #print(line1, "---" ,line2)
        list1 = [int(k) for k in line1.split(' ')]
        list2 = [int(k) for k in line2.split(' ')]
        #print(list1, list2)
        handle_output(t, list1, list2)
