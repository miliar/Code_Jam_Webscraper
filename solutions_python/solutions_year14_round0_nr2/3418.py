"""
CodeJam Qualifications 2014 
Problem B. Cookie Clicker Alpha
author: chris @ sihrc
"""

def readInput(testfile):
    with open(testfile, 'rb') as f:
        lines = list()
        for line in f:
            lines.append(line)
    return lines

def readTestCase(input_line):
    inputs = [float(num) for num in input_line.strip().split()]
    return inputs[0], inputs[1], inputs[2]

def getTimeForFarm(cost_farm, increase, num_farms):
    rate = 2
    time = 0
    for i in xrange(num_farms):
        time += cost_farm/(rate + i * increase)
    return time

def writeAnswerOutputs(output_lines):
    with open("answer.txt", 'wb') as f:
        f.write("\n".join(output_lines))

if __name__ == "__main__":
    lines = readInput("B-small-attempt0.in")
    # lines = readInput("test_input.txt")
    test_cases = int(lines[0].strip())
    cases = []

    for i in xrange(1,test_cases + 1):
        cookies = 0
        rate = 2

        farm_cost,farm_increase,cookie_goal = readTestCase(lines[i])
        prev_time = cookie_goal/rate        
        num_farms = 1
        while (True):
            tFarms = getTimeForFarm(farm_cost, farm_increase, num_farms)
            tGoal = cookie_goal/(rate + num_farms * farm_increase)
            next_time = tFarms + tGoal

            if next_time > prev_time:
                break
            else:
                prev_time = next_time
                num_farms += 1
        cases.append("Case #{0}: {1}".format(i, prev_time))
    writeAnswerOutputs(cases)



