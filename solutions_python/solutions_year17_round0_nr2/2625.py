#-*- coding: utf-8 -*-
def minusone(x):
    x = x-1

    if x < 10:
        return str(x)

    temp_str = ""
    mm = ""
    
    temp = int(str(x)[:-1])

    if str(temp)[-1] == '0':
        mm = minusone(temp)
    else :
        mm = str(temp)
    
    temp_str = mm + str(x)[-1]
    
    return temp_str

def TidyNumbers(x):
    swap_check = False
    x = int(x)
    
    # 10보다 작거나 같은 경우 
    if x == 10:
        x = x-1
    if x < 10:
        return str(x), swap_check
     
    # 10보다 큰 경우
    x_list = list(str(x))

    # 마지막이 0인 경우
    if x_list[-1] == '0':
        x = minusone(x)
        x_list = list(x)

    total_string = ""
    length = len(x_list) # 자릿수
    for i in range(length):
        if i > 0:
            if x_list[i] < x_list[i-1]:
                swap_check = True
                
                x_list[i-1] = str(int(x_list[i-1])-1)
                
                if not(i==1 and x_list[i-1]=='0'):
                    total_string += x_list[i-1]
                    
                for j in range(length-i):
                    total_string += "9"
                    
                return total_string, swap_check
            else :
                if not(i==1 and x_list[i-1]=='0'):
                    total_string += x_list[i-1]
                if i == length-1:
                    total_string += x_list[i]
                
    return total_string, swap_check
                
if __name__ == '__main__':
    f = open("B-large.in")
    f_out = open("output.txt", "w")
    T = int(f.readline())
    for i in range(T):
        # 파일에서 정보 읽기
        x = int(f.readline())
        result = x
        while True:
            result, check = TidyNumbers(result)
            if check == False:
                break
        f_out.write("Case #%d: %s\n" %(i+1, result))
        print(x)
        print("Case #%d: %s\n" %(i+1, result))
    f.close()
    f_out.close()
        
