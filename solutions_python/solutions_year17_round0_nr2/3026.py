
#!/usr/bin/env python3

"""
Tidy Numbers exercise for Code Jam - 2017

Author: Mattia Locatelli
e-mail: mattia.bolob@gmail.com

Developed with Python 3.5.2
"""

def find_max_tidy_num(s_number):
    """
    Find maximun tidy number less than number
    """

    len_input = len(s_number) - 1

    if len_input == 0:
        return s_number

    for i in range(0, len_input):
        if int(s_number[i]) > int(s_number[i+1]):

            final_str = '9' * (len_input - i)
            s_number = s_number[:(i+1)]

            return ''.join([find_max_tidy_num(str(int(s_number)-1)), final_str])

    return s_number


def main():

    """
    Main program entry
    """

    for i in range(1, int(input()) + 1):

        str_num = str(input()) # read a integer number as string
        print("Case #{}: {}".format(i, int(find_max_tidy_num(str_num))))

if __name__ == '__main__':
    main()
