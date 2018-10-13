import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_inputs():
    number = 0
    items = []
    with open(os.path.join(__location__, "input.txt")) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        number = int(content[0])
        for i in range(0, number):
            line = content[i+1].split()
            items.append((line[0], int(line[1])))
    return number, items


def get_flips(data, k):
    count = 0
    flip = {'-': '+', '+': '-'}
    for i in range(0, len(data)):
        if data[i] == '-':
            if len(data) - i < k:
                return 'IMPOSSIBLE'
            else:
                count += 1
                for j in range(i+1, i+k):
                    data[j] = flip[data[j]]
    return count

def get_output():
    number, items = read_inputs()
    for i in range(0, number):
        k = items[i][1]
        data = list(items[i][0])
        print('Case #' +str((i+1))+':',get_flips(data, k))


get_output()
    