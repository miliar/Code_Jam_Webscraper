try:
    import psyco
    psyco.full()
except:
    pass

from sys import stdin, stdout

def move(number_str):
   return number_str[-1] + number_str[:-1] 

n = int(stdin.readline())

for case in range(n):
   pairs = 0
   a, b = map(int,stdin.readline().split())
   domain_in_strings = map(str,range(a, b + 1))
 
   for number_str in domain_in_strings:
      aux_str = number_str
      permutations = []
      for i in range(len(number_str) - 1):
         aux_str = move(aux_str)
         permutations.append(aux_str)
         

      set_of_permutations = set(permutations) 

      for permutation in set_of_permutations:
         if number_str != permutation and permutation in domain_in_strings:
            if int(number_str) < int(permutation) and not permutation.startswith('0'):
               pairs += 1
               #print number_str,permutation 
   
   output_str = "Case #%d: " % (case + 1)
   output_str += str(pairs)   
   stdout.write(output_str + '\n');
