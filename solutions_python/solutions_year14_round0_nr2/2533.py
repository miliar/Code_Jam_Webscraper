import sys


def best_time(in_line):
    temp = in_line.split(' ')
    cur_rate = 2
    cost =  float(temp[0])
    increase = float(temp[1])
    goal = float(temp[2])
    cur_best = goal / cur_rate
    cur_penalty = 0.0
    while(True):
        new_rate = cur_rate + increase
        new_penalty = cur_penalty + (cost / cur_rate)
        new_best = goal / new_rate + new_penalty
        if new_best > cur_best: 
            return cur_best
        else:
            cur_rate = new_rate
            cur_best = new_best
            cur_penalty = new_penalty


def main():
    input_name = sys.argv[1]
    fin = open(input_name, 'r')

    num_cases = int (fin.readline())
    for i in range(num_cases):
        line = fin.readline();
        result = round(best_time(line), 7)
        print("Case #{}: {}".format((i+1), result))

if __name__ == '__main__':
    main()
