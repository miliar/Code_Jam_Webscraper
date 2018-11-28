#!/usr/bin/python

from __future__ import print_function
import re
import fileinput
import sys

def main (): # stdin to stdout; stderr for debugging

    lines = []
    l = 0
    
    for line in fileinput . input ():

        lines . append (line . strip ())
        
    cases = int (lines [l])
    l += 1
    
    for case in range (1, cases + 1):

        n = int (lines [l])
        l += 1

        texts = []

        for text in range (0, n):
        
            text = lines [l]
            l += 1
            
            texts . append (text)
        
        number = count_moves (texts)
        
        if number is None:
        
            reply = "Case #{0}: Fegla Won" . format (case)
            print (reply, file = sys . stderr)
            print (reply)

        else:

            reply = "Case #{0}: {1}" . format (case, number)
            print (reply, file = sys . stderr)
            print (reply)        

def count_moves (texts):

    count = None
    
    if get_is_possible (texts):

        count = 0

        codes = get_codes (texts)
        bases = get_bases (codes)
        
        for i in range (0, len (codes)):
        
            for j in range (0, len (codes [i])):
        
                difference = abs (codes [i] [j] ["quantity"] - bases [j] ["quantity"])
                count += difference
                       
    return count
    
def get_is_possible (texts):

    base = re . sub (r'([a-z])\1+', r'\1', texts [0])
    possible = True
    
    for t in range (1, len (texts)):
    
        if re . sub (r'([a-z])\1+', r'\1', texts [t]) != base:
        
            possible = False
            
            break
    
    return possible
    
def get_codes (texts):

    codes = []
    
    for text in texts:
    
        code = []
        
        for character in text:
        
            if len (code) == 0 or code [-1] ["character"] != character:
            
                code . append ({"character": character, "quantity": 1})
            
            else:
            
                code [-1] ["quantity"] += 1
      
        codes . append (code)
    
    return codes
    
def get_bases (codes):

    bases = []
    
    for item in codes [0]:
    
        bases . append ({"character": item ["character"], "quantity": {}})
    
    for code in codes:
        
        for i in range (0, len (code)):
        
            if code [i] ["quantity"] in bases [i] ["quantity"] . keys ():
                
                bases [i] ["quantity"] [code [i] ["quantity"]] += 1
            
            else:
            
                bases [i] ["quantity"] [code [i] ["quantity"]] = 1

    for item in bases:
    
        best_quantity = 0
        best_count = 0
        
        for key in item ["quantity"] . keys ():
    
            if item ["quantity"] [key] > best_count:
            
                best_quantity = key
                best_count = item ["quantity"] [key]
                
        keys = []
                
        for key in item ["quantity"] . keys ():
        
            if item ["quantity"] [key] == best_count:
            
                keys . append (key)

        item ["quantity"] = sorted (keys) [len (keys) // 2]
    
    return bases
    
if __name__ == "__main__":

    main ()
    exit ()
