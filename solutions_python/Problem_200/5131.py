Input_File = open("B-small-attempt0.txt")
Output_File = open("B-small-solution.txt", "w")
Input = Input_File.read()
Input_File.close()
Input = Input.split()
Output = []
T = int(Input[0])
for Test in range(1, T + 1):
    Tidy_Number_Found = False
    N = Input[Test]
    if len(N) == 1:
        Tidy_Number_Found = True
    else:
        while not Tidy_Number_Found:
            for Digit in range(1, len(N)):
                if int(N[Digit - 1]) <= int(N[Digit]):
                    Tidy_Number_Found = True
                else:
                    Tidy_Number_Found = False
                    break 
            N = str(int(N) - 1)  
        N = str(int(N) + 1)
    Output_File.write("Case #" + str(Test) + ": " + N + "\n")
Output_File.close()