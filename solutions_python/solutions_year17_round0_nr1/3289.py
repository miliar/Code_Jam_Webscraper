
f = open("A-large.in");
f.readline() # Remove total tc cnt..
tc_cnt = 1;

def reverse(char):
    if char=="+":
        return "-"
    else:
        return "+"

while True:
    # 문자열을 문자 배열로 변경 -> 맨 앞이 +인 경우 넘어감, -인 경우 #문자배열에서 토큰[1] 길이만큼 +-를 뒤집음 ->
    # 카운터를 1증가 시키고, 기존 문자배열에서 pop[0]
    # 남은 문자열의 길이가 토큰[1]의 길이와 같을때까지 반복
    # 토큰[1]의 길이와 문자열의 길이가 같을때 모든 요소가 +면 카운터 증가 없이 종료, 모두 -면 카운터 +1 하고 종료, +-가 섞여 있으면 IMPOSSIBLE 출력

    flip_cnt = 0;
    line = f.readline()
    if not line: break
    token = line.split(" ")
    tokenArr = list(token[0])

    while len(tokenArr) > int(token[1]):
        if tokenArr[0] == "-":
            for x in range(0, int(token[1])):
                tokenArr[x] = reverse(tokenArr[x])
            flip_cnt += 1
        tokenArr.pop(0)


    if tokenArr.count("+") == int(token[1]) and tokenArr.count("-") == 0:
        print("Case #"+str(tc_cnt)+": " + str(flip_cnt))
    elif tokenArr.count("-") == int(token[1]) and tokenArr.count("+") == 0:
        print("Case #"+str(tc_cnt)+": " + str(flip_cnt+1))
    else:
        print("Case #"+str(tc_cnt)+": IMPOSSIBLE")

    tc_cnt+=1


f.close()
