'''
Created on May 7, 2010

@author: Jason
'''
import sys

class Snapper(object):
    def __init__(self):
        self.isOn=False
        self.power=False
        self.prev=None
        self.next=None
    
#    def toggle_power(self):
#        if self.power:
#            self.power = False
#        else:
#            self.power = True
    
    def toggle_isOn(self):
        if self.isOn:
            self.isOn = False
        else:
            self.isOn = True
    
if __name__ == '__main__':
    file = sys.argv[1]
    input_file = open(file, 'r')
    input_lines = input_file.readlines()
    input_file.close()
    input_count = int(input_lines[0])
    for input in range(1,input_count+1):
        snappers = []
        num_snappers, num_snaps = input_lines[input].split()
        num_snappers = int(num_snappers)
        num_snaps = int(num_snaps)
        for i in range(num_snappers):
            snappers.append(Snapper())
            snappers[i].num = i
            if i <= num_snappers - 1 and snappers[i].num > 0:
                snappers[i].prev = snappers[i-1]
                snappers[i-1].next = snappers[i]
            elif snappers[i].num == 0:
                snappers[0].power = True
        for j in range(num_snaps):
            snappers.reverse()
            # Determin On state
            for snapper in snappers:
                if snapper.power:
                    snapper.toggle_isOn()
            snappers.reverse()
            # Determine Power state
            for snapper in snappers:
                if snapper.prev is not None:
                    if snapper.prev.isOn and snapper.prev.power:
                        snapper.power = True
                    else:
                        snapper.power = False
        fname = "output.txt"
        file = open(fname,'a')
        if snappers[-1].power and snappers[-1].isOn:
            state = "ON"
        else:
            state = "OFF"
        out = "Case #%s: %s\n" % (input, state)
        file.write(out)
        file.close
                
                 

    
    
        