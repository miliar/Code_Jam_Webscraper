import sys

def find_min_required_invitees(audience):
    current_clappers = 0
    required_clappers = 0

    for shyness_level, no_of_shy_people in enumerate(audience):

        if shyness_level > current_clappers:
            required_clappers += shyness_level - current_clappers

        current_clappers += no_of_shy_people + max(0, shyness_level - current_clappers)

    return required_clappers

if __name__ == '__main__': 
    #assert find_min_required_invitees([1]) == 0
    #assert find_min_required_invitees([1, 0, 1]) == 1
    #assert find_min_required_invitees([1, 1, 1]) == 0
    #assert find_min_required_invitees([1, 1, 1, 1, 1]) == 0
    #assert find_min_required_invitees([1, 1, 0, 0, 1]) == 2
    #assert find_min_required_invitees([0, 9]) == 1

    sys.stdin.readline()

    for i, line in enumerate(sys.stdin, 1):
        result = find_min_required_invitees((int(n) for n in line.split()[1]))

        print("Case #{}: {}".format(i, result))

