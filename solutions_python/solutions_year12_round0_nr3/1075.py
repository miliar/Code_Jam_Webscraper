#! /usr/local/bin/python
# -*- coding:utf-8 -*-

def read_input_file(file):
    f=open(file,'r')
    T=int(f.readline())
    last_data=[]
    for i in range(T):
        tmp_data=f.readline().rstrip('\n')
        tmp_list=tmp_data.split(' ')
        tmp_list=[int(i) for i in tmp_list]
        last_data.append(tmp_list)
    return last_data

def solve(input_data):
    #input_data->[n,m]となるlist
    #nとmは同じ桁数
    n=input_data[0]
    m=input_data[1]

    #1個1個回転させながら調べる，組み合わせの数->ペア候補数-1
    #一度調べた数はテーブルに記録
    dp_num=[] #一度調べた数値の記録用テーブル
    recycle_list=[] #recycledな関係にある数値のグループを記録したリスト[[group1],[group2]]
    for i in range(n,m):
        if i in dp_num:
            continue
        else:
            num_str=str(i)
            group=get_cycle_group(num_str,n,m)
            if len(group)!=1:
                recycle_list.append(group)
                dp_num+=group
    answer=0
    for group_list in recycle_list:
        answer+=count_connect_group(group_list)
    return answer

#数値を入れた時一番頭の数値をしっぽに回転させた数値を返す
def cycle_num_str(num_str):
    new_num_str=num_str[1:]+num_str[0]
    return new_num_str

#nとmは各々下限と上限
def get_cycle_group(num_str,n,m):
    change_num_str=num_str
    result=[int(num_str)]
    while True:
        tmp_num_str=cycle_num_str(change_num_str)
        if tmp_num_str==num_str:
            return result
        if tmp_num_str[0]!='0': #leading zeroがある場合，除去
            tmp_num=int(tmp_num_str)
            if tmp_num>=n and tmp_num<=m: #数値が下限と上限の間に収まっている
                result.append(int(tmp_num_str))
        change_num_str=tmp_num_str

def count_connect_group(group_list):
    n=len(group_list)
    return n*(n-1)/2

def output_text(solve_data):
    f=open('output.txt','w')
    case=1
    for i in solve_data:
        f.write('Case #%s: %s\n' % (case,i))
        case+=1
    f.close()

def run(input_file_name):
    input=read_input_file(input_file_name)
    solve_data=[]
    for data in input:
        solve_data.append(solve(data))
    output_text(solve_data)

if __name__=='__main__':
    input_file_name='C-small-attempt0.in'
    run(input_file_name)
