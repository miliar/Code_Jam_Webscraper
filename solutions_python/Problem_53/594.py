#! /usr/bin/python
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

def initialize_snappers(n):
    snappers = [{'state': False, 'input': True, 'output': False}]
    for i in xrange(1, n):
        snappers.append({'state': False,
                            'input': snappers[i-1]['output'],
                            'output': False})
    return snappers

def togglestate(data, n):
    data[n]['state'] = not(data[n]['state'])
    return

def setoutput(data, n):
    if n == 0:
        data[0]['output'] = data[0]['state']
    else:
        data[n]['input'] = data[n-1]['output']
        data[n]['output'] = data[n]['state'] and data[n]['input']
    return

def snap(data, n):
    togglestate(data, 0)
    setoutput(data, 0)

    for i in xrange(1, n):
        if data[i]['input']:
            togglestate(data, i)
        setoutput(data, i)
    return

def display(data, n):
    for i in xrange(n):
        print "(%d, %d, %d) -->" % (data[i]['input'],
                                 data[i]['state'],
                                 data[i]['output']),
    print

def do_smart_work(n, k):
    if (k + 1) % (2<<(n-1)) == 0:
        return "ON"
    else:
        return "OFF"

def do_hard_work(n, k):
    snappers = initialize_snappers(n)
    for i in xrange(k):
        snap(snappers, n)
##         print "Step %d: " % (i+1),
##         display(snappers, n)
##         pp(snappers)
##         print snappers[1]['input']
    if snappers[n-1]['output']:
        return "ON"
    else:
        return "OFF"

def do_work(n, k):
    print do_hard_work(n, k), do_smart_work(n, k)

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    testcases = int(lines[0])
    for line in xrange(1, testcases+1):
        n, k = map(int, lines[line].split())
##         print "n: %d, k: %d" % (n, k)
        print "Case #%d: " % (line),
        do_work = do_smart_work
        print do_work(n, k)

if __name__ == '__main__':
    main()
