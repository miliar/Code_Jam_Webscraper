#!/usr/bin/env python

import sys
import logging

INPUT_FILE=file(sys.argv[1])
OUTPUT_FILE=file(sys.argv[1].replace('in', 'out'), 'w')
#OUTPUT_FILE=sys.stdout

class ElementList(list, object):
    
    def __init__(self, combo_dict, opposed_dict):
        self.combo_dict = combo_dict
        self.opposed_dict = opposed_dict
        self.set = set()
    
    def invoke(self, element):
        logging.debug("Trying to append element '%s'", element)
        
        if self.combined(element): return 
        if self.opposed(element): return
        
        self.append(element)
        self.set.update((element,))    
     
    def combined(self, element):
        if not len(self):
            return 
            
        last = self[-1]
        combo = self.combo_dict.get(element, {}).get(last)
        if combo:
            self.pop()
            self.append(combo)
            if last not in self: 
                self.set.remove(last)
            logging.debug('Combined with %s to get %s', last, combo)
            return True
    
    def opposed(self, element):
        opposed_list = self.opposed_dict.get(element, set())
        for o in opposed_list:
            if o in self.set:
                logging.debug("Element '%s' is opposed to %s. Cleaning list.", 
                              element, opposed_list)
                self.clean()
                return True 
            
    def clean(self):
        n = len(self)
        for i in range(n):
            self.pop()
        self.set = set()

    def __repr__(self):
        return '[' + ', '.join(self) + ']' 
           
    def __str__(self):
        return self.__repr__() 

        
def invoke(line):
    line_split = line.split(' ')
    combo_dict = {}
    opposed_dict = {}
    
    c = int(line_split.pop(0))
    for i in range(c):
        e1, e2, e3 = tuple(line_split.pop(0))
        
        combo = combo_dict.get(e1, dict())
        combo.update({e2:e3})
        combo_dict.update({e1: combo})
        
        combo = combo_dict.get(e2, dict())
        combo.update({e1:e3})
        combo_dict.update({e2: combo})
    
    d = int(line_split.pop(0))
    for i in range(d):
        opposed_1, opposed_2 = tuple(line_split.pop(0))
        
        opposed = opposed_dict.get(opposed_1, set())
        opposed.update((opposed_2,))
        opposed_dict.update({opposed_1: opposed})

        opposed = opposed_dict.get(opposed_2, set())
        opposed.update((opposed_1,))
        opposed_dict.update({opposed_2: opposed})
    
    n = int(line_split.pop(0)) 
    
    logging.debug('-' * 50)
    logging.debug('New input: %s', line)
    logging.debug('Invoking Elements: %s', line_split[-1])
    logging.debug('Combo cache: %s', combo_dict)
    logging.debug('Opposed cache: %s', opposed_dict)
    invoke_list = ElementList(combo_dict, opposed_dict)
 
    for e in tuple(line_split.pop(0).strip()):
        invoke_list.invoke(e)
        logging.debug("Current state: %s", invoke_list)

    return invoke_list


def main():
    line_num = 0
    for line in INPUT_FILE:
        if line_num == 0:
            line_num += 1
            continue
         
        invoke_list = invoke(line.strip())
        OUTPUT_FILE.write("Case #%s: %s\n" % (line_num, invoke_list))
        line_num += 1

        
if __name__ == '__main__':
    #logging.root.setLevel(logging.DEBUG)
    main()
