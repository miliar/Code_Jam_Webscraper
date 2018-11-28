
f = open("B-small-attempt0.in");
f.readline() # Remove total tc cnt..
tc_cnt = 1;


def isTidy(num):
    if(len(str(num)) == 1):
        return True
    else:
        numlist = list(str(num))
        if(numlist.count(0)!=0 or numlist[0] > numlist[len(numlist)-1]):
            return False

        for idx, number in enumerate(numlist):
            try:
               if number <= numlist[idx+1]:
                    continue
            except IndexError:
                return True
            else:
                return False
        return True


while True:
    # 입력된 숫자값이 한자리면 바로 tidy number
    # 그렇지 않으면 숫자를 대입하며 tidy number인지 확인

    # tidy number 큰 자리의 수가 작은 자리의 수보다 작거나 같아 함
    # 입력된 숫자를 문자열 배열로 변경
    # 앞에서부터 2개를 비교하여 앞의 인덱스가 뒤의 인덱스보다 작거나 같은지 비교
    # tidy number이면 true 아니면 false를 반환


    line = f.readline()
    if not line: break
    num = int(line)

    while True:
        if isTidy(num):
            break;
        else:

            num -= 1

    print("Case #"+str(tc_cnt)+": " + str(num))

    tc_cnt+=1


f.close()
