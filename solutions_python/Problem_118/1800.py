import math
def count(input):
    lines = input.split('\n')
    cases = int(lines[0])
    f1 = file("input_small_fair.txt",'w+b')
    for i in range(cases):
        count = 0
        bounds = lines[i+1].split(" ")
        lower = int(bounds[0])
        upper = int(bounds[1])
        for j in range(lower,upper+1):
            if isPalindrome(j) and isSquare(j) and isPalindrome(int(math.sqrt(j))):
                count += 1
        f1.write("Case #" + str(i+1) + ": " + str(count) + '\n')

def isSquare(number):
    if int(math.sqrt(float(number)))**2 == float(number):
        return True
    return False

def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False


test = """3
1 4
10 120
100 1000"""

input1 = """100
7 122
384 485
484 584
384 484
68 830
612 797
483 485
9 122
65 485
206 283
392 514
7 10
7 121
1 65
9 109
389 713
176 196
257 337
1 302
21 742
1 109
275 955
303 584
120 121
3 5
122 483
120 584
207 328
1 121
121 122
1 1000
483 584
355 689
484 484
425 967
65 484
120 302
78 629
120 221
1 6
356 886
100 1000
7 109
19 333
9 121
126 887
121 484
1 742
107 840
34 811
3 10
9 485
1 104
1 9
122 1000
8 10
21 122
18 526
1 1
3 9
131 843
9 302
435 578
65 122
384 742
1 221
259 334
8 121
10 120
608 726
303 484
1 4
46 453
8 65
7 9
121 121
121 302
3 6
3 65
121 221
65 221
1 485
113 734
120 484
127 209
65 121
198 528
1 10
57 704
87 644
8 122
1 101
1 2
547 967
395 532
8 584
1 5
65 584
120 485
235 963"""
