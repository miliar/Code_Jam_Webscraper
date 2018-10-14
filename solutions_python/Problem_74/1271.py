class cooperative():

    def __init__(self,q):
        self.total = int(q[0])
        self.q = q[1:]
        self.O=1
        self.B=1
        self.O_blocked = False
        self.B_blocked = False
        self.seconds=0
        i=0
        while (i<self.total):
            self.q[2*i+1]=int(self.q[2*i+1])
            i+=1

    def mover (self,number):

        self.turno=self.q[0]

        #print "MOVER:"+self.turno,
        #print self.O_blocked,
        #print self.B_blocked,
        #print str(number)

        if self.turno=='O':
            saltar= abs(number - self.O)

            if self.O_blocked:
                self.pulsar()
                saltar +=1
                self.O_blocked=False
            else:
                #print self.turno + " avanza hasta " + str(number) + "diferencia ",
                self.seconds += saltar
                
                #print "se avanza segundos:"+ str(saltar),
                #print " t: "+str(self.seconds)
                self.O=number
                self.pulsar() 
                saltar +=1
                # actualizo el companero
            nf = self.next_fellow()
            #print "--nf:"+str(nf)
            if nf !=0:
                if self.B_blocked == False:
                    #print "#########"
                    #print str(nf)+" "+ str(self.B) +" " +str(saltar)
                    if nf == self.B:
                        self.B_blocked=True

                    elif abs(nf - self.B) <=saltar:
                        self.B = nf
                        self.B_blocked=True
                    else:
                        self.B= self.B + saltar  if self.B < nf else self.B -saltar
        else:

            saltar= abs(number - self.B)
            if self.B_blocked:
                self.pulsar()
                saltar +=1
                self.B_blocked=False
            else:
                #print self.turno + " avanza hasta " + str(number) + "diferencia ",
                self.seconds += saltar
                #print "se avanza segundos:"+ str(saltar),
                #print "t: "+str(self.seconds)
                self.B=number
                self.pulsar()
                saltar +=1
           
            #import pdb; pdb.set_trace()
 
            nf = self.next_fellow()
            #print "eoooooooooo"+str(nf)
            if nf != 0:
                if self.O_blocked ==False:
                    if nf == self.O:
                        self.O_blocked=True
                    elif abs(nf - self.O) <=  saltar:
                        self.O = nf
                        self.O_blocked=True
                    else:
                        #print self.O
                        #print saltar
                        self.O= self.O + saltar if self.O < nf else self.O -saltar
                        #print self.O
        
    def pulsar(self):
        self.seconds += 1
        #print "pulsado"

    def process(self):
        
        self.turno= self.q[0]
        i=0
        while (i<self.total):
            #print "----------actual: "+ self.q[0] + str(self.q [1])+self.turno
            self.mover(self.q[1])
            #print "B: "+str(self.B)
            #print "O: "+str(self.O)
            self.q=self.q[2:]
            i+=1
        #print "tiempo: "+ str(self.seconds)
        return self.seconds

    def next_fellow(self):
        self.turno = self.q[0]
        nf = 'O' if self.turno == 'B' else 'B' 
        #print "siguiente turno: " + nf,
        nf_n=0
        aa = self.q[2:]
        for i in range(0,len(self.q[2:])/2):
            #print self.q,
            #print self.q[2:],

            if aa[2*i]==nf:
                #print "ok:"+nf
                #print self.q[2*i+1]
                nf_n = aa[2*i+1]
                break
        #print "numero proximo:"+str(nf_n)
        return nf_n

#q = [2,'B', 2, 'O',3]
#q = [4, 'O', 2, 'B', 1, 'B', 2, 'O', 4]
#q = [3, 'O', 5,'O', 8, 'B', 100]
#q = [3, 'B', 5,'B', 8, 'O', 100]
#c = cooperative(q)
#c.process()

#print "a ver"
#c.turno='O'
#print c.next_fellow()

with open('config','r') as f:
    total = f.readline()
    i = 1
    for line in f.readlines():
        q = line.strip().split(' ')
        c = cooperative(q)
    
        result = c.process()
        print "Case #%s: %s" % (i,result)
        i+=1


