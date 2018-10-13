__author__ = 'TM'
file = open('A-small-attempt0.in','r')
out=open('output.out','w+')
samples=int(file.readline())

def read():

    answer=file.readline().strip()
    row=int(answer)

    for x in range(row-1):
        file.readline()

    sqre=file.readline().split()

    for x in range(4-row):
        file.readline()

    return  sqre

for line in range(samples):
    shuffle_1=read()
    shuffle_2=read()


    occurence=0
    card_no=None
    for card in shuffle_1:
        if card in shuffle_2:
            occurence +=1
            card_no=card
    if occurence==1:
        out.writelines ("Case #"+str(line+1)+": "+card_no+"\n")
    elif occurence>1:
        out.writelines ("Case #"+str(line+1)+":"+" Bad magician!"+"\n")
    else:
        out.writelines("Case #"+str(line+1)+":"+" Volunteer cheated!"+"\n")
  