# Play with it!
# 
# In the interative python shell,
# do
#   >>> from interactive_pancakes import *
#   >>> p = Pancakes('+++---+---+-+-+++--+++', 3)
#   >>> p
#   
#   >>> print p
#   
#   >>> p.play()
#   
#   >>> p.play()
#   
#   ...

# pancakes and flipper solution
class Pancakes(object):
    
    # please don't change these four constants
    HAPPY = 0
    DOWN = 1
    
    HAPPY_CHAR = '+'
    DOWN_CHAR = '-'
    
    R = reversed # = lambda o : o
    
    def __init__(self, pancakes, flipper_length):
        
        assert 2 <= flipper_length <= pancakes
        
        self.N = len(pancakes)
        self.bin = self._bin_complex(pancakes) # only called once
        self.f = self._get_flipper_bin(flipper_length)
        self.m = 0 # number of flips so far
        
        self.success = False
        self.impossible = False
    
    def _bin_complex(self, pancakes):
        """
          '+--+-' will be stored as
        0b101101
          ^
          |
        this leading one is there to preserve leading zeros
        """
        
        pancakes = self.R(pancakes)
        
        B = 2
        num = 1 # the leading one is not part of the encoding of happy and down pancakes,
                # but without it, the leading zeros would disappear
        
        for char in pancakes:
            num *= B
            if char is self.HAPPY_CHAR:
                # num += self.HAPPY # NOP when HAPPY == 0
                pass
            elif char is self.DOWN_CHAR:
                num += self.DOWN
            else:
                raise ValueError()
        return num
    
    def _bin_simple(self):
        """
        Returns self.bin as a binary string without the leading one.
        If self.bin == '0b1001', then returns '001'
        """
        return bin(self.bin)[3:]
    
    def _get_flipper_bin(self, flipper_length):
        """
        for flipper_length == 3
        returns 0b111
        
        for flipper_length == 8
        returns 0xff == 0b11111111
        
        etc...
        """
        
        assert flipper_length > 0
        
        B = 2
        f = 0
        for i in range(flipper_length):
            f *= B
            f += 1
        return f
    
    # n := next
    def n(self):
        
        if self.success:
            print 'We have already succeeded in {} moves.'.format(self.m)
            return
        if self.impossible:
            print 'It has already been shown to be IMPOSSIBLE.'
            return
        
        while LSB(self.bin) == self.HAPPY:
            self.bin >>= 1
        
        # -1 to account for the leading one
        bin_simple = int(self._bin_simple())
        if bit_length( bin_simple ) < bit_length(self.f):
            print "IMPOSSIBLE"
            self.impossible = True
            return
        
        print self
        
        # apply the flipper
        self.bin ^= self.f
        
        self.m += 1
        
        bin_simple = int(self._bin_simple())
        if bin_simple == 0:
            # recall that the leading one should be ignored
            print "SUCCESS, all the pancakes are HAPPY in {} flips.".format(self.m)
            self.success = True
            return
    
    # play
    def play(self):
        self.n()
        print self
    
    # bin(self.bin)[3:] skips over the '0b1'
    #                                     ^
    #                                     |
    #                             the leading one
    
    def __str__(self):
        r = lambda b : self.HAPPY_CHAR if int(b) == self.HAPPY else self.DOWN_CHAR
        
        s = self._bin_simple()
        #
        s = map( r, s )
        s = ''.join(s)
        #
        s = s.ljust(self.N, '.')
        #
        s = self.R(s)
        s = ''.join(s)
        return s
        
    def __repr__(self):
        s = self._bin_simple()
        #
        s = s.ljust(self.N, '.')
        #
        s = self.R(s)
        s = ''.join(s)
        return s


def LSB(bin):
    LSB_mask = 0b1 # least significant bit mask
    return bin & LSB_mask

def bit_length(num):
    return len( bin(num)[2:] )