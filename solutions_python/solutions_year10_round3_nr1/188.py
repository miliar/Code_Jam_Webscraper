#!/usr/bin/python
def solve(wires):
    print wires
    inter = 0
    for cur_wire in wires:
        for wire in wires:
            if wire == cur_wire:
                continue
            x = cur_wire[0] < wire[0]
            y = cur_wire[1] > wire[1]
            if (x and y) or (not x and not y):
                inter = inter + 1 

    return inter/2
    

def main():
    """docstring for main"""
    input = open("problem")
    ilines = [l.strip() for l in input.readlines()]
    num_tests = int(ilines[0], 0)
    ans = file("answer", "w")
    line_num = 1
    for test in xrange(num_tests):
        line = ilines[line_num]
        n = [int(x, 0) for x in line.split()]
        line_num = line_num + 1
        wires = []
        for i in xrange(n[0]):
            line = ilines[line_num]
            wires.append([int(x, 0) for x in line.split()])
            line_num = line_num + 1
        x = solve(wires)
        a = "Case #%d: %d\n" % (test + 1, x) 
        ans.write(a)
        print a
    ans.close()

if __name__ == '__main__':
    main()        
