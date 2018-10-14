'''
Created on 14 Apr 2012

@author: benoit
'''



if __name__ == '__main__':
    
    map = {
       ' ' : ' ',       
       'a' : 'y',
       'b' : 'h',
       'c' : 'e',
       'd' : 's',
       'e' : 'o',
       'f' : 'c',
       'g' : 'v',
       'h' : 'x',
       'i' : 'd',
       'j' : 'u',
       'k' : 'i',
       'l' : 'g',
       'm' : 'l',
       'n' : 'b',
       'o' : 'k',
       'p' : 'r',
       'q' : 'z',
       'r' : 't',
       's' : 'n',
       't' : 'w',
       'u' : 'j',
       'v' : 'p',
       'w' : 'f',
       'x' : 'm',
       'y' : 'a',
       'z' : 'q',
       '\n' : '\n',
       }
    
    
    f= open(r'C:/google/input.txt', 'r')
    number_case = f.readline()
    g = open(r'C:/google/output.txt', 'w')
    for i in range(int(number_case)):
        result = "Case #" + str(i+1) + ":"
        string_from = f.readline()
        string_to_table = [map[x] for x in string_from]
        string_to = ""
        for charact in string_to_table:
            string_to = string_to + charact
        result = result + " " + string_to
        g.write(result)