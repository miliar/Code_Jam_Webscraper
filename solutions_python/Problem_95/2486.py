#!/usr/bin/python
#coding=utf-8
import sys

map_dict = dict(a="y", b="h", c="e", d="s", e="o", 
	     f="c", g="v", h="x", i="d", j="u", 
	     k="i", l="g", m="l", n="b", o="k",
	     p="r", q="z", r="t", s="n", t="w", 
	     u="j", v="p", w="f", x="m", y="a", z="q")
map_dict[" "] = " "

if len(sys.argv) < 3:
   print "Uso: %s <input filename> <output filename>" % sys.argv[0]
   sys.exit()
       
input_filename = sys.argv[1]
output_filename = sys.argv[2]
file = open(input_filename, "r")
output_file = open(output_filename, "w")
cases = int(file.readline())

for case in range(0,cases):
    whole_line = file.readline()
    new_line = ""
    for letter in whole_line:
        new_line += map_dict[letter] if map_dict.has_key(letter) else ""
    output_file.write('Case #%d: %s\n' % (case+1, new_line))

file.close()
output_file.close()

