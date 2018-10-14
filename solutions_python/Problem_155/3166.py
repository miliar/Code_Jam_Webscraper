__author__ = 'prasad'
filename = "inp"


def solve(l):
    standing = 0
    temp = 0
    # standing = int(l[0])
    end = False
    for i in range(0, len(l)):
        # if i == '0':
        # continue

        count = int(l[i])
        # print(count)
        if not end:
            if standing >= i:
                standing += count
                # print("{0}  {1}  {2}  ".format(i, standing, count))
            else:
                temp = standing
                print(
                    "fails required standing= " + str(len(l) - 1 - standing) + " current standings = " + str(standing))
                end = True
                # continue
        if end:
            if int(l[i]) != 0:
                break
            standing += count
            # print(standing)
            # print("success all {0} standing".format(standing))
    print(len(l) - temp - 1)


def solve2(l):
    summ = 0
    for i in range(len(l)):
        if i <= summ:
            # print("{0} {1}".format(i,sum))
            summ += int(l[i])
    success = summ > len(l) - 1
    full_sum = summ
    total = sum([int(x) for x in l])
    if success:
        return 0
    if not success:
        print()
        print(l)
        save = 0
        summ = 0
        need = 0
        for i in range(len(l)):
            if i <= summ:
                print("succ {0} {1}".format(i, summ))
                summ += int(l[i])
                save = summ
            else:

                print("fail {0} {1}".format(i, summ))
                need = i - summ
                summ += need
                summ += int(l[i])
                print("sum = {0}".format(summ))
                pass
        return summ - total
        pass


with open("out", 'w') as g:
    pass
with open(filename, 'r') as inpf:
    line = inpf.readline()
    count = int(line[:-1])
    for c in range(count):
        temp = inpf.readline()[:-1]
        l = temp.split(' ')
        # if not c == 1:
        #     pass
        # solve2(l[1])

        with open("out", 'a') as g:

            mess = "Case #{0}: {1}".format(c + 1, solve2(l[1]))

            g.write(mess + "\n")

