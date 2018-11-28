'''
Created on 08 apr 2017

@author: fcerm
'''

if __name__ == '__main__':
    lines = open("input.txt", 'r').readlines()
    out = open("output.txt", 'w');
    for i in range(1,int(lines[0])+1):
        x = lines[i]
        for j in range(int(x),0,-1):
            num = str(j)
            flag = True
            for k in range(0, len(num)-1):
                if int(num[k]) > int(num[k+1]) :
                    flag=False
                    break
            if flag :
                out.write("Case #"+str(i)+": "+str(j)+"\n")
                break
        
                    
    