#
# Author : Sachin Karambalkar
# Date : 14 April 2012
# Problem : ( A ) Speaking in Tongues [ Code Jam 2012 ]
# Platform : Ubuntu 10.10
# Programming Language : Python
# Compiler : python 2.6.6
#
import sys

map_dict = {
                'y' : 'a',
                'n' : 'b',
                'f' : 'c',
                'i' : 'd',
                'c' : 'e',
                'w' : 'f',
                'l' : 'g',
                'b' : 'h',
                'k' : 'i',
                'u' : 'j',
                'o' : 'k',
                'm' : 'l',
                'x' : 'm',
                's' : 'n',
                'e' : 'o',
                'v' : 'p',
                'z' : 'q',
                'p' : 'r',
                'd' : 's',
                'r' : 't', 
                'j' : 'u',
                'g' : 'v',
                't' : 'w',
                'h' : 'x',
                'a' : 'y',
                'q' : 'z',
                ' ' : ' ',
            }


def _output( input_lines ):
    output_lines = []
    for line in input_lines:
        pos = 0
        new_line =""
        new_char =""
        while pos < len(line):
            new_char = map_dict[line[pos]]
            new_line+="%c"%new_char
            pos = pos + 1
        output_lines.append( new_line )

    for line in output_lines:
        print "Case #%d: %s"%(output_lines.index(line)+1, line)


if __name__ == "__main__":
    num = raw_input()
    i = 1
    input_lines = []
    while i <= int(num):
        _input = raw_input()
        if len( _input ) > 100:
            print "Input line size exceeds 100 characters."
            sys.exit(1)
        input_lines.append( _input.lower() )
        i=i+1

    _output( input_lines )


