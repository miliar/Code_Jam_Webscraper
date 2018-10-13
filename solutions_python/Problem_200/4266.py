def read_number():
    data = input()
    res = []
    for i in range(0, len(data)):
        res.append(int(data[i]))
    return res

def number_to_str(number, last_idx):
    res = str(number[0]) if number[0] > 0 else ""
    for i in range(1, last_idx):
        res = res + str(number[i])
    for i in range(last_idx, len(number)):
        res = res + "9"

    return res

def process(number):
    last_idx = len(number)
    sdf = False
    for i in range(1, len(number)):
        if number[i] < number[i - 1]:
            number[i - 1] = number[i - 1] - 1
            last_idx = i - 1
            sdf = True
            break

    if not sdf:
        return number_to_str(number, len(number))

    not_done = True
    while not_done:
        not_done = False
        for i in range(last_idx, 0, -1):
            if number[i] < number[i - 1]:
                number[i - 1] = number[i - 1] - 1
                last_idx = i - 1
                not_done = True
                break

    return number_to_str(number, last_idx + 1)

test_cnt = int(input())

for t_idx in range(1, test_cnt + 1):
    number = read_number()
    print("Case #" + str(t_idx) + ": " + process(number))