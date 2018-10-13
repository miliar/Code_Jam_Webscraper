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
            line = content[i+1]
            items.append(line)
    return content

def test_cases():
    data = read_inputs()
    cases = int(data[0])
    sol = []
    line = 1
    for i in range(0, cases):
        distance, horses = data[line].split(' ')[0], data[line].split(' ')[1]
        l = []
        l.append((int(distance), int(horses)))
        line += 1
        for horse in range(0, int(horses)):
            hspeed, hdistance = int(data[line].split(' ')[0]), int(data[line].split(' ')[1])
            line += 1
            l.append((int(hspeed), int(hdistance)))
        sol.append(l)
    return sol


def horses():
    sol = test_cases()
    res = []
    for case in range(0, len(sol)):
        distance, horses = sol[case][0]
        nr = 0
        for i in range(1, len(sol[case])):
            hd, hs = sol[case][i]
            t = (distance - hd)/hs
            nr = max(t,nr)
        
        res.append(distance/nr)

    return res


def print_answer():
    h = horses()
    for i in range(0, len(h)):
        print ('Case #' +str(i+1) +': ',h[i])


print_answer()