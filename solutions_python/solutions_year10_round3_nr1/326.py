#!/usr/bin/python

def check(w, wires):
    for wire in wires:
        if w[0] > wire[0] and w[1] < wire[1]:
            return 1
        elif w[0] < wire[0] and w[1] > wire[1]:
            return 1

    return 0

def process():
    wires = []

    num = 0

    numWires = int(raw_input())
    for i in range(numWires):
        input = raw_input()
        elements = input.split()

        w = [int(elements[0]), int(elements[1])]
        num += check(w, wires)
        wires.append(w)

    return num

if __name__ == "__main__":
    numInputs = int(raw_input())

    for i in range(numInputs):
        print "Case #" + repr(i + 1) + ": " + repr(process())

# vim: set ts=4 sw=4 et:
