# done
def solved(pancakes):
    for i in pancakes:
        if i == '-':
            return False
    return True

# done
def all_equal(pancakes):
    npancakes = len(pancakes)
    x = pancakes[0]

    for p in pancakes:
        if p != x:
            return False
    return True

def count_negatives(pancakes):
    count = 0
    for p in pancakes:
        if p == '-':
            count+=1
    return count

def solvable(pancakes, flippersize):
    print("We've got this pancakes {} and flippersize {}".format(pancakes, flippersize))
    npancakes = len(pancakes)

    if npancakes == flippersize:
        return all_equal(pancakes)

    x = npancakes/2

    if x < flippersize:
        # flipper is bigger than half of pancakes
        # O flipper cobre mais de metade das panquecas

        nonflipped = npancakes - flippersize

        firstblock = nonflipped
        secondblock = nonflipped-2*nonflipped

        togetherforever = pancakes[firstblock:secondblock]
        if all_equal(togetherforever) and all_equal(pancakes[:firstblock]) and all_equal(pancakes[secondblock:]):
            if togetherforever[0] == '+':
                if pancakes[0] == pancakes[-1]:
                    return True
            elif pancakes[0] != pancakes[-1]:
                return True
    else:
        # flipper is smaller than or equal to half of pancakes

        # theory, the number of pancakes to flip must be a multiple of the size of the flipper

        return True
    return False

def flipone(p):
    if p == '+':
        return '-'
    else:
        return '+'

def flip(pancake, start, flippersize):
    flipped = ""
    for i in range(0, flippersize):
        flipped += flipone(pancake[start+i])
    return flipped


def flipper(pancakes, start, flippersize):
    pancakes = pancakes[:start] + flip(pancakes, start, flippersize) + pancakes[(start + flippersize):]
    return pancakes

def first_negative(pancakes):
    for i in range(0, len(pancakes)):
        if pancakes[i] == '-':
            return i
    return -1

def solvable2(pancakes, flippersize):
    i = first_negative(pancakes)
    if i > len(pancakes)-flippersize or i == -1:
        return False
    return True

def solve(pancakes, flippersize):
    i = first_negative(pancakes)
    return flipper(pancakes, i, flippersize)

def main():
    # read number of tests
    ntests = int(input())

    for t in range(0, ntests):
        # read grill and flippersize
        pancakes, flippersize = input().split(" ")
        flippersize = int(flippersize)

        flips = 0
        issolved = solved(pancakes)
        issolvable = solvable2(pancakes, flippersize)
        while issolvable and not issolved:

            pancakes = solve(pancakes, flippersize)
            flips+=1

            # check if solved or still solvable
            issolved = solved(pancakes)
            issolvable = solvable2(pancakes, flippersize)

        if issolved:
            print("Case #{}: {}".format(t+1, flips))
            continue
        if not issolvable:
            print("Case #{}: IMPOSSIBLE".format(t+1))

if __name__ == '__main__':
    main()
