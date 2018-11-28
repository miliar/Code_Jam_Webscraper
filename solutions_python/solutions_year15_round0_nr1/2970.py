def clap(shyness_array):
    standing = 0
    friends = 0
    for require_level, num_ppl in enumerate(shyness_array):
        if standing >= require_level:
            # enough ppl standing
            standing += num_ppl
            #print('{} standing'.format(standing))
        elif num_ppl > 0:
            # Not enough ppl standing
            friends = friends + require_level - standing
            standing = require_level + num_ppl
            #print('need {} friends.'.format(friends))

    #print('total friends: {}'.format(friends))
    return friends




if __name__ == '__main__':
    f = open('input.txt')
    T = int(next(f))
    cases = []
    for line in f:
        n, case = line.split()
        cases.append(case)

    cases = [[int(d) for d in x] for x in cases]

    for x, case in enumerate(cases):
        result = clap(case)
        print('Case #{}: {}'.format(x+1, result))
