'''
Created on 2017. 4. 8.

@author: Hyeonsu
'''
def bathroom_stalls(n, k):
    s = []
    s.append(n)
    while k > 0:
        k -= 1
        s.sort(reverse=False)
        j = s.pop()
        if j == 0 :
            break

        ls = int(j/2)
        rs = int((j-1)/2)
        if k==0:
            break
        
        if k%2 == 0:
            k = int(k/2)
            s.append(rs)
        else:
            k = int(k/2+1)
            s.append(ls)
            
    return str(int(ls))+" "+str(int(rs))

if __name__ == '__main__':
    f = open("D:/Download/C-small-2-attempt2.in", 'r')
    n = int(f.readline())
    for i in range(int(n)):
        print_str="Case #"+str(i+1)+": "
        line = f.readline()
        inputs = line.split(" ")
        n = int(inputs[0])
        k = int(inputs[1])
        print_str += bathroom_stalls(n, k)
        print(print_str)
    f.close()
    pass