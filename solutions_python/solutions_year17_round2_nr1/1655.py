##input = open('A-sample-input.txt', 'r')
##output = open('A-sample-output.txt', 'w')

input = open('A-small-attempt0.in', 'r')
output = open('A-small.out', 'w')

##input = open('A-large.in', 'r')
##output = open('A-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(d, n, positions, speeds):
    times_to_catch_up = [0] * (n+1)
    catch_up_points = [d] * (n+1)
    times_after_catch_up = [0] * (n+1)
    print 'speeds', speeds
    for i in range(n, 0, -1):
        print 'i=', i
        if i == n:
            times_to_catch_up[i] = (d - positions[i]) * 1.0 / speeds[i]
            not_caught_up = [i, (d - positions[i]) * 1.0 / speeds[i]]
            print times_to_catch_up[i]
        else:
            catch_up_points[i] = positions[i]
            print catch_up_points
            caught_up = False
            for j in range(i+1, n+1, 1):
                i_time_to_catch_up_point = (catch_up_points[j] - positions[i]) * 1.0 / speeds[i]
                print i,'trying to catch up to', j
                print 'time it takes to catch up=', i_time_to_catch_up_point
                if i_time_to_catch_up_point <= times_to_catch_up[j]:
                    caught_up = True
                    previous_catch_up_point = catch_up_points[j-1]
                    time_to_previous_catch_up_point = (previous_catch_up_point - positions[i]) * 1.0 / speeds[i]
                    time_to_catch_up = (positions[j] - previous_catch_up_point) * 1.0 / (speeds[i] - speeds[j]) + time_to_previous_catch_up_point
                    catch_up_points[i] = positions[i] + speeds[i] * time_to_catch_up
                    times_to_catch_up[i] = time_to_catch_up
            if not caught_up:
                not_caught_up = [i, (d - positions[i]) * 1.0 / speeds[i]]
##    print not_caught_up
##    print not_caught_up[0], 'position of not caught up'
##    print 'tiems to catch up', times_to_catch_up
    total_time = not_caught_up[1] + sum(times_to_catch_up[:not_caught_up[0]])
    total_time = not_caught_up[1]
    return d * 1.0 / total_time
    
                

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        d, n = read_ints()
        positions = []
        speeds = []

        for i in range(n):
            position, speed = read_ints()
            if len(positions) == 0:
                positions.append(position)
                speeds.append(speed)
            else:
                if position < positions[0]:
                    positions.insert(0, position)
                    speeds.insert(0, speed)
                else:
                    positions.append(position)
                    speeds.append(speed)
        positions.insert(0, 0)
        speeds.insert(0, 0)
##        if case == 56:
        solution = solve(d, n, positions, speeds)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
