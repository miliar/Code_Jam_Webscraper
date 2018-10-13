import sys

def solver(audienceMap):
    running_sum = 0
    add_friends = 0

    for i, nsi in enumerate(audienceMap):
        # if running_sum < i:
        #     number_of_friend_to_add = i - running_sum
        #     add_friends += number_of_friend_to_add
        #     running_sum += number_of_friend_to_add
        #     # print("Branch 1")
        # elif nsi == 0 and running_sum == i:
        if nsi == 0 and running_sum == i:
            add_friends += 1
            running_sum += 1
            # print("Branch 2")
        else:
            running_sum += nsi
            # print("Branch 3")

        # print("post nsi = {0}, i = {1}".format(nsi, i))
        # print("post add_friends = {0}".format(add_friends))
        # print("post running_sum = {0}".format(running_sum))


    return add_friends

def parse(inputFile):
    with open(inputFile) as f:
        indata = f.read().splitlines()

        # print("N = {0}".format(indata[0]))

        audienceMaps = []
        for l in indata[1::]:
            smax, smap = l.split()
            final_smap = [int(c) for c in list(smap)]

            audienceMaps.append(final_smap)
        return audienceMaps

def main(argv):
    audienceMaps = parse(argv)

    sols = map(solver, audienceMaps)

    for i, sol in enumerate(sols):
        print("Case #{0}: {1}".format(i+1, sol))

if __name__ == '__main__':
    main(sys.argv[1])

