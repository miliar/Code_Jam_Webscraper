# Task A - Saving the Universe
# Written in Python

testing = False

def universe(data):
    count, engines = data
    switches = 0
    current = set()
    for engine in engines:
        if engine not in current:
            if len(current) == count-1:
                switches += 1
                current.clear()
            current.add(engine)
    return switches

def main():
    if testing:
        file_name = 'A-test'
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
            num += current[0]+1
            queries = int(data[num])
            current.append(data[num+1:num+queries+1])
            num += queries+1
            output.append('Case #%s: %s' % (i, universe(current)))
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
