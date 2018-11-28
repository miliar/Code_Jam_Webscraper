import sys

is_tidy = lambda x: x == "".join(sorted(str(x)))

index = -1

for line in sys.stdin.readlines():
  index += 1
  if index > 0:
    line = line.strip()
    if is_tidy(line):
      result = line
    else:
      digits = [ int(c) for c in line ]
      while not is_tidy(''.join([str(c) for c in digits])):
        for i in xrange(len(digits)):
          if digits[i] > digits[i+1]:
            rim = i
            break
        digits = digits[:rim] + [digits[rim] - 1] + [9]*len(digits[rim+1:])
      result = digits
    print "Case #%i: %i" % (index, int(''.join([str(c) for c in result])))
