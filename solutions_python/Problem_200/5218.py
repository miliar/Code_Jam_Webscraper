# Jonathan Lenart
# 04/08/2017

# 2017 Qualifier Problem B ("Tidy numbers")

# this will only work on the small input size

def is_tidy(number):
   temp = int(number[0])
   for digit in number[1:]:
      int_digit = int(digit)
      if temp > int_digit:
         return False
      temp = int_digit
   return True

def find_max_tidy(max_value):
   while max_value > 0:
      if(is_tidy(str(max_value))):
         return max_value
      max_value-=1

# end small input size

def main():
   input_file = open("input_B.txt")
   output_file = open("output_B.txt", "a")	
   num_test_cases = int(input_file.readline())
   test_vals = []
   for line in input_file:
      test_vals.append(int(line))

   tc = 1
   while tc <= num_test_cases:
      max_tidy_num = find_max_tidy(test_vals[tc-1])
      out_str = "Case #" + str(tc) +": " + str(max_tidy_num) + "\n"
      output_file.write(out_str) 
      tc+=1
 
   input_file.close()
   output_file.close()

if __name__ == '__main__':
   main()
