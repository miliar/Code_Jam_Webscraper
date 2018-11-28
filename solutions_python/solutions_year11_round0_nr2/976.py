#!/usr/bin/python
'''
Created on 2011 5 7

@author: cihancimen
'''

def mystr(list):
    str = "["
    for i in range(len(list)):
        if(i != len(list) - 1):
            str += list[i] + ', '
        else:
            str+=list[i]
    str +="]"
    return str

def testcase(test_num):
    line = raw_input()
    cb = {'Q':{}, 'W':{}, 'E':{}, 'R':{} , 'A':{}, 'S':{}, 'D':{}, 'F':{}}
    op = {'Q':set(), 'W':set(), 'E':set(), 'R':set() , 'A':set(), 'S':set(), 'D':set(), 'F':set()}
    count = {'Q':0, 'W':0, 'E':0, 'R':0 , 'A':0, 'S':0, 'D':0, 'F':0}
    parts = line.split(' ')
    num_cb = int(parts[0])
    for i in range(1, num_cb+1):
        c1,c2,i = parts[i]
        cb[c1][c2] = i
        cb[c2][c1] = i
    num_op = int(parts[num_cb+1])
    for i in range(num_cb +2, num_cb+num_op+2):
        el1,el2 = parts[i]
        op[el1].add(el2)
        op[el2].add(el1)
#    print parts
#    print cb
#    print op
    elems = parts[-1]
    st = []
    
    for elem in elems:
        st.append(elem)
        count[elem] +=1
        if(len(st)>1):
            top, rup  = st[-1], st[-2]
            if(top in count):
                if(rup in cb[top]):
                    st = st[:-2]
                    st.append(cb[top][rup])
                    count[top] -= 1
                    count[rup] -= 1
                else:
                    for o in op[top]:
                        if(count[o] > 0):
                            st = []
                            count = {'Q':0, 'W':0, 'E':0, 'R':0 , 'A':0, 'S':0, 'D':0, 'F':0}
                            break;
    print 'Case #%d: %s' % (test_num, mystr(st))

if __name__ == '__main__':
    num_test= int(raw_input())
    for i in range(num_test):
        testcase(i+1)
    pass