n = int(raw_input())

def check_all(value):
    return value.find("-") == -1

def inverted(string):
    placeholder = ""
    for i in string:
        if i == '+':
            placeholder += '-'
        else:
            placeholder += '+'
    return placeholder

def flip(string, start, count):
    if len(string) - start < count:
        return ""
    return string[:start] + inverted(string[start:start+count]) + string[start+count:]

for i in xrange(n):
    string, count = raw_input().split(" ")
    count = int(count)
    counter = 0
    while True:
        if check_all(string):
            break
        string = flip(string,string.find('-'),count)
        counter += 1
    if string != "":
        print "Case #{}: {}".format(i+1, counter)
    else:
        print "Case #{}: IMPOSSIBLE".format(i+1)