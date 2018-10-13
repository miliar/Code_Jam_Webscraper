# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Shahar"
__date__ ="$08-May-2010 06:16:00$"

def Snapper(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    T = int(fin.readline())
    for iT in range(T):
        numbers = fin.readline().rstrip('\n').split(' ')
        N = int(numbers[0])
        K = int(numbers[1])
        P = (K % (2**N))
        text = 'Case #' + str(iT+1) + ': '
        if P == ((2**N)-1) :
            text = text + 'ON'
        else :
            text = text + 'OFF'
        print text
        fout.write(text + '\n')

if __name__ == "__main__":
    #Snapper(sys.argv[1]);
    #Snapper('C:\\Users\\Shahar\\Projects\\Misc\\LearnPython2\\GCJ2010Qual\\test\\A-test.in');
    #Snapper('C:\\Users\\Shahar\\Projects\\Misc\\LearnPython2\\GCJ2010Qual\\test\\A-small-attempt0.in');
    Snapper('C:\\Users\\Shahar\\Projects\\Misc\\LearnPython2\\GCJ2010Qual\\test\\A-large.in');

