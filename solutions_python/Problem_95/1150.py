#! /usr/local/bin/python
# -*- coding:utf-8 -*-

def read_input_file(file):
    f=open(file,'r')
    T=f.readline() #テストケースの数

    result=[]
    #テストケース分ループする
    for i in range(int(T)):
        tmp_data=f.readline()
        tmp_data=tmp_data.rstrip('\n')
        result.append(tmp_data)
    
    f.close()
    return result


def solve(input):
    change_dict={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
    
    result=[]
    for string in input:
        tmp_str=''
        for i in range(len(string)):
            if string[i]==' ':
                tmp_str+=' '
            else:
                tmp_str+=change_dict[string[i]]
        result.append(tmp_str)
    return result

def output_text(solve):
    f=open('output.txt','w')
    case=1
    for string in solve:
        f.write('Case #%s: %s\n' % (case,string))
        case+=1
    f.close()

if __name__=='__main__':
    file='A-small-attempt2.in'
    input=read_input_file(file)
    solve_list=solve(input)
    output_text(solve_list)
    print input
    print solve_list
