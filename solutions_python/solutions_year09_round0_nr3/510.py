def acheletra(index, subtexto):
    global count
    for j in xrange(0, len(subtexto)):
        if mensagem[index] == subtexto[j]:
            if (index+1) == len(mensagem):
                count = count + 1
            else:   
                acheletra(index+1, subtexto[j:])

mensagem = 'welcome to code jam'
file = open('C-small-attempt0.in')
file.readline()
count_line = 1
for texto in file:  
    count = 0  
    acheletra(0, texto)
    print "Case #%d: %s"%(count_line,(str(count)[-4:]).zfill(4))
    count_line = count_line + 1
    

