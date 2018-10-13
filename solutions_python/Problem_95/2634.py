#!/usr/bin/python

import sys

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

#Output file
filename = "1.out"
FILE = open(filename,"w")


#main
T = f.readline()
lines = f.readlines()
dict = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
i=1;
for strings in lines:
   FILE.write("Case #%d: " % (i))
   i=i+1
   for char in strings:
      if char in dict:
         FILE.write(dict[char])
      else:
         FILE.write(char)

FILE.close()
