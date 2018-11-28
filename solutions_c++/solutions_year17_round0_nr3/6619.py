#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <climits>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <list>
using namespace std;
int T=0;
int N, K;
/*
题目：厕所N个隔间，要进去K个人，每个进去的人都要选择和其他人尽量远的隔间，也就是选出min(离左边人最近距离, 离右边人最近距离)值最大的隔间，若果有若干个这种隔间，选最左边那个。要求在给出N和K的情况下，给出最后一个人进厕所时的max(离左边人最近距离, 离右边人最近距离)和min(离左边人最近距离, 离右边人最近距离)
思想：
*/

int tran_max(int a){
    return a/2;
}
int tran_min(int a){
    
    return (a-1)/2;
}

int rem[3000];
int need[3000];
int main(){
    freopen("C-small-1-attempt2.in","r",stdin);  
    //freopen("B-large.in","r",stdin);  
    freopen("out0.txt","w",stdout); 
    //freopen("out0-large.txt","w",stdout); 
    
    scanf("%d",&T);
    
    int res_max, res_min;
    for(int i=1; i<=T; i++){
        /*
        scanf("%d %d",&N,&K);
        queue<int> Q_max;
        queue<int> Q_min;
        Q_max.push(tran_max(N));
        Q_min.push(tran_min(N));
        int k = 0;
        while(!Q_max.empty()){
            int size = Q_max.size();

            for(int j=0; j<size; j++){
                int head_max = Q_max.front();Q_max.pop();
                int head_min = Q_min.front();Q_min.pop();
                res_max = head_max;
                res_min = head_min;
                //printf("head_max=%d, head_min=%d\n", head_max, head_min);
                k++;
                if(k>=K)
                    goto END;
                if(head_max!=0){
                    Q_max.push(tran_max(head_max));
                    Q_min.push(tran_min(head_max));
                }
                if(head_min!=0){
                    Q_max.push(tran_max(head_min));
                    Q_min.push(tran_min(head_min));
                }
            }
        }

    END:
        printf("Case #%d: %d %d\n", i, res_max, res_min);
        */
        
        for(int i=0;i<3000;i++){
            rem[i]=0;
        }
        scanf("%d %d",&N,&K);
        int final = 0, res_min=0, res_max=0;
        for(int i=0;i<K;i++){//第i个人
            res_min=-1;
            res_max=-1;
            for(int j=0;j<N;j++){//遍历每一个位置
                //printf("%d\n",rem[j]);
                if(rem[j]!=0){
                    continue;
                }
                int left=0, right=0;
                for(int k=j-1; k>=0; k--){
                    if(rem[k]!=0)
                        break;
                    else 
                        left++;
                }
                for(int k=j+1; k<N; k++){
                    if(rem[k]!=0)
                        break;
                    else 
                        right++;
                }
                
                int smaller = min(left, right);
                int bigger = max(left, right);
                if(smaller>res_min){
                    final = j;
                    res_min = smaller;
                    res_max = bigger;
                }else if(smaller==res_min && bigger>res_max){
                    final = j;
                    res_min = smaller;
                    res_max = bigger;
                }
                //cout<<left<<' '<<right<<"saf"<<endl;
            }
            //printf("asdf");
            rem[final]=1;
            //printf("%d %d %d\n",final,max,min);
        }
        printf("Case #%d: %d %d\n",i,res_max,res_min);
    }
    return 0;
}