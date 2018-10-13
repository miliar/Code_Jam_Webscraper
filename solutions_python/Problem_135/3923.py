#! /usr/bin/env python

def main():
    test_case = input()
    for i in range(test_case):
        temp = []
        result = []

        first_row  =  input() 
        for j in range(1, 5):
            temp.append(raw_input().split(" "))
        one = temp[first_row-1]
        one = map(int, one)

        second_row  =  input()
        temp = []
        for j in range(1, 5):
            temp.append(raw_input().split(" "))
        two = temp[second_row-1]
        two = map(int, two)

        result = list(set(one)&set(two))
        if len(result)==0:
            print 'Case #%d: Volunteer cheated!'%(i+1)
        elif len(result)==1:
            print 'Case #%d: '%(i+1), result[0]
        else:
            print 'Case #%d: Bad magician!'%(i+1)

if __name__  ==  '__main__':
    main()
