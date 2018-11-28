# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="alvaro"
__date__ ="$May 7, 2010 7:15:53 PM$"

import re;

class Snapper:
    def process_entry(self):
        t = 2**self.N-1;
        print 'Case #%d:' % self.entry,
        if t is self.K & t:
            print 'ON';
        else: print 'OFF';
        
    def read_entry(self):
        if self.next < len(self.input):
            self.entry = self.next;
            pattern = '^(\d+) (\d+)$';
            matches = re.match(pattern, self.input[self.entry]);
            self.N = int(matches.group(1));
            self.K = int(matches.group(2));
            self.next = self.next + 1;
        else: return False;
        return True;
    def read_header(self):
        self.entries = int(self.input[0]);
        self.next = 1;
    def read_file(self):
        f = open('input');
        self.input = f.readlines();
    def __init__(self):
        self.read_file();
        self.read_header();
        while self.read_entry():
            self.process_entry();


if __name__ == "__main__":
    print Snapper();
