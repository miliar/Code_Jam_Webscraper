import sys

def is_palindrome( int_in_question) :
   # Return true if the number is a palindrome in base 10   
   # Change the number into a string and then a list.
   as_list_of_chars = list( str( int_in_question))
   # Copy the list and reverse it.
   reversed_list_of_chars = list( as_list_of_chars)
   reversed_list_of_chars.reverse( )
   # True if the list of chars is palindromic.
   return as_list_of_chars == reversed_list_of_chars



input_data = sys.stdin.readlines()

tests = int(input_data[0])

for itest in xrange(0, tests):
   cur_line = input_data[itest+1].split()
   minval = int(cur_line[0])
   maxval = int(cur_line[1])

   npalins = 0
   for i in xrange(1, maxval+1):
      if is_palindrome(i) :
         if is_palindrome(i * i) :
            if (i*i) <= maxval and (i*i) >= minval:
            #print( i, i * i)
               npalins += 1;
   out_line = "Case #"+str(itest+1)+": "+str(npalins)
   print out_line
