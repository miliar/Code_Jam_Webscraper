import os

def optimal_farms(C,F,X):
    for i in range(10000000):
        t1=X/(2+(F*i))
        
        t2=(X/(2+(F*(i+1))))+(C/(2+(F*i)))
        
        if t2>t1:
            return i

def total_time(C,F,X):
    m_farms=optimal_farms(C,F,X)
    
    t_farm=0
    
    for i in range(m_farms):
        t_farm+=C/(2+(F*i))
        
    t=X/(2+(F*m_farms))
    
    return (t_farm+t)
    
        
def main():

    input=open(r'C:\Users\Nuria\Desktop\CodeJam\ProblemaB\B-large.in','r')
    input.readline()
    
    output=open('C:\Users\Nuria\Desktop\CodeJam\ProblemaB\output_large.txt','w')
    

    case=0
    
    for line in input:
        case+=1
        
        if line[len(line)-1]=='\n':
            line=line[:-1]
        line=line.split(' ')

        C,F,X = float(line[0]),float(line[1]),float(line[2])

        t=total_time(C,F,X)
        
        string= "Case #%d: %.7f\n"%(case,t)
        output.write(string)

if __name__ == "__main__":
    main()