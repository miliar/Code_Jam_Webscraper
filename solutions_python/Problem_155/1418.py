#python 2.7

import sys

def solve(input_str):
    split_input = input_str.split(" ")
    s_max = int(split_input[0])
    standing = 0
    friends = 0
    print "S_max = " + str(s_max)
    for i in range(0, (s_max + 1)):
        print "Need " + str(i) + " have s:" + str(standing) + " and f:" + str(friends)
        if (standing + friends) < (i):
            add_friend_count = (i - (standing + friends))
            print "Adding friends: " + str(add_friend_count)
            friends += add_friend_count
        standing += int(split_input[1][i])
    return str(friends)   

def main():
    if (not len(sys.argv) == 3):
        print("Need exactly twos args: input filename and output filename")
        return
    input_data = open(sys.argv[1], 'r').read()
    output_file = open(sys.argv[2], 'w')
    split_input = input_data.split("\n")
    case_count = int(split_input[0])
    for i in range(0,case_count):
        res = solve(split_input[i+1])
        output_file.write("Case #" + str(i + 1) + ": " + res + "\n")
    
if __name__ == "__main__":
    main()
