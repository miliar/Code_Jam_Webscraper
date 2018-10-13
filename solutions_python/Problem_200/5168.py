test_case_num = int(raw_input())
test_cases = []

def is_sorted(s):
    if len(s) in [0, 1]:
        return True
    if s[0] <= s[1]:
        return is_sorted(s[1:])
    return False

for test_case in range(test_case_num):
    test_cases.append(raw_input())

output = []
for test_case in test_cases:
    while not is_sorted(str(test_case)):
        num = int(test_case)
        num -= 1
        test_case = num
    output.append(test_case)

n = 1
f = open("output.txt", 'w')
#f.write(output)

for out in output:
    f.write("Case #{}: {}\n".format(n, out))
    n += 1
