
def calc(in_file):
    s = list(in_file.readline())
    alph_map = dict()
    alph_map['Z'] = 0
    alph_map['W'] = 0
    alph_map['U'] = 0
    alph_map['F'] = 0
    alph_map['X'] = 0
    alph_map['V'] = 0
    alph_map['G'] = 0
    alph_map['O'] = 0
    alph_map['R'] = 0
    alph_map['I'] = 0



    for alpha in s:
        if alpha not in alph_map: alph_map[alpha] = 0
        alph_map[alpha] += 1

    dig_map = dict()

    #zero
    dig_map[0] = 0
    while alph_map['Z'] > 0:
        alph_map['Z'] -= 1
        alph_map['E'] -= 1
        alph_map['R'] -= 1
        alph_map['O'] -= 1
        dig_map[0] += 1

    dig_map[2] = 0
    while alph_map['W'] > 0:
        alph_map['T'] -= 1
        alph_map['W'] -= 1
        alph_map['O'] -= 1
        dig_map[2] += 1

    dig_map[4] = 0
    while alph_map['U'] > 0:
        alph_map['F'] -= 1
        alph_map['O'] -= 1
        alph_map['U'] -= 1
        alph_map['R'] -= 1
        dig_map[4] += 1

    dig_map[5] = 0
    while alph_map['F'] > 0:
        alph_map['F'] -= 1
        alph_map['I'] -= 1
        alph_map['V'] -= 1
        alph_map['E'] -= 1
        dig_map[5] += 1

    dig_map[6] = 0
    while alph_map['X'] > 0:
        alph_map['S'] -= 1
        alph_map['I'] -= 1
        alph_map['X'] -= 1
        dig_map[6] += 1

    dig_map[7] = 0
    while alph_map['V'] > 0:
        alph_map['S'] -= 1
        alph_map['E'] -= 1
        alph_map['V'] -= 1
        alph_map['E'] -= 1
        alph_map['N'] -= 1
        dig_map[7] += 1

    dig_map[8] = 0
    while alph_map['G'] > 0:
        alph_map['E'] -= 1
        alph_map['I'] -= 1
        alph_map['G'] -= 1
        alph_map['H'] -= 1
        alph_map['T'] -= 1
        dig_map[8] += 1

    dig_map[1] = 0
    while alph_map['O'] > 0:
        alph_map['O'] -= 1
        alph_map['N'] -= 1
        alph_map['E'] -= 1
        dig_map[1] += 1

    dig_map[3] = 0
    while alph_map['R'] > 0:
        alph_map['T'] -= 1
        alph_map['H'] -= 1
        alph_map['R'] -= 1
        alph_map['E'] -= 1
        alph_map['E'] -= 1
        dig_map[3] += 1

    dig_map[9] = 0
    while alph_map['I'] > 0:
        alph_map['N'] -= 1
        alph_map['I'] -= 1
        alph_map['N'] -= 1
        alph_map['E'] -= 1
        dig_map[9] += 1

    ans = ""
    while dig_map[0] > 0:
        dig_map[0] -= 1
        ans += "0"
    while dig_map[1] > 0:
        dig_map[1] -= 1
        ans += "1"
    while dig_map[2] > 0:
        dig_map[2] -= 1
        ans += "2"
    while dig_map[3] > 0:
        dig_map[3] -= 1
        ans += "3"
    while dig_map[4] > 0:
        dig_map[4] -= 1
        ans += "4"
    while dig_map[5] > 0:
        dig_map[5] -= 1
        ans += "5"
    while dig_map[6] > 0:
        dig_map[6] -= 1
        ans += "6"
    while dig_map[7] > 0:
        dig_map[7] -= 1
        ans += "7"
    while dig_map[8] > 0:
        dig_map[8] -= 1
        ans += "8"
    while dig_map[9] > 0:
        dig_map[9] -= 1
        ans += "9"

    return ans


if __name__ == '__main__':
    in_file = open("input.txt")
    ou_file = open("output.txt", 'w')
    T = int(in_file.readline())
    for t in range(T):
        ans = calc(in_file)
        ou_file.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
    ou_file.close()
