#!/usr/bin/env python3

def magic_trick(first_answer, first_array, second_answer, second_array):
    answers1=set(first_array[first_answer-1])
    answers2=set(second_array[second_answer-1])
    return answers1 & answers2

def output_parser(answers):
    if len(answers)==1:
        return str(answers.pop())
    elif len(answers)>1:
        return "Bad magician!"
    elif len(answers)==0:
        return "Volunteer cheated!"

def file_parser(filename):
    fo=open(filename)
    cases=[]
    test_cases=int(next(fo).strip())
    for case in range(test_cases):
        a1=int(next(fo).strip())
        arr1=[]
        for j in range(4):
            arr1.append([int(i) for i in next(fo).strip().split()])
        a2=int(next(fo).strip())
        arr2=[]
        for j in range(4):
            arr2.append([int(i) for i in next(fo).strip().split()])
        cases.append((a1,arr1,a2,arr2))
    return cases

def main(filename):
    cases=file_parser(filename)
    for num,case in enumerate(cases):
        print("Case #{0}: {1}".format(num+1, output_parser(magic_trick(*case))))

if __name__=="__main__":
    from sys import argv
    main(argv[-1])
