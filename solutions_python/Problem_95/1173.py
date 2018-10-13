try:
    import psyco
    psyco.full()
except:
    pass

from sys import stdin, stdout

mydict = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c',
 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b',
 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p',
 'y': 'a', 'x': 'm', 'z': 'q'}

n = int(stdin.readline())

for i in range(n):
   input_str = stdin.readline()
   output_str = "Case #%d: " % (i + 1)

   for char in input_str:
      if char != '\n':
         output_str += mydict[char]
   stdout.write(output_str + '\n');
