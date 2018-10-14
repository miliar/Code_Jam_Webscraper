#coding:utf8



def insert(queue, a,n):
    for item in queue:
        if item[0] == a:
            item[1]+=n
            return
    queue.append([a,n])


#TODO
#gör så att alla consecutive likadana, addas i samma lista, då vinner du
#det finns bara två tal i taget!!!!!!! tänk på det
def main():
    test_cases = int(raw_input())
    for i in range(test_cases):
        #print "\n\ntest_case: " + str(i+1)
        inp = raw_input().split(" ")
        stalls = inp[0]
        people = inp[1]
        #print "stalls: " +str(stalls)
        
        #print "people: " +str(people)
        queue = [[int(stalls),1]]
        #print queue
        a = int()
        b = int()
        j=0
        while j < int(people):
            #print queue
            #print "person " + str(j+1)+": "
            entry = queue.pop(0)
            num = entry[0]
            n = entry[1]
            
            #print "entry: " +str(entry)
            #print "n:"+ str(n)
            #print "\n"
            if(j+n < int(people)):
                j+=n
            else:
                res = int(people) - j
                insert(queue,num,n-(res))#sätt tillbaka n-1
                n=res #n=1
                j+=n 
            if num%2 == 0 and num>1:
                a = num/2
                b = num/2-1
                insert(queue,a,n)
                insert(queue,b,n)
            else:
                if num==0:
                    print "ERROR"
                a = num/2
                b = num/2
                insert(queue,a,2*n)
                
            queue.sort(reverse=True)
        print "Case #" + str(i+1) + ": " + str(a) + " " + str(b)
main()
