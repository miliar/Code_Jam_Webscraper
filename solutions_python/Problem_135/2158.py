def main():
    file = open('1.txt','r')
    file_out = open('1_output.txt','w')

    test_cases = int(file.readline())

    for test in range(1,test_cases+1):
        answer1 = int(file.readline())-1
        row1 = file.readline().split()
        row2 = file.readline().split()
        row3 = file.readline().split()
        row4 = file.readline().split()
        grid1 = [row1,row2,row3,row4]

        answer2 = int(file.readline())-1
        row1 = file.readline().split()
        row2 = file.readline().split()
        row3 = file.readline().split()
        row4 = file.readline().split()
        grid2 = [row1,row2,row3,row4]

        if len(set(grid1[answer1]+grid2[answer2]))==len(grid1[answer1]+grid2[answer2]):
            file_out.write("Case #"+str(test)+": Volunteer cheated!\n")

        elif len(set(grid1[answer1]+grid2[answer2]))<len(grid1[answer1]+grid2[answer2])-1:
            file_out.write("Case #"+str(test)+": Bad magician!\n")
        else:
            found = False
            number = 0

            for num in grid1[answer1]:
                if num in grid2[answer2]:
                    found = True
                    number = grid2[answer2][grid2[answer2].index(num)]
            if found:
                file_out.write("Case #"+str(test)+": "+str(number)+"\n")

    file.close()
    file_out.close()

main()