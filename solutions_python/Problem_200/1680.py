input = """100
132
1000
7
111111111111111110
181249070016914438
81223444455777788
13455679999555599
145663633140709149
112775
555943756691146504
51468
21
657
787885203785329557
990948919367530586
11111233306
989999999999999999
46663
874204885523600849
523
794022283302264196
109999
83
111233444113455778
504434127209094672
41223333445666677
111111122222222212
22267
32234557777889999
764361320850771565
11224445667888887
11223365778
643411679437108733
109
111122222222012457
1
24297889357525697
232
323344455677888899
936479899185895577
433569
572233121146815505
52443576257
701518434144486040
589799
142473
306252
76999
812333556677778900
329309633723126473
666218905835118716
852309349939941644
1000000000000000000
784659685586488949
182473267803121451
163927162144670666
358915719204841226
731756296075135427
227251459914300594
212233344455667898
40
12215
78167
51368
816089632974196662
33467733347
61222235566778890
54999999999999999
622556
11111111111111053
900350975519011717
179977
41113457778
111111024744150346
112233356666777773
999999999999999999
488010224358949884
734
71222445599
534507039721441027
52246780000
319684074954921624
45599778798789979
806886156594581545
9
12214524824
947427847545839229
11123334455566657
513570
33
841690148931920805
611112222456677889
45679
917593082214474599
637946691710188027
11111122220
78
507
65999999999
11012062055
"""

#digit 0 equals lowest significant digit
def get_digits(x):
    digits = []

    partial = x // 10
    while partial > 0:
        digits.append(x - partial*10)
        x = partial
        partial = x // 10

    digits.append(x)

    return digits


def is_tidy(x):
    last_digit = 9
    for i in get_digits(x):
        if i > last_digit:
            return False
        last_digit = i

    return True

def alternate_solve(x):
    digits = get_digits(x)
    num_digits = len(digits)

    for i in reversed(range(1, num_digits)):
        if digits[i] > digits[i-1]:
            digits[i] = digits[i] - 1

            #mark all remaining digits as 9 (kind of like subtract with carry)
            for i in range(i):
                digits[i] = 9

            break

    out = 0
    mult = 1
    for i in digits:
        out += i * mult
        mult *= 10

    if not is_tidy(x):
        out = alternate_solve(out)

    return out

split_input = [int(x) for x in input.splitlines()]

num_test_cases = split_input[0]
test_cases = split_input[1:]

num_failed = 0

for test_number,i in enumerate(test_cases):
    alternate_solution = alternate_solve(i)
    # print("In: {} Case #{}: {}".format(i, test_number + 1, alternate_solution))
    print("Case #{}: {}".format(test_number + 1, alternate_solution))

    # for j in range(i,0,-1):
    #     if is_tidy(j):
    #         # print("In: {} Case #{}: {}".format(i, test_number+1,j))
    #         if(alternate_solution != j):
    #             print(i, j, alternate_solution)
    #             num_failed += 1
    #         break

# print(num_failed, "failed")