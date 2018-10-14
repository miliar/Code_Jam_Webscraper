def first_method(intervals):
    total = []
    rate = 0
    for i in range(len(intervals)-1):
        eaten = intervals[i] - intervals[i+1]
        if eaten > 0:
            total.append(eaten)
        if eaten > rate:
            rate = eaten
    return rate, sum(total)

def second_method(rate, intervals):
    total = []
    #rate = abs(intervals[len(intervals)-2] - intervals[len(intervals)-1])
    for i in range(len(intervals)-1):
        if intervals[i] <= rate:
            total.append(intervals[i])
        else:
            total.append(rate)
    return sum(total)


input = open("input.txt", "r")

cases = int(input.readline())

with open('large_results.txt', 'w') as results:
    for case in range(cases):
        num_intervals = int(input.readline())
        intervals = [int(x) for x in input.readline().split()]
        rate, first_result = first_method(intervals)
        second_result = second_method(rate, intervals)
        to_write = "Case #%i: %s %s" % (case+1, first_result, second_result)
        print to_write
        results.write(to_write + "\n")

input.close()