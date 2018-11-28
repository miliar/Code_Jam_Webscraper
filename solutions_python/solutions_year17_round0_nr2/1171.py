
from random import randint

def largest_tidy_number(digits):  
    for i in reversed(range(0, len(digits)-1)):
        if digits[i] > digits[i + 1]:
            digits[i] = digits[i] - 1
            for j in range(i+1, len(digits)):
                digits[j] = 9
            

def main():
    """ main function """
    number_of_lines = int(input())
    for n in range(1, number_of_lines + 1):
        line = input()
        digits = list(map(int,list(line)))
        largest_tidy_number(digits)
        number = int(''.join(map(str,digits)))
        print("Case #"+str(n)+": " + str(number))



if __name__ == "__main__":
    main()


    