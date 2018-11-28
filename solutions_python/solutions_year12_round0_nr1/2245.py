import string

def create_mapping(str1, str2, goog_dict):
    str1 = str1.replace(' ', '')
    str2 = str2.replace(' ', '')

    for i in range(len(str1)):
        goog_dict[str1[i]] = str2[i]

    return goog_dict

def calc_map():
    goog_dict = {'y': 'a', 'e': 'o', 'q': 'z'}

    english = ["our language is impossible to understand", 
               "there are twenty six factorial possibilities",
               "so it is okay if you want to just give up"]
    googlerese = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
                  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                  "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
    
    for i in range(3):
        create_mapping(googlerese[i], english[i], goog_dict)

    return goog_dict

def find_missing(goog_dict):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    goo_str = ''.join(goog_dict.keys())
    eng_str = ''.join(goog_dict.values())
    
    missing_goo = alphabet.strip(goo_str)
    missing_eng = alphabet.strip(eng_str)

    goog_dict[missing_goo] = missing_eng

    return goog_dict

def translate(goog_dict):
    return string.maketrans(''.join(goog_dict.keys()), 
                            ''.join(goog_dict.values()))

def main():
    goog_dict = find_missing(calc_map())
    table = translate(goog_dict)
    
    f = open('input.txt')
    num_cases = int(f.readline())

    for i in range(1, num_cases + 1):
        case = f.readline().strip('\n')
        out = string.translate(case, table)
        print "Case #" + str(i) + ": " + out

if __name__ == '__main__':
    main()
