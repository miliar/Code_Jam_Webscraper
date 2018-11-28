from collections import deque, Counter

def solve(line):
    num = int(line)
    while num > 0:
        # print(num)
        str_num = list(str(num))
        if len(str_num) == 1:
            return num
        rev = list(reversed(str_num))
        for i, (a, b) in enumerate(zip(rev[1:], rev)):
            # print(i, len(rev)-2)
            if a > b:
                if rev[i] == "0" and rev[i-1] == "0":
                    j = i
                    while rev[j] == "0" and rev[j-1] == "0" and j > 0:
                        j -= 1
                    num -= 10**j
                    break
                j = i-1 if i else 0
                num -= 10**j
                break
        else:
            return num
        # if str_num == sorted(str_num):
        #     return num
        # num -= 1
    raise Exception("failed")


def main():
    num = int(input())
    for i in range(1, num+1):
        print("Case #{}: {}".format(i, solve(input())))

main()
