f = open("B-Large.in", 'r')
for index, string in enumerate(f.readlines()):
    string = string.strip()
    number = int(string)
    keepgoing = []
    if index != 0:
        ls =[]
        case = str(index)
        if len(str(string)) == 1:
            print("Case #"+ case +": " + string)
        else:
            for num in string:
                    ls.append(int(num))
            for k in range(len(ls)):
                for i in range(1,len(ls)):
                    if ls[i-1] > ls[i]:
                        ls[i-1]-= 1
                        for x in range(i,len(ls)):
                            ls[x] = 9
                        break
 
                    
            result = [str(x) for x in ls]
            final_number = ''.join(result)
            final_number = int(final_number)
            print("Case #"+ case +": " + str(final_number))



                    
                
                
   
