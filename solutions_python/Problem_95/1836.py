data = [l.strip() for l in open("infile", "r").readlines()]
out = open("outfile", "w")

newletters = ['y', 'h', 'e', 's', 'o', 
              'c', 'v', 'x', 'd', 'u', 
              'i', 'g', 'l', 'b', 'k', 
              'r', 'z', 't', 'n', 'w', 
              'j', 'p', 'f', 'm', 'a', 'q']

ncases = int(data.pop(0))
for case in range(ncases):
  line = data.pop(0)
  trans = ""
  for letter in line:
    if letter == ' ':
      trans += letter
    else:
      trans += newletters[ord(letter)-97]
  out.write("Case #" + str(case + 1) + ": " + trans + "\n")
