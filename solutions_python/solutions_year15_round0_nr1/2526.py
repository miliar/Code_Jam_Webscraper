def read_input():
    max_shyness, shyness_lst = raw_input().split()
    return shyness_lst

def process(inputs):
    shyness_person = inputs
    shyness_person = map(int, shyness_person)
    prefix_sum = 0
    friends_to_add = 0
    for level, num_person in enumerate(shyness_person):
        insufficient = max(level - prefix_sum, 0)
        friends_to_add += insufficient
        prefix_sum += insufficient + num_person
    return friends_to_add

def formating(output):
    return "%d" % output

if __name__ == '__main__':

    T = int(raw_input())
    case_num = 1
    while case_num <= T:
        inputs = read_input()
        result = process(inputs)
        answer = formating(result)

        print "Case #%d: %s" % (case_num, answer)
        case_num += 1
