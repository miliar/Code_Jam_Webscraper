'''
Problem

Last year, the Infinite House of Pancakes introduced a new kind of pancake. It has a happy face made of chocolate chips on one side (the "happy side"), and nothing on the other side (the "blank side").

You are the head cook on duty. The pancakes are cooked in a single row over a hot surface. As part of its infinite efforts to maximize efficiency, the House has recently given you an oversized pancake flipper that flips exactly K consecutive pancakes. That is, in that range of K pancakes, it changes every happy-side pancake to a blank-side pancake, and vice versa; it does not change the left-to-right order of those pancakes.

You cannot flip fewer than K pancakes at a time with the flipper, even at the ends of the row (since there are raised borders on both sides of the cooking surface). For example, you can flip the first K pancakes, but not the first K - 1 pancakes.

Your apprentice cook, who is still learning the job, just used the old-fashioned single-pancake flipper to flip some individual pancakes and then ran to the restroom with it, right before the time when customers come to visit the kitchen. You only have the oversized pancake flipper left, and you need to use it quickly to leave all the cooking pancakes happy side up, so that the customers leave feeling happy with their visit.

Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to leave all pancakes happy side up, or state that there is no way to do it.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S and an integer K. S represents the row of pancakes: each of its characters is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up).

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is either IMPOSSIBLE if there is no way to get all the pancakes happy side up, or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it.

Limits

1 ≤ T ≤ 100.
Every character in S is either + or -.
2 ≤ K ≤ length of S.
Small dataset

2 ≤ length of S ≤ 10.
Large dataset

2 ≤ length of S ≤ 1000.
Sample


Input

Output

3
---+-++- 3
+++++ 4
-+-+- 4

Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE

'''

def flip_string(s,strt,end):
    new_str = ""
    for i in range(len(s)):
        if i>=strt and i<end:
            if s[i]=='+':
                new_str+='-'
            else:
                new_str += '+'
        else:
            new_str+=s[i]
    return new_str
def check_if_all_happ(s):
    for c in s:
        if c != "+":
            return 0
    return  1

def Min_No_Flips(s,k):
    y = 0
    ret = check_if_all_happ(s)
    if ret == 1:
        return  0
    done = 0
    first = 0
    num_flips = 0
    new_s=s
    while done!=1:
        for i in range(len(new_s)):
            if new_s[i]=="-":
                first = i
                break
        end = first+k
        #print("first " + str(first) + " end " + str(end))
        if end>len(new_s):
            return "IMPOSSIBLE"
        new_s = flip_string(new_s,first,end)
        #print(new_s)
        num_flips+=1
        ret = check_if_all_happ(new_s)
        if ret == 1:
            return num_flips
    return y

input_file_path = "c:/test/A-large.in"
num_cases = 0
lines = []
with open(input_file_path, 'r') as filep:
        for line in filep:
            if num_cases == 0:
                num_cases = int(line)
                continue
            else:
                lines.append(line)

filehandle = open("c:/test/result.txt",'w')
for i in range(len(lines)):
    s,k = str(lines[i]).split(' ')
    y = Min_No_Flips(s,int(k))
    #print("Case #"+str(i+1)+": "+str(y))
    filehandle.write("Case #"+str(i+1)+": "+str(y)+"\n")

filehandle.close()