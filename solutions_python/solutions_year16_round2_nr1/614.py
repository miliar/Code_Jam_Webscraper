def solve(s, x, res):
    charmap = {}
    for c in s:
        if c not in charmap.keys():
            charmap[c] = 0
        charmap[c] += 1
    zero = charmap.get('Z', 0)
    two = charmap.get('W', 0)
    four = charmap.get('U', 0)
    six = charmap.get('X', 0)
    eight = charmap.get('G', 0)
    if 'Z' in charmap:
        charmap['Z'] -= zero
        charmap['E'] -= zero
        charmap['R'] -= zero
        charmap['O'] -= zero
    if 'W' in charmap:
        charmap['T'] -= two
        charmap['W'] -= two
        charmap['O'] -= two
    if 'U' in charmap:
        charmap['F'] -= four
        charmap['O'] -= four
        charmap['U'] -= four
        charmap['R'] -= four
    if 'X' in charmap:
        charmap['S'] -= six
        charmap['I'] -= six
        charmap['X'] -= six
    if 'G' in charmap:
        charmap['E'] -= eight
        charmap['I'] -= eight
        charmap['G'] -= eight
        charmap['H'] -= eight
        charmap['T'] -= eight
    one = charmap.get('O', 0)
    three = charmap.get('H', 0)
    five = charmap.get('F', 0)
    seven = charmap.get('S', 0)
    if one > 0:
        charmap['O'] -= one
        charmap['N'] -= one
        charmap['E'] -= one
    if three > 0:
        charmap['T'] -= three
        charmap['H'] -= three
        charmap['R'] -= three
        charmap['E'] -= three
        charmap['E'] -= three
    if five > 0:
        charmap['F'] -= five
        charmap['I'] -= five
        charmap['V'] -= five
        charmap['E'] -= five
    if seven > 0:
        charmap['S'] -= seven
        charmap['E'] -= seven
        charmap['V'] -= seven
        charmap['E'] -= seven
        charmap['N'] -= seven
    nine = charmap.get('I', 0)
    phonenum = ""
    for i in range(zero):
        phonenum += "0"
    for i in range(one):
        phonenum += "1"
    for i in range(two):
        phonenum += "2"
    for i in range(three):
        phonenum += "3"
    for i in range(four):
        phonenum += "4"
    for i in range(five):
        phonenum += "5"
    for i in range(six):
        phonenum += "6"
    for i in range(seven):
        phonenum += "7"
    for i in range(eight):
        phonenum += "8"
    for i in range(nine):
        phonenum += "9"
    res.write("Case #{}: {}\n".format((x + 1), phonenum))


def main():
    f = open("C://CodeJam/alarge.in", 'r')
    res = open("C://CodeJam/alarge.out", 'w')
    T = int(f.readline())
    for x in range(T):
        s = f.readline()
        solve(s, x, res)
    f.close()
    res.close()

if __name__ == "__main__":
    main()
