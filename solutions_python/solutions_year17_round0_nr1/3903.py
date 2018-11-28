#coding:utf-8

#for A-small

def print_result(casenum,result):
    if result==1001:
        print "Case #" + str(casenum) + ": IMPOSSIBLE"
    else:
        print "Case #" + str(casenum) + ": " + str(result)

def check(S):
    return S.find("-")

def calcpan(S,K,num,resnum):#S,K,再帰回数,ひっくり返した回数
    if check(S[0:num]) != -1:
        return 1001
    if num+K > len(S):
        if check(S) != -1:
            return 1001
        #print S,resnum
        return resnum



    #ひっくり返さない
    result1 = calcpan(S,K,num+1,resnum)

    #ひっくりかえす
    for j in range(num,num+K):
        if S[j] == "+":
            S = S[:j] + '-' + S[j+1:]
        else:
            S = S[:j] + '+' + S[j+1:]



    result2 = calcpan(S,K,num+1,resnum+1)

    return min(result1,result2)

if __name__ == '__main__':

    T = int(raw_input()) #行数

    for casenum in range(1,T+1):#Tの回数実行する

        input = raw_input().split()
        S = input[0] # + happy or - blank
        K = int(input[1])

        if check(S) == -1:
            result = 0
        else:
            #全通り計算(small用)
            result = calcpan(S,K,0,0)

        print_result(casenum,result)






