import os


def main():
    with open('in.txt') as f, open('out.txt', 'w') as out:
        num_cases = int(f.readline())
        for case in range(1, num_cases+1):

            cost, rate, goal = tuple([float(x) for x in f.readline().split()])

            cookies = 0.0
            time = 0.0
            remainder = goal
            cur_rate = 2.0
            while (goal/cur_rate) > ((cost)/(cur_rate) + goal/(cur_rate+rate)):
                time += cost/cur_rate
                cur_rate += rate

            time+=goal/cur_rate
                
            out.write('Case #{0}: {1}\n'.format(case, time))

if __name__ == "__main__":
    main()