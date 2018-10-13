t = int(input())

def main():
    for i in range(1, t+1):
        num = int(input())
        ans= check(num)
        print("Case #" + str(i) + ": " + ans)


def check(num):

    num_str = str(num)

    cur = int(num_str[0])
    index = 0
    length = len(num_str)



    for j in range(0, length):
        if int(num_str[j]) >= cur:
            cur = int(num_str[j])
            index = j

        else:

            old_num = int(num_str[0:(index+1)])
            rest_zero = length-(index+1)
            magic_num = (old_num * pow(10, rest_zero)) - 1

            return check(magic_num)


    return num_str




if __name__=="__main__":
    main()