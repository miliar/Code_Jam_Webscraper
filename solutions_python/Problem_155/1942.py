__author__ = 'Q'


def get_friends(max, shyness_levels):
    standing = 0
    invited = 0
    for level in range(0, max + 1):
        members = int(shyness_levels[level])
        if level <= standing:
            standing += members
        else:
            invited += (level - standing)
            standing += (level - standing)+members
    return invited


def main(data):
    data = data.split('\n')
    number_lines = int(data[0])
    for i in range(1, number_lines+1):
        case = data[i].split()
        to_invite = get_friends(int(case[0]), case[1])
        print("Case #{0}: {1}".format(i, to_invite))




with open("C:/Users/Q/Downloads/A-large.in") as fh:
    data = ''
    for line in fh:
        data+= line
    main(data)
