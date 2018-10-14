import random

expansion_dictionary = dict()
expansion_dictionary[1] = (0,0,[]) # min, max, to_extend

def dynamic_calculate_left_right(bathroom_stalls,kth_person, verbose=False):
    to_expand = [bathroom_stalls]
    for personhelping in range(kth_person):
        if verbose and personhelping % 1000 == 1:
            print(bathroom_stalls - personhelping)
        to_expand.sort(reverse=True)
        num_to_expand = to_expand.pop(0)
        if num_to_expand in expansion_dictionary:
            min, max, to_extend = expansion_dictionary[num_to_expand]
            to_expand.extend(to_extend)
        else:
            min, max = (num_to_expand-1) // 2, num_to_expand // 2
            expansion_dictionary[num_to_expand] = (min, max, [min, max])
            to_expand.extend([min,max])
    return min, max


def calculate_left_right(bathroomstalls,personcount):
    if personcount == 1:
        return bathroomstalls//2, (bathroomstalls-1)//2
    halfway = personcount//2
    if halfway * 2 == personcount:
        nextone = bathroomstalls // 2
    else:
        nextone = (bathroomstalls-1) // 2
    return calculate_left_right(nextone, personcount//2)

def stresstest(maxstalls):
    for _ in range(100):

        stalls = random.randint(2,maxstalls)
        calculate_left_right(stalls, stalls - 1)
        if not dynamic_calculate_left_right(stalls, stalls-1) == calculate_left_right(stalls,stalls-1):
            print(dynamic_calculate_left_right(stalls, stalls-1))
            print(calculate_left_right(stalls, stalls - 1))
            input("Help!")


if __name__ == "__main__":
    with open('C-large.in') as f:
        for casenum, line in enumerate(f):
            if casenum == 0:
                continue
            stall_count, k_person = line.split()
            stall_count, k_person = int(stall_count), int(k_person)
            maxr, minl = calculate_left_right(stall_count,k_person)
            print("Case #%d: %d %d" % (casenum, maxr, minl))

