T = int(raw_input())
values = {'11':'1','1i':'i','1j':'j','1k':'k','i1':'i','ii':'1','ij':'k','ik':'j','j1':'j','ji':'k','jj':'1','jk':'i','k1':'k','ki':'j','kj':'i','kk':'1'}
signs  = {'11':'+','1i':'+','1j':'+','1k':'+','i1':'+','ii':'-','ij':'+','ik':'-','j1':'+','ji':'-','jj':'-','jk':'+','k1':'+','ki':'+','kj':'-','kk':'-'}

def print_case(case,result):
    print "Case #"+str(case+1)+": "+result

def check_i_k(string):
    #find first i
    i = -1
    i_positive = True
    cache_string = string
    current_char = 0
    if cache_string[0] == 'i':
        i = 0
    else:
        while len(cache_string) > 1:
            current_char += 1
            sign = signs[cache_string[:2]]
            if sign == '-' and i_positive: i_positive = False
            elif sign == '-' and not i_positive : i_positive = True
            if values[cache_string[:2]] == "i" and i_positive:
                i = current_char
                break
            cache_string = values[cache_string[:2]] + cache_string[2:]
            
    #find last k 
    k = -1
    k_positive = True
    cache_string = string
    current_char = len(string)-1
    if cache_string[len(cache_string)-1] == "k":
        k = len(cache_string)-1
    else:
        while len(cache_string) > 1:
            current_char -= 1
            sign = signs[cache_string[-2:]]
            if sign == '-' and k_positive: k_positive = False
            elif sign == '-' and not k_positive : k_positive = True
            if (values[cache_string[-2:]] == "k" and k_positive):
                k = current_char
                break
            cache_string = cache_string[:-2] + values[cache_string[-2:]]
    return i,k

def calculate_string(string):
    positive = True
    while len(string) > 1:
        sign = signs[string[:2]]
        if sign == "-" and positive == True:
            positive = False
        elif sign == "-" and positive == False:
            positive = True
        string = values[string[:2]] + string[2:]
    return string,positive

for case in range(T):
    first_raw = raw_input().split(" ")
    L = int(first_raw[0])
    X = int(first_raw[1])
    string = str(raw_input())
    #pre checks
    if L*X <= 2:
        print_case(case,"NO")
        continue
    elif L*X == 3:
        if string == "ijk":
            print_case(case,"YES")
            continue
        else:
            print_case(case,"NO")
            continue
    repeat = X if X < 20 else 20
    repeated = ""
    while repeat > 0:
        repeated += string
        repeat -= 1
          
    final,positive = calculate_string(string)
#     print final,positive
    if final == '1':
        if positive:
            print_case(case,"NO")
            continue
        elif (not positive) and X % 2 == 0:
            print_case(case,"NO")
            continue
        else:
            pass # maybe
#     else:
#         print_case(case,"NO")
#         continue
    else:
        if X % 2 == 1:
            print_case(case,"NO")
            continue
        elif ( X / 2 ) % 2 == 0:
            print_case(case,"NO")
            continue
        else:
            pass # maybe
      
    i,k = check_i_k(repeated)
  
    if (k-i) < 1 or i == -1 or k == -1:
        print_case(case,"NO")
    else:
        print_case(case,"YES")    