__author__ = 'chamathsilva'


data = [10,5,15,5]

data2 = [23,90,40,0,100,9]

rate = 0

def method_one(lst):
    global rate
    total_one = 0
    max_rate = 0

    for i in range (len(lst)-1):
        temp = lst[i+1] - lst[i]

        if temp < 0:
            total_one +=temp
            if temp < max_rate:
                max_rate = temp

    rate = abs(max_rate)
    return abs(total_one)


def method_two(lst):
    global rate
    total_two = 0

    for i in range (len(lst)-1):
        temp = lst[i]
        if temp > rate:
            total_two += rate
        else:
            total_two += temp

    return total_two


def get_input():
    out_string = ""
    input_file =open('A-large.in.txt', 'r')
    N = int(input_file.readline())

    for i in range(N):
        grabage = input_file.readline()

        temp = [int(i) for i in input_file.readline().split()]

        out_string += str("Case #") + str(i+1)+str(": ")+str(method_one(temp))+str(" ")+str(method_two(temp))+str("\n")
    output_file = open('output_file11111.out','w')
    output_file.write(out_string)




if __name__ == "__main__":
    get_input()







print(method_one(data))
print(method_two(data))
print(method_one(data2))
print(method_two(data2))
