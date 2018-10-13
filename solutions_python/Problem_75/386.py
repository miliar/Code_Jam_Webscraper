infile = open("B-large.in")
outfile = open("B-large.out",'w')
lines = infile.readlines()
c = []
d=[]
T=int(lines[0])
def evaluate(s):
  global c
  global d
  for rule in c:
    if (rule[0]+rule[1] == s[len(s)-2:] or rule[1]+rule[0] == s[len(s)-2:]):
      return str(s[:len(s)-2]+rule[2]) 
  for rule in d:
    if (s[len(s)-1] ==  rule[0] and rule[1] in s[:len(s)-1]):
      return ""
    if (s[len(s)-1] ==  rule[1] and rule[0] in s[:len(s)-1]):
      return ""
  return s
for case in range(1,T+1):
  data = lines[case].split()
  c = []
  d = []
  C = int(data[0])
  for i in range(1,C+1):
    c.append(data[i])
  D= int(data[C+1])
  for i in range(2+C,2+C+D):
    d.append(data[i])
  N = int(data[2+C+D])
  sequence = data[3+C+D]
  out = ""
  for letter in sequence:
    out = evaluate(out + letter)
    
  outfile.write("Case #%d: ["%case)
  if len(out)>0:
    outfile.write(out[0])
  for i in range(1,len(out)):
    outfile.write(", %s"%out[i])
  outfile.write("]\n")
