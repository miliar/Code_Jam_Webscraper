# Task B - Train Timetable
# Written in Python

testing = False

def convert(time):
    hour, minute = [int(num) for num in time.split(':')]
    time = hour*60+minute
    return time

def timetable(turn, departs, arrivals):
    departs = [[convert(time), True] for time in departs]
    arrivals = [[convert(time)+turn, False] for time in arrivals]
    times = departs
    times.extend(arrivals)
    times.sort()
    times = [time[1] for time in times]
    current = 0
    count = 0
    for time in times:
        if time:
            if current:
                current -= 1
            else:
                count += 1
        else:
            current += 1
    return str(count)

def train(data):
    turn, from_a, from_b = data
    output = timetable(turn, [time[0] for time in from_a], [time[1] for time in from_b])
    output += ' ' + timetable(turn, [time[0] for time in from_b], [time[1] for time in from_a])
    return output

def main():
    if testing:
        file_name = 'B-test'
    else:
        file_name = raw_input('Enter file: ')
    try:
        f = open(file_name + '.in', 'rU')
    except:
        print 'File "' + file_name + '.in" does not exist!'
    else:
        inputs = ''
        data = []
        for line in f:
            inputs += line
            if line.strip('\n') != '':
                data.append(line.strip('\n'))
        f.close()
        output = []
        count = int(data[0])
        num = 1
        for i in xrange(1, count+1):
            current = [int(data[num])]
            from_a, from_b = [int(j) for j in data[num+1].split()]
            num += 2
            current.append([time.split() for time in data[num:num+from_a]])
            num += from_a
            current.append([time.split() for time in data[num:num+from_b]])
            num += from_b
            output.append('Case #%s: %s' % (i, train(current)))
        output = '\n'.join(output)
        if testing:
            print output
        else:
            print inputs
            print output
            f = open(file_name + '.out', 'w')
            f.write(output)
            f.close()

main()
