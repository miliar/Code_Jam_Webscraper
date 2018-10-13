import sys

test_cases = int(sys.stdin.readline())
checked =[]
def check(i,a,b):
    global checked
    arr_i = list(str(i))
    arr_a = list(str(a))
    arr_b = list(str(b))
    result = 0
    for ind in range(len(arr_i)):
        lett_i = arr_i[ind]
        if int(lett_i) >= int(arr_i[0]) and int(lett_i) <= int(arr_b[0]):
            #print "Here"
            last = arr_i[:ind]
            first = arr_i[ind:]
            num = int(''.join(first+last))
            #print num, a, b, i
            if num >= a and num > i and num <= b and not((i, num) in checked):
                checked.append((i, num))
                result += 1
    #print checked
    return result
def solve_test_case(num):
    nums = str(sys.stdin.readline()).split()
    a = int(nums[0])
    global checked
    b = int(nums[1])
    result = 0
    for i in range(a, b+1):
        checked = []
        result += check(i,a,b)
    print "Case #" + str(num) + ": " + str(result)

for i in range(test_cases):
    solve_test_case(i+1)
