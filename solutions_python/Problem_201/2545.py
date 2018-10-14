
from itertools import groupby
import math

f = open("C-small-1-attempt0.in");
f.readline() # Remove total tc cnt..
tc_cnt = 1;

def removeOFromArr(arr):
    for idx, x in enumerate(arr):
        if x[0] == "o":
            arr.pop(idx)
        else:
            continue
    return arr

while True:
    # N의 숫자에 맞추어 양 끝에 o로 둘러쌓인 N개의 .을 가진 문자열을 만듬
    # .이 가장 긴 곳을 확인
    # .이 가장 긴 곳의 . 길이가 홀수이면 중앙을, 짝수이면 절반보다 -1 인 곳의 .을 o로 교체
    # 위 루틴을 cnt+1 < K 일때까지 반복
    # cnt+1 값이 K일때 .이 가장 긴 곳의 다시 확인
    # 중앙값 선택 후 죄우측의 간격중 긴 곳을 Max로 짧은곳을 Min으로 결과값 만들어 출력

    cnt = 0;
    line = f.readline()
    if not line: break
    token = line.split(" ")

    stallNum = int(token[0])
    people = int(token[1])

    temp_str = "o"+"."*stallNum+"o"

    while cnt+1 < people:
        groups = groupby(temp_str)
        result = [(label, sum(1 for _ in group)) for label, group in groups]
        longest_dot = max(removeOFromArr(result), key=lambda x: x[1])[1]

        if longest_dot % 2 == 0:
            index = longest_dot/2 - 1
        else:
            index = math.floor(longest_dot/2)

        position = temp_str.find("."*longest_dot)
        temp_str = temp_str[0:int(index)+position] + "o" + temp_str[int(index)+1+position:]

        cnt += 1


    groups = groupby(temp_str)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    longest_dot = max(removeOFromArr(result), key=lambda x: x[1])[1]


    if longest_dot == 1:
        max_val = min_val = 0
    elif longest_dot % 2 == 0:
        max_val = longest_dot / 2
        min_val = longest_dot / 2 - 1
    else:
        max_val = min_val = math.ceil(longest_dot / 2) - 1

    print("Case #"+str(tc_cnt)+": "+str(int(max_val))+" "+str(int(min_val)))

    tc_cnt += 1


f.close()