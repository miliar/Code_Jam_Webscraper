""" Speaking in Tongues """
""" Google Language ---> Googlerese """
""" Googlerese is made from english in such a way that
    a english sentence mapped into a "Googlerese" sentence
    that is not valid in English """
""" G has one-to-one and onto mapping into X(English) """


import string
basic_letters = list(string.ascii_lowercase)

def create_language_dictionary() :
    dic = {}
    dic['a'] = 'y'
    dic['b'] = 'n'
    dic['c'] = 'f'
    dic['d'] = 'i'
    dic['e'] = 'c'
    dic['f'] = 'w'
    dic['g'] = 'l'
    dic['h'] = 'b'
    dic['i'] = 'k'
    dic['j'] = 'u'
    dic['k'] = 'o'
    dic['l'] = 'm'
    dic['m'] = 'x'
    dic['n'] = 's'
    dic['o'] = 'e'
    dic['p'] = 'v'
    dic['q'] = 'z'
    dic['r'] = 'p'
    dic['s'] = 'd'
    dic['t'] = 'r'
    dic['u'] = 'j'
    dic['v'] = 'g'
    dic['w'] = 't'
    dic['x'] = 'h'
    dic['y'] = 'a'
    dic['z'] = 'q'
    dic[' '] = ' '

    return dic

def reverse_dictionary(dic) :
    d = {' ' : ' ' }
    for i in basic_letters :
        d[dic[i]]=i
    return d

def convert_G_to_X(g_sentence, dic) :
    sentence = ""
    for i in g_sentence :
        sentence += dic[i]
    return sentence

def convert_X_to_G(sentence, dic) :
    g_sentence = ""
    for i in sentence :
        g_sentence += dic[i]
    return g_sentence

dic = create_language_dictionary()

reverse_dic = reverse_dictionary(dic)

s1 = "our language is impossible to understand"
s2 = "there are twenty six factorial possibilities"
s3 = "so it is okay if you want to just give up"

#print(convert_X_to_G(s3, dic))

s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

def solution(reverse_dic) :
    file = open("A-small-attempt3.in", "r")
    file_w = open("output1.txt", "w")
    line_no = 1
    for i in file :
        if line_no == 1 :
            line_no += 1
            continue
        s = convert_G_to_X(i[:len(i)-1], reverse_dic)
        sc = 'Case #' + str(line_no-1) +': '
        file_w.write(sc)
        file_w.write(s)
        file_w.write('\n')
        line_no += 1
    file_w.close()
    file.close()

    
##print(s1)
##print('-----------------------------------')
##print(convert_G_to_X(s1, reverse_dic))
##print('-----------------------------------')
##
##print(s2)
##print('-----------------------------------')
##print(convert_G_to_X(s2, reverse_dic))
##print('-----------------------------------')
##
##print(s3)
##print('-----------------------------------')
##print(convert_G_to_X(s3, reverse_dic))
##print('-----------------------------------')

#print(convert_G_to_X(s, reverse_dic))

solution(reverse_dic)
