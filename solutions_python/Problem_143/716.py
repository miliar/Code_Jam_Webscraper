def solve(fname):
    output = open("output2.txt", "w+")

    with open(fname, "r") as f:
        number_of_cases = int(f.readline())

        ''' solve problem here '''

        for i in xrange(number_of_cases):
            game_info = f.readline().strip().split(" ")
            a, b, k = int(game_info[0]), int(game_info[1]), int(game_info[2])

            number_of_wins = 0
            for r in xrange(a):
              for j in xrange(b):
                if r & j < k:
                  number_of_wins += 1

            output.write("Case #{}: {}\n".format(i+1, number_of_wins))

# solve("input2.txt")
solve("input2.in")
