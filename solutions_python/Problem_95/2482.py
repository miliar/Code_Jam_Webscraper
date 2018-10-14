gese = "ejp mysljylc kd kxveddknmc re jsicpdrysi \
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd \
de kr kd eoya kw aej tysr re ujdr lkgc jv"

eng = "our language is impossible to understand \
there are twenty six factorial possibilities \
so it is okay if you want to just give up"

gese = ''.join(gese.split())
eng = ''.join(eng.split())

dictionary = {'z':'q', 'q':'z'}
for letter in range(len(gese)):
    goog = gese[letter]
    english = eng[letter]
    dictionary[goog] = english
    
def translate(file_name):
    f = open(file_name, 'r')
    cases = int(f.readline())
    result = ""
    for num in range(cases):
        text = f.readline()
        result += "Case #" + str(num+1) + ": " + convert(text)
    print result[:-1]
        
def convert(text):
    def mapchar(char):
        if dictionary.has_key(char): return dictionary[char]
        else: return char
    return ''.join([mapchar(char) for char in text])
        