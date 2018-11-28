import sys

def main():
    in_file = open(sys.argv[1],'r')
    out_file = open('out','w')
    in_file_list = in_file.readlines()
    in_file_list = in_file_list[1:len(in_file_list)]
    case = 0
    for string in in_file_list:
        count = 0
        case+=1
        tmp_list = string.split()
	start = int(tmp_list[0])
	stop = int(tmp_list[1])
	for num in range(start,stop+1):
            orig = num
	    str_num = str(num)
            #out_file.write(str_num+":")
	    while (num != 0):
	        move = num % 10
		num = num/10
                if (num == 0):
                    break
		str_num = str(move)+str_num[0:len(str_num)-1]
                #out_file.write(str_num+', ')
                if (str_num[0] == '0'):
                    continue
		if (int(str_num) >= start and int(str_num) <= stop and int(str_num) > orig):
		    count+=1
                    #out_file.write("recycled, ")
            #out_file.write("\n")
        out_file.write("Case "+"#"+str(case)+": "+str(count)+"\n")
    in_file.close()
    out_file.close()

		
if __name__ == "__main__":
    main()
	        
	        
             
	     
    

