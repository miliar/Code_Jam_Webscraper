

#from http://en.wikipedia.org/wiki/List_of_prime_numbers#The_first_500_prime_numbers
primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]
def factors(n,b,p):
    r=set()
    for x in primes:
        if not n%x and x>=p:
            r.add(x)
    return r

def go():
    f=open('2.txt')
    case=0
    for x in range(int(f.readline())):
        case+=1
        t=f.readline().split()
        a=int(t[0])
        b=int(t[1])
        p=int(t[2])
        l=range(a,b+1)
        #print l
        l=[factors(x,b,p) for x in l]
        #print l

        changed=1
        while changed:
            changed=0
            x=0
            while 1:                
                if x==len(l):
                    break
                y=0
                while 1:                    
                    if y==len(l):
                        break
                    if x!=y and l[x].intersection(l[y]):
                        l[x]=l[x].union(l[y])
                        del l[y]
                        changed=1
                    else:
                        y+=1
                x+=1
        print 'Case #%d: '%case,len(l)
                        


go()
