class Snapper:
    def __init__(self, filename):
        self.F=filename
    def checkLight(self, i ,n , k):
        resp= "Case #"+str(i)+": "
        firstL=(2**n) -1
        if k<firstL:
            return resp+"OFF"
        elif k==firstL:
            return resp+"ON"
        else:
            resto= k-firstL
            if resto%(firstL+1)==0:
                return resp+"ON"
            else:
                return resp+"OFF"

    def loadData(self):
        fin=open(self.F,'r')
        fout=open("A-largee.out", "w")
        num=int(fin.readline())
        p=1
        while(p<=num):
            datos=fin.readline()
            cdat= datos.split(" ")
            print p, num
            n=int(cdat[0])
            k=int(cdat[1])
            fout.write(self.checkLight(p, n, k)+ "\n")
            p+=1
        

snaper=Snapper("A-large.in")
snaper.loadData()
