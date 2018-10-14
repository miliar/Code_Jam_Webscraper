#! /usr/bin/python

def gcd(a,b):
    if a < b:
        tmp = a
        a = b
        b = tmp

    if a %b == 0:
        return b
    else:
        return gcd(b,a%b)


#infilename = "testc.in"
infilename = "C-small-attempt1.in"
#infilename = "C-large.in"
outfilename = "C-small.out"
#outfilename = "C-large.out"

f = open("../../"+infilename,"r")
o = open(outfilename,"w")

noCases = int(f.readline())


for case in range(1,noCases+ 1):

        otherplayers = []
        raw_data = f.readline().split(" ")

        numplayers = int(raw_data[0])
        playlow =  int(raw_data[1])
        playhigh = int(raw_data[2])

        raw_data = f.readline().split(" ")

        for n in range(0,numplayers):
            otherplayers.append(int(raw_data[n]))

        noteslist = []
        for othernotes in otherplayers:
            tmplist = []
            for note in range(playlow,playhigh+1):
                if (othernotes%note==0) or (note%othernotes==0) :
                    tmplist.append(note)
            noteslist.append(tmplist)
            
            
        checklist = noteslist[0]
        answer = []


        for chk in checklist:
            answer.append(chk)

        for chk in checklist:
            for idx in range(1,numplayers):
                otherlist = noteslist[idx]

                if not chk in otherlist:
                    answer.remove(chk)
                    break

            
        if len(answer)==0:
            result = "NO"
        else:
            answer.sort()
            result = str(answer[0])
        
	o.write("Case #"+str(case)+": "+ str(result)+"\n")

f.close()
o.close()
