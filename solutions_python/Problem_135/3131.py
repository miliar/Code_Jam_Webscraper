


def main():
    fout = open("magic_out.txt",'w')
    with open("magic.txt")as fin:
        n = int(fin.readline())
        for i in range(n):
            first_answer = int(fin.readline())
            for j in range(first_answer-1):
                fin.readline()
            answer_set = set(fin.readline().strip().split())
            for j in range(first_answer,4):
                fin.readline()
            second_answer = int(fin.readline())
            for j in range(second_answer-1):
                fin.readline()
           
            answer_set = answer_set & set(fin.readline().strip().split())
            for j in range(second_answer,4):
                fin.readline()
            if len(answer_set)==1:
                res = answer_set.pop()
            elif len(answer_set)>1:
                res = "Bad magician!"
            else:
                res = "Volunteer cheated!"
            fout.write("Case #{}: {}\n".format(i+1,res))

if __name__ == '__main__':
    main()
