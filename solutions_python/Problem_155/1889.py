## Question 1 Ovation
num_of_case = int(raw_input())

def do(data):
    current = 0
    addition = 0
    for i in range(len(data)):
        if i == 0:
            current += data[i]
        else:
            if data[i] == 0:
                continue
            if current >= i:
                current += data[i]
            else:
                addition += i - current
                current += addition + data[i]
    return addition
        

for i in range(num_of_case):
    line = raw_input()
    data = line.split(' ')[1]
    data = [int(x) for x in data]
    addition = do(data)
    print("Case #%d: %d"% (i+1, addition))