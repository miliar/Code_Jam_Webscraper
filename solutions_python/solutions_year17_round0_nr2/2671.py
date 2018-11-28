class Tidy:
    def __init__(self, num):
        self.my_num = num

    def is_tidy(self):
        num_list = [d for d in str(self.my_num)]
        for i in range(0, len(num_list)-1):
            ix = int(num_list[i])
            iy = int(num_list[i+1])
            if ix > iy:
                num_list[i] = str(ix - 1)
                for j in range(i+1, len(num_list)):
                    num_list[j] = '9'
                self.my_num = int(''.join(num_list))
                return False
        
        return True

    def get_largest_tidy(self):
        while self.my_num >= 0:
            #print("checking {}".format(self.my_num))
            if self.is_tidy():
                return self.my_num

if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())  # read a list of integers, 2 in this case
        obj = Tidy(n)
        largest_tidy = obj.get_largest_tidy()
        print("Case #{}: {}".format(i, largest_tidy))
        # check out .format's specification for more formatting options