#coding:utf-8

#for b-small

def print_result(casenum,result):
    print "Case #" + str(casenum) + ": " + str(result)


if __name__ == '__main__':

    T = int(raw_input()) #行数

    N=2000 #largeだと10^18

    nums = []
    for i in range(1,N+1):

        num = list(str(i))
        f=1
        for j in range(1,len(num)):
            if num[j-1] > num[j]:
                f = 0
                break
        if f ==1: nums.append(i)



    for casenum in range(1,T+1):#Tの回数実行する

        input = int(raw_input())

        bnum = nums[0]
        for i in nums:
            if i > input:
                print_result(casenum,bnum)
                break
            bnum = i

