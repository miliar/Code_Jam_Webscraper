# C = Cookie Farm Cost
# F = Cookie Farm Production Rate
# X = Cookie Win Condition

def read_input(file_name):
    with open(file_name, 'r') as input_file:
        input_lines = input_file.readlines()
        cases = int(input_lines[0])
        input_lines = input_lines[1:]

    with open('cookie_output.txt', 'w+') as output:
        for i in xrange(1, cases + 1):
            conditions = input_lines[0].split(' ')
            C = float(conditions[0])
            F = float(conditions[1])
            X = float(conditions[2])
            print C, F, X
            print
            cps = 2
            cookies = 0
            time = 0

            #for i in xrange(0, 8):
            while True:
                time_to_farm = (C)/cps
                t2 = (X)/(cps + F) + time_to_farm + time
                t3 = (X - cookies)/cps + time
                if t3 < t2:
                    break
                else:
                    cps += F
                    time += time_to_farm

            output.write("Case #{0}: {1:.7f}\n".format(i, t3))
            input_lines = input_lines[1:]


read_input('cookie_input.txt')