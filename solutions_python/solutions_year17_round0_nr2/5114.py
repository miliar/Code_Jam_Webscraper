#!/usr/bin/python3

#Author: Shuaib Oladigbolu
#Problem B. Tidy Numbers

def isAscending(list):
    previous = list[0]
    for number in list:
        if number < previous:
            return False
        previous = number
    return True

filename = 'B-small-attempt0'
def main():
    with open(filename+'.in') as file:
        lines = file.read().splitlines()
    cases = int(lines[0])
    lines.remove(lines[0])

    f = open(filename+'.out', 'w')
    for case in range(cases):
        number = int(lines[case])
        for j in reversed(range(number+1)):
            num = str(j)
            numList = []
            for i in num:
                numList.append(i)
            if isAscending(numList) == True:
                f.write('Case #{}: {}\n'.format(str(case+1), str(num)))
                break


if __name__ == '__main__':main()