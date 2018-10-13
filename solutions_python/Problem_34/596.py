# Read in File

f = open('A-large.in', 'r')

(L, D, N) = f.readline().strip().split(' ')
L = int(L)
D = int(D)
N = int(N)

# print "word length: ", L
# print "num words: ", D
# print "num tests: ", N

words = {}

def add_word(word):
  # print "adding: %s" % word
  cur = words
  last = ""
  for letter in word:
    if (not cur.has_key(letter)):
      cur[letter] = {}
    cur = cur[letter]
    last = letter
  cur = True

for i in range(0, D):
  word = f.readline().strip()
  add_word(word)

## Words should be: {'a': {'b': {'c': {}}}, 'c': {'b': {'a': {}}}, 'b': {'c': {'a': {}}}, 'd': {'a': {'c': {}}, 'b': {'c': {}}}}

# print words

def chunk_word(word):
  retn = []
  current = []
  in_list = False
  for letter in word:
    if(letter == '('):
      current = []
      in_list = True
    elif (letter == ')'):
      retn.append(current)
      in_list = False
      pass
    elif (in_list):
      current.append(list(letter))
    else:
      retn.append(list(letter))
  return retn

# chunk_word("abc")    =  [['a'], ['b'], ['c']]
# chunk_word("(ab)bc") =  [[['a'], ['b']], ['b'], ['c']]

def test_word(word):
  letters = chunk_word(word)
  num_possible = 0
  cur = words
  to_test = [words]
  next_tests = []
  for lst in letters:
    for letter in lst:
      letter = letter[0]
      for hash in to_test:
        # print "hash: %s" % hash
        if (hash.has_key(letter)):
          # print "  has key: %s" % letter
          next_tests.append(hash[letter])
    to_test = next_tests
    next_tests = []
    # print "to test: %s" % to_test
  return len(to_test)

for i in range(0, N):
  word = f.readline().strip()
  ret = test_word(word)
  print "Case #%d: %d" % (i+1, ret)
