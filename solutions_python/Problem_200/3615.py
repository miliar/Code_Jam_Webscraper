#Oversized Pancake Flipper

def check(num):

    tmp = list(str(num))
    ret = []
    for idx, value in enumerate(tmp):
        if idx == 0:
            continue
        if value < tmp[idx-1]:
            tmp[idx-1] = str(int(tmp[idx-1])-1)
            #print(tmp, tmp[:idx-1], tmp[idx:])
            ret = tmp[:idx]
            ret.extend(['9']*len(tmp[idx:]))
            return int(''.join(ret))
    return num

def solution(case):
    tmp = int(input())

    ans = check(tmp)
    while ans != check(ans):
        ans = check(ans)
    """
    for i in reversed(range(tmp+1)):
        ret = check(i)
        if ret == -1:
            ans = i
            break
    """

    print("Case #" + str(case) + ": " + str(ans))

if __name__ == "__main__":
    cases = input()
    for case in range(1, int(cases)+1):
        solution(case)
