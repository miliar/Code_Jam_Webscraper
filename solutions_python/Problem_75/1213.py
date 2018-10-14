 
def getReplaceElement(replace_list,prev_elem, curr_elem):
    for string in replace_list:
      if (string[0] == curr_elem and string[1] == prev_elem) or (string[1] == curr_elem and string[0] == prev_elem):
        return string[2]
        
    return ''
    
def getRemoveIndex(remove_list, flag_index, curr_elem):
    for string in remove_list:
        try:
            if curr_elem == string[0] and flag_index[string[1]] != -1:
                return flag_index[string[1]]
        except:
          pass
        try:
            if curr_elem == string[1] and flag_index[string[0]] != -1:
                return flag_index[string[0]]
        except:
          pass
    return -1

def rfind(list, elem):
    ret = -1
    i = len(list)-1
    while i > -1:
        if list[i] == elem:
            ret = i
            break
        i -= 1
    return ret
    
def prepare_input(input_file):
    T = int(input_file.readline().replace('\n',''))
        
    output_file = file("B-large.out", "w")
        
    for test_case_counter in xrange(T):
        v1 = input_file.readline().replace('\n','').split(' ')
        index = 0
        replace_list = []
        remove_list = []
        C = int(v1[index])
        index += 1
        for i in xrange(C):
          replace_list.append(v1[index])
          index += 1
        D = int(v1[index])
        index += 1
        for i in xrange(D):
          remove_list.append(v1[index])
          index += 1
        N = int(v1[index])
        index += 1
        out_list = []
        flag_index = {}
        for i in xrange(len(v1[index])):
          if len(out_list) == 0:
            out_list.append(v1[index][i])
            flag_index[v1[index][i]] = 0
          else:
              length = len(out_list)
              replace_elem = getReplaceElement(replace_list, out_list[length-1], v1[index][i])
              if replace_elem <> '':
                  elem = out_list[length-1]                  
                  out_list[length-1] = replace_elem
                  flag_index[elem] = rfind(out_list, elem)
              else:
                  remove_index = getRemoveIndex(remove_list, flag_index, v1[index][i])
                  if remove_index == -1:
                      out_list.append(v1[index][i])
                      flag_index[v1[index][i]] = len(out_list)-1
                  else:
                    out_list[:] = []
                    for key in flag_index:
                        flag_index[key] = -1
                        
         
        #lowest count will be the number of switches in the server
        output_file.write("Case #"+str(test_case_counter+1)+": [")
        length = len(out_list)
        for i in xrange(length):
            if i < length-1:
              output_file.write(out_list[i] + ', ')
            else:
              output_file.write(out_list[i])
        output_file.write("]\n")
        
    output_file.close()
    
if __name__ == "__main__":
    input_file = file("B-large.in")
    prepare_input(input_file)
