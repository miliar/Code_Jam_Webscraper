#!/usr/bin/env python

def tidy(x):
   if (str(x) == ''.join(sorted(str(x)))):
      return True
   else:
      return False

cnt = 0
f = open("infile")
text_file = open("output.txt","w")
#ignore # of recs
f.readline()
next = f.readline()
while next != "":
   a = int(next)
   while not (tidy(a)):
      a -= 1
   cnt += 1

   s = "Case #" + str(cnt) + ": " + str(a)
   print (s)
   text_file.write(s + "\n")
   next = f.readline()
text_file.close()
