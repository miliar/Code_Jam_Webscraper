#!/usr/bin/python

import glob
import sys
import os
import re
import filecmp

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
    a1 = None
    s1r1 = None
    s1r2 = None
    s1r3 = None
    s1r4 = None
    a2 = None
    s2r1 = None
    s2r2 = None
    s2r3 = None
    s2r4 = None

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

        elif a1 is None:

            a1 = int (line)

            print ("    a1 {0}" . format (a1))

        elif s1r1 is None:

            list = line . split (" ")
            s1r1 = []

            for item in list:

                s1r1 . append (int (item))

            print ("    s1r1 {0}" . format (" " . join (map (str, s1r1))))
            
        elif s1r2 is None:

            list = line . split (" ")
            s1r2 = []

            for item in list:

                s1r2 . append (int (item))

            print ("    s1r2 {0}" . format (" " . join (map (str, s1r2))))

        elif s1r3 is None:

            list = line . split (" ")
            s1r3 = []

            for item in list:

                s1r3 . append (int (item))

            print ("    s1r3 {0}" . format (" " . join (map (str, s1r3))))

        elif s1r4 is None:

            list = line . split (" ")
            s1r4 = []

            for item in list:

                s1r4 . append (int (item))

            print ("    s1r4 {0}" . format (" " . join (map (str, s1r4))))

        elif a2 is None:

            a2 = int (line)

            print ("    a2 {0}" . format (a2))

        elif s2r1 is None:

            list = line . split (" ")
            s2r1 = []

            for item in list:

                s2r1 . append (int (item))

            print ("    s2r1 {0}" . format (" " . join (map (str, s2r1))))
            
        elif s2r2 is None:

            list = line . split (" ")
            s2r2 = []

            for item in list:

                s2r2 . append (int (item))

            print ("    s2r2 {0}" . format (" " . join (map (str, s2r2))))

        elif s2r3 is None:

            list = line . split (" ")
            s2r3 = []

            for item in list:

                s2r3 . append (int (item))

            print ("    s2r3 {0}" . format (" " . join (map (str, s2r3))))

        elif s2r4 is None:

            list = line . split (" ")
            s2r4 = []

            for item in list:

                s2r4 . append (int (item))

            print ("    s2r4 {0}" . format (" " . join (map (str, s2r4))))

          # Solve

            v1 = [s1r1, s1r2, s1r3, s1r4] [a1 - 1]
            v2 = [s2r1, s2r2, s2r3, s2r4] [a2 - 1]

            solve (out_file, case, v1, v2)

          # Reset

            case += 1
            #t = None
            a1 = None
            s1r1 = None
            s1r2 = None
            s1r3 = None
            s1r4 = None
            a2 = None
            s2r1 = None
            s2r2 = None
            s2r3 = None
            s2r4 = None

  # Check the output file

    check (out_file)

def solve (out_file, case, v1, v2):

    print ("    Solve")
    print ("    v1 {0}" . format (" " . join (map (str, v1))))
    print ("    v2 {0}" . format (" " . join (map (str, v2))))
    print ("")

    file = open (out_file, "a+")

    count = 0
    answer = "Volunteer cheated!" # Assumption

    for v in v1:
    
        if v in v2:
        
            print ("    **** {0} in v2" . format (v))
        
            count += 1
            answer = v if count == 1 else "Bad magician!"
            
  # Compose the result and write it to the output file

    result = "Case #{0}: {1}" . format (case, answer)
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
