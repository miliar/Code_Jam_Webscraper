# Task A - Text Messaging Outrage
# Written in Python

testing = False

def text(data):
    data = [[int(num) for num in line] for line in data]
    maximum, available, num = data[0]
    letters = data[1]
    letters.sort()
    letters.reverse()
    key = 0
    level = 1
    count = 0
    for letter in letters:
        if level == maximum+1:
            return 'Impossible'
        count += letter*level
        key += 1
        if key == available:
            key = 0
            level += 1
    return count

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
                data.append(line.strip('\n').split())
        f.close()
        output = []
        count = int(data[0][0])
        for i in xrange(1,count+1):
            output.append('Case #%s: %s' % (i, text([data[i*2-1],data[i*2]])))
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
