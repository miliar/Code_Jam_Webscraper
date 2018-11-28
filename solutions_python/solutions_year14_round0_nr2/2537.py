def time_until_goal(goal, cookies, freq):
    return (goal - cookies) / freq
    
if __name__ == '__main__':
    input_file = open('B-large.in')
    output_file = open('B-large.out', 'w')
    
    input = input_file.readline
    print = lambda s: output_file.write(s+'\n')

    cases = int(input())

    for case in range(cases):
        time, cookies, freq = 0, 0, 2
        farm_cost, farm_freq, finish = map(float, input().split())

        while time_until_goal(farm_cost, cookies, freq) + time_until_goal(finish, cookies, freq+farm_freq) < time_until_goal(finish, cookies, freq):
            time += time_until_goal(farm_cost, cookies, freq)
            freq += farm_freq

        time += time_until_goal(finish, cookies, freq)
        
        answer = time
        
        print("Case #{}: {:.7f}".format(case+1, answer))

    output_file.close()
