__author__ = 'Orin'

nums = {}
nums[1] = 1

def flip(num):
    num = str(num)
    num = num[::-1]
    return int(num)

def buildNums(maxNum = 1000000):
    for i in range(2, maxNum + 1):
        fliped = flip(i)

        if  fliped >= i:
            nums[i] = nums [i-1] + 1
        elif i % 10 == 0:
            nums[i] = nums [i-1] + 1
        else:
            if nums[fliped] > nums[i-1]:
                nums[i] = nums [i-1] + 1
            else:
                nums[i] = nums[fliped] + 1

def main():
    folder_path = 'C:\\Users\\Orin_2\\Projects\\CodeJam\\'
    in_name = 'A-small-attempt0.in'
    out_name = 'A-small-attempt0.out'
    maxNum = 10**6
    buildNums(maxNum)
    with open(folder_path + in_name,'r') as inp:
        cases = inp.read().split('\n')
    
    for c in range(len(cases)):
        cases[c]  = int(cases[c])
    t = cases[0]
    cases.remove(t)



    with open(folder_path + out_name,'w') as out:
        for case in range(t):
            num = cases[case]
            times = nums[num]
            out.write("Case #{0}: {1}\n".format(case+1,times))

if __name__ == '__main__':
    main()