list_cases=[]
list_output=[]
testcases=0

ELEMENT_1 = 'i'
ELEMENT_2 = 'j'
ELEMENT_3 = 'k'
ELEMENT_4 = '-i'
ELEMENT_5 = '-j'
ELEMENT_6 = '-k'
ELEMENT_7 = '-1'
ELEMENT_8 = '1'
ELEMENT_END = '0'

map_ELEMENT_1 = { ELEMENT_1:ELEMENT_7, ELEMENT_2:ELEMENT_3,ELEMENT_3:ELEMENT_5}
map_ELEMENT_2 = { ELEMENT_1:ELEMENT_6, ELEMENT_2:ELEMENT_7,ELEMENT_3:ELEMENT_1}
map_ELEMENT_3 = { ELEMENT_1:ELEMENT_2, ELEMENT_2:ELEMENT_4,ELEMENT_3:ELEMENT_7}

map_ELEMENT_4 = { ELEMENT_1:ELEMENT_8, ELEMENT_2:ELEMENT_6,ELEMENT_3:ELEMENT_2}
map_ELEMENT_5 = { ELEMENT_1:ELEMENT_3, ELEMENT_2:ELEMENT_8,ELEMENT_3:ELEMENT_4}
map_ELEMENT_6 = { ELEMENT_1:ELEMENT_5, ELEMENT_2:ELEMENT_1,ELEMENT_3:ELEMENT_8}

map_ELEMENT_8 = { ELEMENT_1:ELEMENT_1, ELEMENT_2:ELEMENT_2,ELEMENT_3:ELEMENT_3}
map_ELEMENT_7 = { ELEMENT_1:ELEMENT_4, ELEMENT_2:ELEMENT_5,ELEMENT_3:ELEMENT_6}

def main():
    input_parser()
    process()

def input_parser():
    count = 0
    fo = open("C:\\input.txt", "r")
    testcases = int(fo.readline())
    while count < testcases:
        str_case = fo.readline()
        list_case = str_case.split()
        str_case=''
        temp_str = fo.readline()
        temp_count = 0
        temp_str = temp_str.strip()
        while temp_count < int(list_case[1]):
            str_case = str_case + temp_str
            temp_count = temp_count + 1
        list_cases.append(str_case)
        count = count + 1
    fo.close()

def process():
    count=1
    fo = open("C:\\output.txt", "w+")
    result = ELEMENT_7
    for string_case in list_cases:
        #print string_case
        result = sub_process(string_case)
        if result == len(string_case):
            string_data = "Case #%d: YES\n" %(count)
        else:
            string_data = "Case #%d: NO\n" %(count)
        fo.write(string_data)
        count=count+1
    fo.close()

def sub_process(string_case):
    temp=0
    length = len(string_case)
    temp = find_element(ELEMENT_1,string_case,temp)
    #print " Resul1 " + str(temp)
    temp = find_element(ELEMENT_2,string_case,temp)
    #print " Resul2 " + str(temp)
    temp = find_element(ELEMENT_3,string_case,temp)
    #print " Resul3 " + str(temp)
    temp = find_element(ELEMENT_END,string_case,temp)
    return temp

def  find_element(element, string_case, index):
     if index == ELEMENT_7:
         return ELEMENT_7
     length = len(string_case)

     if(element == ELEMENT_END):
         if index >= length:
             return length
     
     if index >= length:
         return ELEMENT_7

     element_1 = string_case[index]
     count=int(index) + 1
     if(element_1 == element):
                 return count
     
     while count < length:
         if(element_1 == element):
             return count
         #print count
         #print len(string_case)
         
         #print element_1
         
         element_2 = string_case[count]
         #print "Element 2"
         #print element_2
         
         if(element_1 == ELEMENT_1):
             element_1 = map_ELEMENT_1[element_2]
         elif(element_1 == ELEMENT_2):
             element_1 = map_ELEMENT_2[element_2]
         elif(element_1 == ELEMENT_3):
             element_1 = map_ELEMENT_3[element_2]
         elif(element_1 == ELEMENT_4):
             element_1 = map_ELEMENT_4[element_2]
         elif(element_1 == ELEMENT_5):
             element_1 = map_ELEMENT_5[element_2]
         elif(element_1 == ELEMENT_6):
             element_1 = map_ELEMENT_6[element_2]
         elif(element_1 == ELEMENT_7):
             element_1 = map_ELEMENT_7[element_2]
         elif(element_1 == ELEMENT_8):
             element_1 = map_ELEMENT_8[element_2]             
         count = count + 1
     if (element == ELEMENT_3) and (element_1 == ELEMENT_3):
             return count
     if(element == ELEMENT_END) and (element_1 == ELEMENT_8):
             return length
     return ELEMENT_7


main()


    
