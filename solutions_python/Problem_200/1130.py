with open('/Users/shawn/Documents/python_proj/codejam/B-large.in', 'r') as f:
    cases = int(f.readline())
    lines = f.readlines()

for case in range(cases):
    num = lines[case].strip()
    stack = []
    smaller = False
    all_nine = False
    for i in range(len(num)):
        digit = int(num[i])
        if stack == [] or stack[-1] <= digit:
            stack.append(digit)
        else:
            smaller = True
            if stack and stack[-1] > 1:
                if len(stack) == 1 or stack[-2] != stack[-1]:
                    stack[-1] -= 1
                else:
                    ele = stack.pop()
                    i -= 1
                    while len(stack) > 1 and stack[-2] == stack[-1]:
                        stack.pop()
                        i -= 1
                    stack[-1] -= 1
            else:
                all_nine = True
            break

    result = ""

    if smaller:
        if all_nine:
            for j in range(len(num) - 1):
                result += "9"
        else:
            while i < len(num):
                result = "9" + result
                i += 1
            while stack:
                num = stack.pop()
                result = str(num) + result
    else:
        while stack:
            num = stack.pop()
            result = str(num) + result

    print "Case #" + str(case + 1) + ": " + str(result)