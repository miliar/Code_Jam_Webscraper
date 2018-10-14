
# https://code.google.com/codejam/contest/dashboard?c=2974486

#f = open("test.txt")
f = open("A-small-attempt3.in")
testCaseNumber = int(f.readline())
# 按照题目的说明, 第一行的数字代表了有多少个测试案例(test case)
# 我们这次是数字 100


# 1个测试案例有10行
# 100个测试案例有1000行
# A-small-attempt0.in 这个文件刚好有1001行. 里面有1000行的测试案例+第一行那个数字告诉你有多少测试案例


message = ""
string_that_save_to_file = ""

for case_number in list(range(1, testCaseNumber+1)):  # 循环100次，每次拿一个测试案例

    one_case = ""
    for b in list(range(1,11)): # 因为每个测试案例有10行，所以我们循环10次，然后获取到这10行
        one_case = one_case + f.readline()
    # 现在我们开始处理这10行
    one_case_list = one_case.split("\n") # 按换行符分割成列表
    case1_list = one_case_list[0:5]   # 拿到case1
    case2_list = one_case_list[5:]    # 拿到case2, 格式都是列表, 类似这样:['2', '8 2 7 15', '3 1 5 6', '4 10 16 14', '9 11 12 13', '']

    case1_number = case1_list[0]  # 我们把志愿者报的那一行, 从字符串拆成列表.
    case2_number = case2_list[0]  # 这里同样.

    case1_the_row = case1_list[int(case1_number)]  # case1_the_row 是 string 类型
    case2_the_row = case2_list[int(case2_number)]
    case1_the_row = case1_the_row.split()
    case2_the_row = case2_the_row.split()



    # 拿列表1里每个数字和列表2里面比较
    # 看看有多少个数字是一样的
    same_number_list = []
    for n1 in list(range(0,4)):
        for n2 in list(range(0,4)):
            if case1_the_row[int(n1)] == case2_the_row[int(n2)]:
                same_number_list.append(case1_the_row[n1])  # 把这个相同的数字存起来


    if len(same_number_list) == 0:
        message = "Case #" + str(case_number) + ": " + "Volunteer cheated!"
    if len(same_number_list) == 1:
        message = "Case #" + str(case_number) + ": " + same_number_list[0]
    if len(same_number_list) == 2:
        message = "Case #" + str(case_number) + ": " + "Bad magician!"
    if len(same_number_list) == 3:
        message = "Case #" + str(case_number) + ": " + "Bad magician!"
    if len(same_number_list) == 4:
        message = "Case #" + str(case_number) + ": " + "Bad magician!"

    string_that_save_to_file = string_that_save_to_file + message + '\n'




print(string_that_save_to_file)



with open('A_out.txt', 'w') as file:
    file.write(string_that_save_to_file)


