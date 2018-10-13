import os
import math

f = open('C-small-2-attempt2.in.txt')
cases = int(f.readline())
stalls = []
people = []
results = []
for _ in range(0, cases):
    arr = f.readline().split(" ")
    stalls.append(int(arr[0]))
    people.append(int(arr[1]))


class Stall:
    def __init__(self, occ=False, ls=0, rs=0):
        self.occ = occ
        self.ls = ls
        self.rs = rs


def fill(start, end, person):
    range = end - start + 1
    if range % 2 == 0:
        sta[start + range // 2 - 1] = 1
        fill(start + range // 2 ,end ,person+1)
    else:
        sta[start + range // 2] = 1
        fill(start,start + range // 2 - 1 ,person+1)

def twop(num):
    count = 0
    while num > 1:
        num = num // 2
        count += 1
    return count


for i, item in enumerate(stalls):
    print(i)
    if item == people[i]:
        results.append([0, 0])
    elif twop(item) - twop(people[i]) == 0:
        results.append([0, 0])
    else:
        # sta = []
        # for _ in range(0, item):
        #     sta.append(0)
        # # fill 1 at the left middle
        # fill(0,len(sta)-1,1)
        # # fill 2 at right
       
        # print()

        numbers = []
        numbers.append(item)
        check = 0
        check_req = 1
        for ii in range(0,people[i]):
            if numbers[ii] % 2 != 0:
                numbers.append(numbers[ii] // 2)
                numbers.append(numbers[ii] // 2)
            elif numbers[ii] != 0:
                numbers.append(numbers[ii] // 2)
                numbers.append(numbers[ii] // 2 - 1)
            else:
                numbers.append(0)
                numbers.append(0)
            check += 1
            if check == check_req:
                if ii+1 == people[i]:
                     break
                check_req *= 2
                numbers_prev = numbers[:len(numbers)-check_req]
                numbers_after = numbers[len(numbers)-check_req:]
                numbers_after = sorted(numbers_after, reverse=True)
                numbers = numbers_prev + numbers_after
                check = 0
        results.append(numbers[len(numbers)-2:])





f2 = open('output3.out3.txt', 'w')
for i, result in enumerate(results):
    f2.write("Case #{}: {} {}\n".format(i + 1, result[0], result[1]))
f2.close()
