'''
Created on April 30 2016

@author: elmoatasem
'''





int2Str = lambda x:str(x) # map(int2Str,[1,2]) :  [1,2] > ['1', '2']
intList2StringList = lambda x:  map(str,x) #map(intList2StringList, [[1,3,4],[4,5,4]]) : [[1, 3, 4], [4, 5, 4]] > [['1', '3', '4'], ['4', '5', '4']]
strList2IntList = lambda x:  map(int,x)#map(strList2IntList, [['1', '3', '4'], ['4', '5', '4']]) : [['1', '3', '4'], ['4', '5', '4']] >  [[1, 3, 4], [4, 5, 4]]
strList2Str = lambda x: "".join(x) # map(strList2Str, [['1','2'],['3','4']]) : [['1','2'],['3','4']] > ['12', '34']
intList2Int = lambda x: int(strList2Str(map(int2Str,x)))# map(intList2Int, [[1,2,4,3],[6,7,8,9]]) : [[1,2,4,3],[6,7,8,9]] > [1243, 6789]
str2StrList = lambda x: list(x) # map(str2StrList, ['12','34']) : ['12','34'] > [['1', '2'], ['3', '4']] 
int2IntList = lambda x:  map(int,str2StrList(int2Str(x)))# map(Int2IntList, [123,44]):  [123,44] > [[1, 2, 3], [4, 4]]
make2DList = lambda rows,columns : [[0 for x in range(columns)] for x in range(rows)] # make2DList(r = 3,c = 5) [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        
            
                
def solve(D,N,horses): 
    speed = []
    for i in range(len(horses)):
        (Ki,Si) = horses[i]
        Ti = (D - Ki)*1.0 / Si
        speed.append(Ti)
    print speed
    if(max(speed) > 0):
        return D/max(speed)*1.0  
    else:
        return D/max(speed)*1.0 
    
    



f_r = open('A-large_1.in',"r")
n_test=int(f_r.readline().strip()) 
f_w = open("A2.out", "w")
result = ""
for i in range(n_test):
    D,N =  map(int,f_r.readline().split())
    horses = []
    for j in range(N):
        Ki,Si =  map(int,f_r.readline().split())
        horses.append((Ki,Si))
    print horses
    result = solve(D,N,horses)
    print result
    output_str='Case #{itr}: {res}'.format(itr=(i+1),res=result)
    f_w.write(output_str+'\n')
    
f_r.close()
















