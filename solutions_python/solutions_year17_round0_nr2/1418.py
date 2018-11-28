"ProblemB Code"

def tidy(num_list):
    for i in range(len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            num_list[i+1:] = [0]*(len(num_list)-(i+1))
            num = list_to_num(num_list)
            num -= 1
            num_list = num_to_list(num)
            return tidy(num_list)

    num = list_to_num(num_list)
    return num # number is sorted

def list_to_num(num_list):
    num = 0
    for i in range(len(num_list)):
        num += 10 ** (len(num_list)-i-1) * num_list[i]
    return num

def num_to_list(num):
    num_string = str(num)
    num_list = [int(j) for j in list(num_string)]
    return num_list

def main():
    t = input()
    for i in range(1,t+1):
        num_string = raw_input()
        num = int(num_string)
        num_list = [int(j) for j in list(num_string)]
        
        num_tidy = tidy(num_list)
        print("Case #{}: {}".format(i,num_tidy))

main()