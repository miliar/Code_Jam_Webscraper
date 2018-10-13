import math

def main():
    print("hi")
    
    f = open('D-small-attempt10.in', 'r')
    numberOfProblems = int(f.readline())
    out = open('D-small-attempt10.out','w')
    for x in range(0,numberOfProblems):
        inp = f.readline()
        X,R,C = inp.split(" ")
        X = int(X)
        R = int(R)
        C = int(C)
        answer = ""
        remain = (R * C - X)
        if remain >= 0 and remain%X == 0:
            if X == 4 and (R<4 and C<4):
                answer = "RICHARD"
            elif X == 4 and (R==1 or C==1):
                answer = "RICHARD"
            elif X == 4 and (R==2 or C==2) and (R==4 or C==4):
                answer = "RICHARD"
            elif X==3 and (R==1 or C ==1):
                answer = "RICHARD"
            else: 
                answer = "GABRIEL"
        else:
            answer = "RICHARD"


            


        #write answer to out
        out.write("Case #" + str(x+1) + ": " + str(answer) + "\n")



    f.close()
    out.close()



if __name__ == "__main__":
    main()
