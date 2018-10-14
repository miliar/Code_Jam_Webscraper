DEBUG=0


def printd(*arg):
    if DEBUG == 1:
        print("---",arg)

class EmptyStalls:
    def __init__(self, n):
        self.sizes = {n}
        self.stalls = { n:1 }
    def next_empty_stalls(self):
        max_size = max(self.sizes)
        number_of_people = self.stalls[max_size]
        printd("sizes:{}".format(self.sizes))
        printd("stalls:{}".format(self.stalls))
        printd("max:{}, number: {}".format(max_size,number_of_people))
        self.sizes = self.sizes-{max_size}
        del self.stalls[max_size]
        if (max_size%2 == 0):
            s1=max_size//2
            s2=max_size//2 - 1
            if (s1 in self.sizes):
                self.stalls[s1] = self.stalls[s1] + number_of_people
            else:
                self.sizes = self.sizes | {s1}
                self.stalls[s1] = number_of_people
            if (s2 in self.sizes):
                self.stalls[s2] = self.stalls[s2] + number_of_people
            else:
                self.sizes = self.sizes | {s2}
                self.stalls[s2] = number_of_people
            printd("sizes:{}".format(self.sizes))
            printd("stalls:{}".format(self.stalls))
            return number_of_people,s1,s2
        else:
            s1=(max_size-1)//2
            if (s1 in self.sizes):
                self.stalls[s1] = self.stalls[s1] + 2 * number_of_people
            else:
                self.sizes = self.sizes | {s1}
                self.stalls[s1] = 2 * number_of_people
            printd("sizes:{}".format(self.sizes))
            printd("stalls:{}".format(self.stalls))
            return number_of_people,s1,s1

    
t = int(input())  # read a line with a single integer
for case_num in range(1, t + 1):
    n, k =     [int(s) for s in input().split(" ")]
    es=EmptyStalls(n)
    total_people = 0
    s1,s2=0,0
    while total_people < k :
        num,s1,s2=es.next_empty_stalls()
        total_people += num
        printd("total people: {}, s1:{}, s2:{}",total_people,s1,s2)
    print("Case #{}: {} {}".format(case_num,s1,s2))


    
