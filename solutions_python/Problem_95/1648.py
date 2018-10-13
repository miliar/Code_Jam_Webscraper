import string

ex1_in = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
ex1_out = "our language is impossible to understand"

ex2_in = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
ex2_out = "there are twenty six factorial possibilities"

ex3_in = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
ex3_out = "so it is okay if you want to just give up"

def create_dictionary():
    d = dict()
    
    for i,letter in enumerate(ex1_out):
        d[ex1_in[i]] = letter 
        
    for i,letter in enumerate(ex2_out):
        d[ex2_in[i]] = letter
        
    for i,letter in enumerate(ex3_out):
        d[ex3_in[i]] = letter
        
    d['y'] = 'a'
    d['e'] = 'o'
    d['q'] = 'z'
    
    small_letters = string.letters[0:26]
    
    for letter in small_letters:
        if letter not in d.keys():
            last_key = letter
    
    for result in small_letters:
        if result not in d.values():
            last_value = result
            
    d[last_key] = last_value    
    
    return d   

def translate_line(jib,dic):
    out = jib
    out = list(out)
    result = out
    small_letters = string.letters[0:26]
    
    for i,letter in enumerate(out):
        if letter=='\n':
            continue
        result[i] = dic[letter]
        
    return "".join(result)

def solve(dic):
    mapper = dic
    
    file_in = file("A-small-attempt1.in")
    file_out = file("A-small-attempt1.out","w")
    num_of_cases = int(file_in.readline())
    
    for i in range(num_of_cases):
        line = file_in.readline()
        translated = translate_line(line, mapper)
        file_out.writelines(['Case #%s: %s' % (i+1,translated)])
    
    file_out.close()
        

if __name__ == '__main__':
    d = create_dictionary()
    solve(d)