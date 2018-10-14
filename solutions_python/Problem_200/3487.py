
def ifTidy(num):
    if '0' in num:
        return False
    for i in reversed(range(len(num))):
        if i == 0:
            break
        if num[i] < num[i-1]:
            return False
    return True

def getTidyNum(num):
    result = list(num)
    result[-1] = "9"
    result[-2] = str(int(result[-2]) - 1)
    for i in reversed(range(len(num)-1)):
        if i == 0:
            break
        if int(result[i]) < int(result[i-1]):
            result[i] = "9"
            result[i-1] = str(int(result[i-1]) - 1)
            if int(result[i+1]) < 9:
                for j in range(i+1, len(num)):
                    result[j] = "9"

    return int("".join(result))


file = open('input.txt')
tests = int(file.readline())
cases = []
for t in range(tests):
    cases.append(file.readline().strip())

test = 0
for num in cases:
    test += 1
    k = int(num)
    if not ifTidy(str(k)):
        k = int(getTidyNum(str(k)))
    print("Case #{}: {}".format(test, k))