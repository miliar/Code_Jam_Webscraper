"""The grouper class has been reciped from:
http://code.activestate.com/recipes/387776/
"""

class Grouper(object):
   """This class provides a lightweight way to group arbitrary objects
together into disjoint sets when a full-blown graph data structure
would be overkill.

Objects can be joined using .join(), tested for connectedness
using .joined(), and all disjoint sets can be retreived using
.get().

The objects being joined must be hashable.

For example:

>>> g = grouper.Grouper()
>>> g.join('a', 'b')
>>> g.join('b', 'c')
>>> g.join('d', 'e')
>>> list(g.get())
[['a', 'b', 'c'], ['d', 'e']]
>>> g.joined('a', 'b')
True
>>> g.joined('a', 'c')
True
>>> g.joined('a', 'd')
False"""   
   def __init__(self, init=[]):
      mapping = self._mapping = {}
      for x in init:
         mapping[x] = [x]
        
   def join(self, a, *args):
      """Join given arguments into the same set.
Accepts one or more arguments."""
      mapping = self._mapping
      set_a = mapping.setdefault(a, [a])

      for arg in args:
         set_b = mapping.get(arg)
         if set_b is None:
            set_a.append(arg)
            mapping[arg] = set_a
         elif set_b is not set_a:
            if len(set_b) > len(set_a):
               set_a, set_b = set_b, set_a
            set_a.extend(set_b)
            for elem in set_b:
               mapping[elem] = set_a

   def joined(self, a, b):
      """Returns True if a and b are members of the same set."""
      mapping = self._mapping
      try:
          return mapping[a] is mapping[b]
      except KeyError:
          return False

   def __iter__(self):
      """Returns an iterator returning each of the disjoint sets as a list."""
      seen = set()
      for elem, group in self._mapping.iteritems():
          if elem not in seen:
              yield group
              seen.update(group)



fin = open('B-small.in', 'r');
fout = open('B-small.out', 'w');

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]

def common(x, y, l):
	for p in primes:
		if p >= l and x % p == 0 and y % p == 0:
			return True
	return False

T = int(fin.readline());

for i in range(T):
	args = fin.readline().split(' ')
	
	A = int(args[0])
	B = int(args[1])
	P = int(args[2])

	g = Grouper(range(A,B+1))

	for j in range(A,B+1):
		for h in range(j+1, B+1):
			if not g.joined(j, h) and common(j, h, P):
				g.join(j, h)

	fout.write('Case #' + str(i + 1) + ': ' + str(len(list(g))) + '\n')
