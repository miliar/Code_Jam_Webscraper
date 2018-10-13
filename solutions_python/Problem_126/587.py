# google codejam
# io template
import argparse, os

VOWELS = set(["a", "e", "i", "o", "u"])

def solve(case):
   n_value = 0
   for each in substrings(case[0], case[1]):
      if has_consonant_chain_of(each, case[1]):
         n_value += 1
   return str(n_value)
   
def substrings(word, min):
   for start in range(len(word) - min + 1):
      current = word[start:]
      for idx in range(min, len(current) + 1):
         yield current[:idx]
         
def has_consonant_chain_of(word, n):
   count = 0
   for char in word:
      if char not in VOWELS:
         count += 1
      else:
         count = 0
      if count >= n:
         return True
   return False
   
def parse(source):
   line = source.readline()
   elements = line.split()
   return elements[0], int(elements[1])
    
class Challenge():
   """read and write codejam case files"""
   def __init__(self, in_file, out_file):
      self.input = in_file
      self.output = out_file
      open(self.output,"w").close()
      self.write_cursor = 1
      with open(self.input, "r") as source:
         self.case_count = int(source.readline())
      
   def write(self, answer):
      """write case answers in ascending order"""
      with open(self.output, "ab") as sink:
         nl = "\n" if self.write_cursor > 1 else ""
         text = "{}Case #{:d}: {}".format(nl, self.write_cursor, answer)
         sink.write(bytes(text,"utf-8"))
         self.write_cursor += 1
         
   def cases(self, parse):
      """read cases from input file using the given parser
            the parse function will be given the source file object to read from"""
      with open(self.input, "r") as source:
         source.readline() # skip case count
         for i in range(self.case_count):
            yield parse(source)
   
            
if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('input')
   parser.add_argument('output', nargs = "?", default = None)
   args = parser.parse_args()
   input_file = args.input
   output_file = args.output if args.output is not None else os.path.splitext(os.path.basename(input_file))[0] + ".out"
   io = Challenge(input_file, output_file)
   for case in io.cases(parse):
      answer = solve(case)
      io.write(answer)