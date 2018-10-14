import numpy as np
lines = open('B-large.in', 'r').read().splitlines()

case_no= int(lines[0])


def main():
    for num in xrange(case_no):
        tidy_no = lines[num+1]
        while 1:
            tidy_no_list= np.array(list(tidy_no))
            temp= False
            for i in xrange(1, len(tidy_no_list)):
                if not tidy_no_list[i-1] <= tidy_no_list[i]:
                    tidy_no_list[i-1] = int(tidy_no_list[i-1]) - 1
                    tidy_no_list[i:] = 9
                    temp=True
                    tidy_no= list(tidy_no_list)
                    break
            if not temp:
                break

        print 'Case #{}: {}'.format(num+1, int(''.join(tidy_no_list)))

if __name__=='__main__':
    main()