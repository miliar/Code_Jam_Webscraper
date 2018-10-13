# Problem 1: Oversized Pancake Flipper
# CodeJam 2017 Qualification
# By: Richard Salas Chavez

def main():
    input = open('A-large (1).in','r')
    output = open('A-output-large.txt', 'w')

    test_cases = int(input.readline()) # number of test cases
    print test_cases
    case = 1
    # loop through cases
    while(case <= test_cases):
        line = input.readline().strip()
        parts = line.split(' ')
        pancakes, flipper = parts[0], parts[1]
        flipper = int(flipper)
        num_pancakes = len(pancakes)
        print pancakes
        print num_pancakes
        print

        working = True
        moves = 0 # how many moves/flips need to be made
        while (working):
            happy = 0

            # check how many pancakes are happy
            for c in pancakes:
                if c == '+':
                    happy += 1
            if happy == num_pancakes: # if they are all happy then you're done
                output.write("Case #%i: %i\n" % (case, moves))
                break

            rem_panks = ''
            # if the first pancake is happy look for the next unhappy one
            if pancakes[0] == '+':
                parts = pancakes.split('+-', 1)
                pancakes = str(parts[0]) + '+'
                if len(parts) > 1:
                    rem_panks = '-' + str(parts[1])
            # if the first pancake is not happy then look for the first unhappy one
            else:
                parts = pancakes.split('-+', 1)
                pancakes = str(parts[0]) + '-'
                if len(parts) > 1:
                    rem_panks = '+' + str(parts[1])

            # up to here is good, just need to fix everything below this
            # more specifically need to flip the pancakes correctly and check impossible cases
            if pancakes[0] == '-':
                moves += 1
                new_pancake = ''
                pancakes += rem_panks
                for i, p in enumerate(pancakes): # flip first few pancakes
                    if i < flipper:
                        if p == '+':
                            new_pancake += '-'
                        else:
                            new_pancake += '+'
                    else:
                        new_pancake += p
                pancakes = new_pancake
            else:
                if len(rem_panks) < flipper:
                    if num_pancakes - len(rem_panks) % flipper != 0:
                        output.write("Case #%i: IMPOSSIBLE\n" % (case))
                        break # impossible to get them all happy
                    else: # flip first few pancakes
                        moves += 1
                        pancakes += rem_panks
                        new_pancake = ''
                        for i, p in enumerate(pancakes):
                            if i < flipper:
                                if p == '+':
                                    new_pancake += '-'
                                else:
                                    new_pancake += '+'
                            else:
                                new_pancake += p
                        pancakes = new_pancake

                else : # flip remaining n pancakes # if first one is sad flip it
                    moves += 1
                    new_rem_panks = ''
                    if len(rem_panks) > 0:
                        for i,p in enumerate(rem_panks):
                            if i < flipper:
                                if p == '+':
                                    new_rem_panks += '-'
                                else:
                                    new_rem_panks += '+'
                            else:
                                new_rem_panks += p
                    pancakes += new_rem_panks
            print pancakes
        case += 1

    input.close()
    output.close()
main()