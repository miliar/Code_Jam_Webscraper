'''
Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.

Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ N ≤ 1000.
Large dataset

1 ≤ N ≤ 1018.
Sample


Input

Output

4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999


'''
def get_digits(num):
    #print("input num "+str(num))
    digits = [int(i) for i in str(num)]
    return digits
def last_tidy(num):
    digits = get_digits(num)
    #print(digits)
    if len(digits) == 1:
        return num
    done = 0
    while done!=1:
        digits = get_digits(num)
        is_tidy = 1
        for i in range(len(digits)-1):
            if digits[i+1]<digits[i]:
                is_tidy=0
                break
        #print("is_tidy "+str(is_tidy))
        if is_tidy ==1:
            return num
        num-=1
        #print(num)
        #last_tidy(num)
    return 0
input_file_path = "C:\\test\\Tidy_Numbers//B-small-attempt0.in"
num_cases = 0
lines = []
with open(input_file_path, 'r') as filep:
        for line in filep:
            if num_cases == 0:
                num_cases = int(line)
                continue
            else:
                lines.append(line)

filehandle = open("C:\\test\\Tidy_Numbers//result.txt",'w')
for i in range(len(lines)):
    #s,k = str(lines[i]).split(' ')
    #y = Min_No_Flips(s,int(k))
    #print("Case #"+str(i+1)+": "+str(y))
    num = int(lines[i])
    lst_tidy = last_tidy(num)
    print("Case #" + str(i + 1) + ": " + str(lst_tidy) + "\n")
    filehandle.write("Case #" + str(i + 1) + ": " + str(lst_tidy) + "\n")
filehandle.close()