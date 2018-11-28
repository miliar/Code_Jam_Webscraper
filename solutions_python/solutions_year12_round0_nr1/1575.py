import string

def init():
    '''build googlerese_to_english'''
    googlerese_to_english = {}
    #temp_english = {}

    googlerese = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
                  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                  "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
    english = ["our language is impossible to understand",
               "there are twenty six factorial possibilities",
               "so it is okay if you want to just give up"]

    for i in range(len(googlerese)):
        for j in range(len(googlerese[i])):
            #print googlerese[i][j], english[i][j]
            googlerese_to_english[googlerese[i][j]] = english[i][j]
            
    googlerese_to_english["q"] = "z"
    googlerese_to_english["z"] = "q"

    """
    for l in string.lowercase[:16]:
        temp_english[googlerese_to_english[l]] = ""
        print l, googlerese_to_english[l]

    for l in string.lowercase[17:-1]:
        temp_english[googlerese_to_english[l]] = ""
        print l, googlerese_to_english[l]

    print sorted(temp_english)
    
    for l in string.lowercase:
        print l, googlerese_to_english[l]
    """

    return googlerese_to_english


def solve(case_string):
    result = ''
    for letter in case_string:
        result += googlerese_to_english[letter]
        
    return result

#input, solve and output:
                        
input = open('A-small-attempt0.in', 'r')
output = open('A-small-attempt0.out', 'w')
googlerese_to_english = init()

num_cases = int(input.readline())
for case in range(1, num_cases+1):
        case_string = input.readline().strip()
        result = solve(case_string)
        
        output.write('Case #%s: %s\n' %(case, result))

input.close()
output.close()

