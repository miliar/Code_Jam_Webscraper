def count_continuous(v1, char, after_index):
    count = 0
    i = 50
    for i in range(after_index+1, len(v1)):
        if v1[i] == char:
            count += 1
            if i+1 < len(v1) and v1[i+1] == char:
                continue
            else:
                break

    return count, i

def is_valid(v2, index, search_string):
    char = v2[index]
    sl_index = search_string.find(char)
    sr_index = search_string.rfind(char)
    i = index-1
    j = sl_index-1
    k=sr_index+1
    while i>=0 and j >= 0:
        if search_string[j] == v2[i]:
            j -= 1
        i -= 1
    i=index+1
    while i< len(v2) and k < len(search_string):
        if search_string[k] == v2[i]:
            k += 1
        i += 1
    print j , k, len(search_string)
    if j < 0 and k >= len(search_string):
        return 1

    return 0

def remove_junks(v1, search_string):
    v2 = v1
    for i in xrange(len(v1)):
        if search_string.find(v1[i]) == -1:
            v2 = v2.replace(v1[i], '')

    delete_indexes=[]
    for i in xrange(len(v2)):
        if is_valid(v2, i, search_string) == 0:
            print "returned false"
            delete_indexes.append(i)
    v3=[]
    j = 0
    i = 0
    print delete_indexes
    while (j < len(v2)) :
        if i<len(delete_indexes) and j == delete_indexes[i]:
            i += 1
        else:
            v3.append(v2[j])
        j += 1
    return ''.join(v3)

def get_total(v1, search_string, SI, VI):
    
    count, VI1 = count_continuous(v1, search_string[SI], VI)
    
    if SI+1 < len(search_string) and VI1 < len(v1):
        return (count%10000) * (get_total(v1, search_string, SI+1, VI1))%10000 + (get_total(v1, search_string, SI, VI1))%10000     
    elif SI+1 == len(search_string) and VI1 < len(v1):
            return count%10000 + (get_total(v1, search_string, SI, VI1))%10000
    else:
        return count%10000

def prepare_input(input_file):

    output_file = open('C-small.out', 'w')
    N = int(input_file.readline().replace('\n',''))
    search_string = "welcome to code jam"
    #search_string = "wel"

    for test_case_counter in xrange(N):
        print "-----------------------------------------"
        result_count=0
        #get all the engines
        v1 = input_file.readline().replace('\n','')
        #v1 = remove_junks(v1, search_string)
        print v1
        result_count = get_total(v1, search_string, 0, -1)
        #lowest count will be the number of switches in the server
        string_out = str(result_count)
        output_file.write("Case #"+str(test_case_counter+1)+": ")
        for i in xrange(4-len(string_out)):
            output_file.write("0")
        output_file.write(str(result_count)+"\n")

    output_file.close()

if __name__ == "__main__":
    input_file = file("C-small-attempt0.in")
    prepare_input(input_file)
