'''
Code jam 2014: B. Cookie Clicker Alpha
'''
def main():
    f = open('/home/ayush/B-large.in','r')
    o = open("/home/ayush/Downloads/output.txt",'w')
    t=int(f.readline())
    k=0
    while t:
        t-=1
        k+=1
        y = f.readline().split()
        time=0.0
        rate=2.0
        while (float(y[2])/rate > (float(y[0])/rate + float(y[2])/(rate+float(y[1])))):
            time+=float(y[0])/rate
            rate+=float(y[1])
        time+=float(y[2])/rate
        s = 'Case #%d: %.7f\n' %(k,time)
        o.write(s)
main()
