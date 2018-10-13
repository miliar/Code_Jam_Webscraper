import sys
from math import sqrt

def main():
    f = open(sys.argv[1], 'r+')
    all_lines = f.readlines()

    for i in range(1, len(all_lines)):
        interval = all_lines[i].split(' ')
        valid = []
        for num in range(int(interval[0].strip()), int(interval[1].strip())+1):
            if square(num) and pal(str(num)):
                valid.append(num)
        
        print 'Case #' + str(i) + ': ' + str(len(valid))
                
    
def square(num):
    if sqrt(num).is_integer():
        if pal(str(int(sqrt(num)))):
            return True
    
def pal(num):
    if num == num[::-1]:
        return True




if __name__ == "__main__":
    main()