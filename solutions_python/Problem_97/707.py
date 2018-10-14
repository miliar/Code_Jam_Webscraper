import threading
timer = None
thread_dict = {}

inp = open('C-large.in', 'r')
out = open('C-large.out', 'w')
test = int(inp.readline())

def no_of_recycle_pairs(digits, num, limit):
    res, cur = 0, {}
    for i in range(digits - 1):
        rem = num % (10 ** (i + 1))
        temp = num / (10 ** (i + 1))
        new = rem * (10 ** (digits - i - 1)) + temp
        if new not in cur:
            res += (num < new and new <= limit) and 1 or 0
            cur[new] = 0
    return res

def calculate(index, digits, A, span, B):
    global thread_dict
    res = 0
    if digits == 1:
        return res
    for num in range(A, span + 1):
        res += no_of_recycle_pairs(digits, num, B)
    thread_dict[index][1] = res
    return
        

for i in range(1, test+1):
    data = inp.readline().split(' ')
    data[-1] = data[-1][-1] == '\n' and data[-1][:-1] or data[-1]
    data = [int(num) for num in data]
    A, B = data[0], data[1]
    no_of_thread, cur = (B - A) <= 100 and 1 or 10, A
    test, digit = B, 0
    written = False
    while test:
        digit += 1
        test /= 10
    thread_dict.clear()
    for j in range(no_of_thread):
        thread_dict[j] = [threading.Thread(target = calculate, args = (j, digit, cur, cur + (B - A) / no_of_thread, B)), 0]
        cur += (B - A) / no_of_thread + 1
    for thread in thread_dict:
        thread_dict[thread][0].start()
    def check():
        global timer, thread_dict, written
        flag = False
        for thread in thread_dict:
            if thread_dict[thread][0].isAlive():
                flag = True
                break
        if flag:
            timer = threading.Timer(1.0, check)
            timer.start()
            return
        res = 0
        for thread in thread_dict:
            res += thread_dict[thread][1]
        out.write("Case #%d: %s\n" %(i, res))
        written = True
        return
        
    timer = threading.Timer(1.0, check)
    timer.start()
    while not written:
        pass
