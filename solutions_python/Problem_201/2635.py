#Author: Carina Claassen

'''
  input: number of stalls, number of num_persons
  output: max num stalls between persons, min number of stalls between persons
'''
def answers(num_stalls, num_persons):

    available_in_a_row = [num_stalls]
    for k in range(num_persons - 1):
        best = max(available_in_a_row)
        available_in_a_row.remove(best)
        available_in_a_row.append(best//2)
        available_in_a_row.append(best - best//2 - 1)
    best = max(available_in_a_row)
    return best//2, best - best//2 - 1


'''
  input: name of input file
  output: the output of the parsed input file
'''
def solution(file_name):

    f = open(file_name)
    f.readline()

    i = 1
    for line in f:
        inputs = line.strip().split(" ")
        x, y = answers(int(inputs[0]), int(inputs[1]))
        print "Case #{}: {} {}".format(i, x, y)
        i += 1


solution("C-small-1-attempt0.in")








