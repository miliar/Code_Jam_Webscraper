# Recycling numbers
import math

def number_rotations(x):
  s = str(x)
  for n in range(len(s)-1):
    s = s[1:] + s[0]
    yield int(s)

def main():
  in_file = open('input.txt', 'r')
  lines = in_file.readlines()
  in_file.close()

  out_file = open('output.txt', 'w')
  num_cases = int(lines.pop(0)) # We don't really use this...
  case_count = 1
  while lines:
    text = lines.pop(0)
    vals = map(int, text.split())

    A = max(10, vals.pop(0))
    B = max(10, vals.pop(0))

    output = {}
    result = 0

    # brute force, pretty silly but eh
    limits = range(A, B+1)
    for x in limits:
      if not x in output:
        for y in number_rotations(x):
          if y in limits and x < y and not y in output:
            if x in output:
              output[x].append(y)
            else:
              output[x] = [y]
            result += 1


    # Check for (n, m) and (m, n)

    """"    for k in output:
      print "%d -> " % (k), output[k]
      for v in output[k]:
        if v in output and k in output[v]:
          print (v, k)
        if not v in number_rotations(k):
          print (v, k)
        if str(v)[0] == '0' or str(k)[0] == '0':
          print "Leading 0: (%d, %d)" % (k, v);
        if not v in limits or not k in limits:
          print "out of limits"
        if len(str(v)) != len(str(k)):
          print "Unmatched len"

"""

    output = "Case #%d: %s\n" % (case_count, result)
    out_file.write(output)
    print output,
    case_count += 1


if __name__=="__main__":
  main()
