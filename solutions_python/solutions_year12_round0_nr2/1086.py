#! /usr/local/bin/python
# -*- coding:utf-8 -*-

def read_input_file(file):
    f=open(file,'r')
    T=f.readline() #テストケースの回数
    result=[]
    for i in range(int(T)):
        tmp_data=f.readline().rstrip('\n')
        tmp_list=tmp_data.split(' ')
        N=int(tmp_list[0]) #Googlerの数
        S=int(tmp_list[1]) #surprisingの数
        p=int(tmp_list[2]) #pの値
        scores=[int(i) for i in tmp_list[3:]]
        result.append([N,S,p,scores])
    f.close()
    return result

def solve(input):
    last_result=[] #テストケースの数のサイズをもったlist/各要素はpを超えるGooglerの数の最大値
    for data in input:
        N=data[0]
        S=data[1]
        p=data[2]
        scores=data[3] #scoreはNこの要素を持つlist
        variable_count=0 #+1される可能性のある組の数
        result_count=0
        for score in scores:
            if score==0 or score==1 or score%3==1:
                #scoreが0か1か3で割ったあまりの時はbest_scoreが一意に決定する
                best_score=get_best_score_not_surprise(score)
                if best_score>=p:
                    result_count+=1
            else:
                #scoreがそれ以外の時(soreが0,1ではなく3で割った余りが0か2のとき)はscoreが1上がる可能性がある
                best_score=get_best_score_not_surprise(score)
                if best_score>=p:
                    result_count+=1
                elif best_score==p-1:
                    #best_scoreの上がる余地は1
                    variable_count+=1
        result_count+=min(S,variable_count) #Sとvariable_countの最小値だけp点以上もつgooglerが増える可能性がある
        last_result.append(result_count)

    return last_result

#total_scoreが0,1,3で割った余りが1のときは最大値が一意に確定
#それ以外の時はsurprisingのときとそれ以外で変わる
def get_best_score_not_surprise(total_score):
    if total_score==0:
        return 0
    elif total_score==1:
        return 1
    elif total_score%3==1:
        n=int(total_score/3)
        return n+1
    elif total_score%3==2:
        n=int(total_score/3)
        return n+1 #surprisingのときはn+2
    elif total_score%3==0:
        n=int(total_score/3)
        return n #surprisingのときn+1

def output_text(solve_data):
    f=open('output.txt','w')
    case=1
    for i in solve_data:
        f.write('Case #%s: %s\n' % (case,i))
        case+=1

if __name__=='__main__':
    file_name='B-large.in'
    input=read_input_file(file_name)
    solve_list=solve(input)
    output_text(solve_list)
    #print input
    #print solve_list
