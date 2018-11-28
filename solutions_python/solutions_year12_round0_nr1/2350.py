f = open('/home/izuzak/Downloads/A-small-attempt0.in', 'r')
o = open('/home/izuzak/Downloads/out', 'w')
lines = f.readlines()[1:]

mapping_in = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
mapping_out =['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q', ' ']

lineno = 1
for line in lines:
  l = list(line[:-1])
  out = l[:]
  s = 'Case #' + str(lineno) + ': '
  for i in range(len(l)):
    out[i] = mapping_out[mapping_in.index(l[i])]
  o.write(s + ''.join(out) + '\n')
  lineno = lineno + 1;
