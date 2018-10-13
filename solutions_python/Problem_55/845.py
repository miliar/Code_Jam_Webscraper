'''
Created on May 8, 2010

@author: Jason
'''

import sys
import os

class RollerCoaster():
    def __init__(self, capacity, runs, queue):
        ''' Roller Coaster Constructor'''
        self.available = capacity
        self.capacity = capacity
        self.runs = runs
        self.queue = queue.split()
        self.on_coaster = []
        self.revenue = 0
        self.run()
    
    def load_group(self, group_size):
        ''' Load the group on to the Roller Coaster and calculate the revenue it earns '''
        self.revenue = self.revenue + int(group_size)
        self.on_coaster.append(group_size)
        self.queue.pop(0)
        self.available = self.available - group_size
    
    def group_fit(self, group_size):
        ''' Tries to add the next group to the coaster, True if loaded, False if not '''
        if group_size <= self.available:
            return True
        return False
    
    def unload_coaster(self):
        ''' Add the groups that rode the coaster to the end of the queue '''
        for group in self.on_coaster:
            self.queue.append(group)
        self.on_coaster = []
    
    def run(self):
        ''' Run the roller coaster '''
        while self.runs > 0:
            run_queue = tuple(self.queue)
            for group in run_queue:
                if self.group_fit(int(group)):
                    self.load_group(int(group))
                else:
                    break
            self.unload_coaster()
            self.available = self.capacity
            self.runs = self.runs - 1
                    
out_file = "output.txt"

def output(num, value):
    ''' Output the result of the case to the end of the output file '''
    global out_file
    file = open(out_file, 'a')
    file.write("Case #%s: %s\n" % (num, value))
    file.close()

if __name__ == '__main__':
    if os.path.exists(out_file):
        os.remove(out_file)
    in_file = sys.argv[1]
    file = open(in_file, 'r')
    cases = int(file.readline())
    for case in range(cases):
        runs, capacity, groups = file.readline().split()
        queue = file.readline()
        coaster = RollerCoaster(int(capacity), int(runs), queue)
        output(case+1, coaster.revenue)
    file.close()