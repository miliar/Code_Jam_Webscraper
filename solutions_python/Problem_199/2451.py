#-*- coding: utf-8 -*-
def Pancake(x, y):

    flip_count = 0
    x_list = list(x)
    length = len(x_list)

    # Case 2 : 모든 펜케익이 다 + 이면
    if x_list.count('+') == length:
        return str(flip_count)

    # Case 1, 3:
    count = 0
    for i in range(length):        
        if x_list[i] == '-':            
            # 플립해야되는 갯수보다 남은 것인 작은 경우
            if len(x_list[i:]) < y:
                if x_list[i:].count('-') > 0:
                    return "IMPOSSIBLE"
                
            # 같은 경우
            elif len(x_list[i:]) == y:
              if x_list[i:].count('+') > 0:
                    return "IMPOSSIBLE"
            
            # flip
            flip_count += 1
            for j in range(y):
                if  x_list[i+j] == '-':
                    x_list[i+j] = '+'
                else :
                    x_list[i+j] = '-'
    return flip_count
        

if __name__ == '__main__':
    f = open("A-large.in")
    f_out = open("output.txt", "w")
    T = int(f.readline())
    for i in range(T):
        # 파일에서 정보 읽기
        temp = f.readline()
        temp = temp.split()
        x, y = temp[0], int(temp[1])

        result = Pancake(x, y)
        f_out.write("Case #%d: %s\n" %(i+1, result))
    f.close()
    f_out.close()
        
