'''
Created on Apr 8, 2016

@author: Thomas
'''
import re
import sys

def flip_stack(s):
    '''flip the provided stack/substack of pancakes'''
    
    # replace with temporary character
    s = s.replace('+', 't')
    # switch - for +
    s = s.replace('-', '+')
    # switch + for -
    s = s.replace('t', '-')
    
    return s

def flip(stack, k):
    start = stack.find("-")
    end = (start + k)
    past_end = end - (len(stack) - 1)
    
    if past_end > 0:
        start -= past_end
        end -= past_end    
    
    s_sub = stack[start:end]
    stack = stack[:start] + flip_stack(s_sub) + stack[end:]
    return stack

def flip_decision(stack, k, num_flips=0):
    '''decide what to flip, do the flip, and continue until all happy faces'''
    print stack
    if "-" in stack:
        # Not all Happy Face Pancakes          
        if ('-' * k) in stack:
            num_occ = stack.count('-' * k)
            stack = stack.replace(('-' * k), ('+' * k))
            num_flips += num_occ
                    
        elif stack.find("-") >= 0:
            print "pre" + stack
            stack = flip(stack, k)
            num_flips += 1
            print "pos" + stack

        if num_flips > len(stack):
            return "IMPOSSIBLE"
            
        return flip_decision(stack, k, num_flips)
    
    else:
        return num_flips 
        

if __name__ == '__main__':
    out = {}

    with open("A-small-attempt2.in", 'rb') as f:
        lines = f.readlines()[1:]
        for idx,line in enumerate(lines):
            line = line.rstrip()
            pancakes = re.search("[+-]+", line).group(0)
            k = int(re.search("[0-9]+", line).group(0))

            print line + str("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            num_flips = flip_decision(pancakes, k)
            out[idx+1] = num_flips


    with open("output.out", 'w') as f:
        f.write("")
        for key, val in out.iteritems():
            line = "Case #" + str(key) + ": " + str(val) + "\n"
            f.write(line)