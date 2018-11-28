__author__ = 'Sirna'


def main():
    f=open("A-small-attempt1.in")
    f2=open("a.out","w")
    cases=(int)(f.readline())
    for i in range(cases):
        rowno1=(int)(f.readline())
        for j in range(rowno1-1):
            f.readline()
        first=set(f.readline().split())
        for j in range(4-rowno1):
            f.readline()
        rowno2=(int)(f.readline())
        for j in range(rowno2-1):
            f.readline()
        second=set(f.readline().split())
        for j in range(4-rowno2):
            f.readline()
        result=first.intersection(second)
        if(len(result)<1):
            f2.write("Case #"+(str)(i+1)+": Volunteer cheated!\n")
        elif(len(result)==1):
            f2.write("Case #"+(str)(i+1)+": "+result.pop()+"\n")
        else:
            f2.write("Case #"+(str)(i+1)+": Bad magician!\n")


if __name__=="__main__":
    main()