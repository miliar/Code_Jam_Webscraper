

def numbers_to_number(numbers):
    base = max(numbers)+1
    nb_obtained = 0
    
    numbers.reverse()
    mult = 1
    for i in numbers:
        nb_obtained += mult*i
        mult *= base
    return nb_obtained

def alien_to_numbers(lst):
    result = [1]

    nb_used = {}
    nb_used[lst[0]] = 1

    zero_used = False
    nb_next = 2    
    for no in lst[1:]:
        if no in nb_used.keys():
            result.append(nb_used[no])
        else:
            if not zero_used:
                nb_used[no] = 0
                result.append(0)
                zero_used = True
            else:
                nb_used[no] = nb_next
                result.append(nb_next)
                nb_next += 1
    return result

N = int(raw_input())

for i in range(1,N+1):
    word = raw_input()
    
    print "Case #%d: %d" % (i, numbers_to_number(alien_to_numbers(list(word))));
    

    