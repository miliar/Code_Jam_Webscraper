#!/usr/bin/python

import glob
import sys
import os
import re
import filecmp
import time

def main ():

  # Get the name (sans extension) of the app,
  # which is also the name of the data.
  
    app = sys . argv [0]
    app = re . sub (r"^(.+)\.py$", r"\1", app)

  # For each input file of the same name as the app:

    for in_file in glob . glob ("{0}-*.in" . format (app)):
    
      # Determine the name of the output file
    
        out_file = re . sub (r"^(.+)\.in", r"\1.out", in_file)
    
      # If the output file does not already exist
    
        if not os . path . isfile (out_file):
        
          # Process the input file
            
            process (out_file, in_file)

def process (out_file, in_file):

    print ("Procesing {0}" . format (in_file))

    case = 1
    t = None
    c = None
    f = None
    x = None

  # Read the input file

    file = open (in_file, "r")
    text = file . readlines ()
    file . close ()

  # Lines

    for line in text:

        line = line . strip ()

        if t is None:

            t = int (line)

            print ("    t {0}" . format (t))

        elif c is None:

            cfx = line . split (" ")
            
            c = float (cfx [0])
            f = float (cfx [1])
            x = float (cfx [2])

            print ("    c {0}" . format (c))
            print ("    f {0}" . format (f))
            print ("    x {0}" . format (x))

          # Solve

            solve (out_file, case, c, f, x)

          # Reset

            case += 1
            #t = None
            c = None
            f = None
            x = None

  # Check the output file

    check (out_file)

def solve (out_file, case, c, f, x):

    file = open (out_file, "a+")

    free = 2 # Cookies per second
    earn = 0 # Cookies per second from farming
    best = None # Seconds
    done = False
    time_to_get_farms = 0
    
    while not done:
        
        time_to_finish = x / (free + earn)
        total_time = time_to_get_farms + time_to_finish
    
        if best == None:
        
            best = total_time
            
        elif total_time < best:
        
            best = total_time
            
        else:
        
            done = True
            
        if not done:
        
          # Buy a farm

            time_to_get_farms += c / (free + earn)
            earn += f
            
  # Compose the result and write it to the output file

    result = "Case #{0}: {1}" . format (case, "%.7f" % (best))
    file . write ("{0}\n" . format (result))
    print ("    {0}" . format (result))
    print ("")

  # Close the output file

    file . close ()

def check (out_file):

  # Determine the name of the solution file

    solution_file = re . sub (r"^(.+)\.out", r"\1.solution", out_file)

  # If the solution file exists

    if os . path . isfile (solution_file):
    
      # Compare the output file with the solution file
    
        if filecmp . cmp (out_file, solution_file):
        
            print ("    Check: Correct")
            
        else:
        
            print ("    Check: Incorrect")
        
    else:

      # No solution file
        
        print ("    Check: Unknown")

if __name__ == "__main__":

    main ()
    exit (0)
