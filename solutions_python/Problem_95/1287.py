'''
Created on Apr 14, 2012

@author: kevin
'''

input = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

output = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""



if __name__ == "__main__":
    lang_map = {}
    lang_map['z'] = 'q'
    lang_map['q'] = 'z'
    for (index, char) in enumerate(input):        
        input_char = input[index]
        output_char = output[index]
        if (input_char in lang_map):
            if (lang_map[input_char] != output_char):
                print "error:"
                
        else:
            lang_map[input[index]] = output[index]
    
     
    f = open('A-small-attempt1.in', 'r')
    text = f.readline()
    num_entry = int(text)
    print num_entry
    for i in range(num_entry):
        
        text = f.readline()    
        result = ''.join([lang_map[char] for char in text])        
        print "Case #%i: %s" % (i + 1, result),
    
        
    