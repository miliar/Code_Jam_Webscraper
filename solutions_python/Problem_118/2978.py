import sys, math

memoized = {}

def fair_and_square(filename):
  def palindrome(number):
    temp, reversed_number = number, 0
    while temp != 0:
      reversed_number = reversed_number*10 + temp%10
      temp /= 10
    return reversed_number == number

  with open(filename) as inp:
    lines = inp.readlines(2)
  tests = int(lines.pop(0))

  output_file_contents = []

  for i in xrange(tests):
    fairs = 0
    rng = map(int, lines.pop(0).split())
    for j in xrange(rng[0], rng[1]+1):
      state = False
      if memoized.has_key(j):
        if memoized.get(j): fairs += 1
        continue
      else:
        if palindrome(j):
          square_root = int(math.sqrt(j))
          if square_root*square_root == j and palindrome(square_root):
            fairs += 1
            state = True
        memoized[j] = state
        

    output_file_contents.append("Case #%d: %d\n" % (i+1, fairs))
  
  with open('fair-and-square.out', 'w') as out:
    out.writelines(output_file_contents)




if __name__ == '__main__':
  fair_and_square(sys.argv[1])
