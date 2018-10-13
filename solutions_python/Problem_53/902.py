# -*- coding: utf-8 -*-
import math
filename = "A-small-attempt1.in"

class Snapper:
    def __init__(self, root=False):
        self.state = False
        self.power = False
        self.root = root
        if root:
            self.power=True

    def set_power(self, left_snapper):
        self.power = left_snapper.enable_to_light()

    def snap(self, left_snapper=None):

        if self.root or self.power:
            self.state = not self.state

        if not self.root:
            self.set_power(left_snapper)
##    def has_valid_left_snapper(self, left_snapper):
##        self.power = self.root or  left_snapper.enable_to_light()
##        if left_snapper.power:
##            return True
##        else:
##            return False

    def enable_to_light(self):
        return self.power and self.state

    def __str__(self):
        return 'state: %s, power: %s, root: %s' % (self.state, self.power, self.root)

def read_T():
    f = open(filename, "r")
    T = int(f.readline().strip())
    f.close()
    return T

def convert2int_tuple(str_list):
    result = []
    for s in str_list:
        result.append(int(s))
    return tuple(result)

def read_question2(length):

    f = open(filename, "r")
    T = f.readline().strip()

    nums = []

    for i in range(length):
        n = convert2int_tuple(f.readline().strip().split(" "))
        nums.append(n)

    f.close()

    return nums

def snap_all(snappers):
    snappers[0].snap()
    #print snappers[0]
    for i in range(len(snappers)-1):
        snappers[i+1].snap(snappers[i])
        #print snappers[i+1]

def print_all(snappers):
    for s in snappers:
        print s

T = read_T()
nk = read_question2(T)
results = []
for i in range(T):
    data = nk[i]
    root = Snapper(root=True)
    snappers = []
    snappers.append(root)
    for j in range(data[0]-1):
        snappers.append(Snapper())
    for i in range(data[1]):
        snap_all(snappers)
    #print snappers[-1].enable_to_light()
    r = snappers[-1].enable_to_light()
    results.append(r)

f = open("Output2.txt", "w")
for i in range(len(results)):
    if results[i]:
        r_str = 'ON'
    else:
        r_str = 'OFF'
    f.write("Case #" + str(i+1) + ": " + r_str + "\n")
f.close()


##i = 0
##data = nk[i]
##root = Snapper(root=True)
##snappers = []
##snappers.append(root)
##for j in range(data[0]-1):
##    snappers.append(Snapper())