#import pdb
#import pprint

def number_of_subsequence(needle, haystack):
    if (len(needle) == 1):
        return haystack.count(needle)

    l = [i for i in range(0, len(haystack)-1) if haystack[i]==needle[0]]
    count = 0
    
    for i in l:
        count += number_of_subsequence(needle[1:], haystack[i+1:])

    return count

def main():

    with open(r'F:\Python_tut\CodeJam2009\C-small.in', 'r') as f:
        n = f.readline()
        lines = f.readlines()
        case_num = 0
        for line in lines:
            case_num = case_num + 1
            print('Case #%d: %s' %
                  (case_num, str(number_of_subsequence("welcome to code jam", line)%1000).rjust(4,'0')))

    
#    i = number_of_subsequence("welcome to code jam","wweellccoommee to code qps jam")
#    i = number_of_subsequence("am","amaasafdmm")
#    print(i)

if __name__ == '__main__':
##    pdb.set_trace()
    main()


    
        
        
    
