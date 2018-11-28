import string

def main():
  in_file = open('input.txt', 'r')
  lines = in_file.readlines()
  in_file.close()

  mapping = {'a': 'y', 'o': 'e', 'z':'q', 'q': 'z' }

  basis = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
""";

  basis_out = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
""";

  for from_c, to_c in zip(basis, basis_out):
    if from_c in string.lowercase:
      print "%c goes to %c" % (from_c, to_c)
      if from_c in mapping and mapping[from_c] != to_c:
        print "Collision with %c -> %c" % (from_c, to_c)
      if to_c in mapping.items():
        print "wtf"
      mapping[from_c] = to_c

  for from_c, to_c in mapping.items():
    print "%c%c" % (from_c, to_c)

  out_file = open('output.txt', 'w')
  num_cases = int(lines.pop(0)) # We don't really use this...
  n = 1
  while lines:
    text = lines.pop(0)

    perms = []
    t = "".join(map(lambda c: c in mapping and mapping[c] or c, text))
    t = "Case #%d: %s" % (n, t)
    out_file.write(t)
    print t,
    n += 1


if __name__=="__main__":
  main()
