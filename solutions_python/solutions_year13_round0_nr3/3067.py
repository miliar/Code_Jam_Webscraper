def square(nbr):
        squared = False
        racine = 0
        for i in range(nbr + 1):
                if i*i == nbr:
                        squared = True
                        racine = i
                        break
        return [squared, racine]

def palindrome(ch):
        if len(ch) < 2:
                return True
        else:
                return (ch[0] == ch[-1]) and palindrome(ch[1:-1])


def main():
        casefile = open("C-small-attempt6.in",'r')
        cases = casefile.read().split()
        for i in range(1,101):
                a = int(cases[2*i - 1])
                b = int(cases[2*i])
                nbrf = 0
                for nbr in range(a,b+1):
                        if palindrome(str(nbr)) and square(nbr)[0] and palindrome(str(square(nbr)[1])):
                                nbrf = nbrf + 1
                outp = "Case #" + str(i) + ": " + str(nbrf) + "\n"
                outputfile = open("output.txt",'a')
                outputfile.write(outp)
        outputfile.close()
