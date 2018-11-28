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
��Ŀ������N�����䣬Ҫ��ȥK���ˣ�ÿ����ȥ���˶�Ҫѡ��������˾���Զ�ĸ��䣬Ҳ����ѡ��min(��������������, ���ұ����������)ֵ���ĸ��䣬���������ɸ����ָ��䣬ѡ������Ǹ���Ҫ���ڸ���N��K������£��������һ���˽�����ʱ��max(��������������, ���ұ����������)��min(��������������, ���ұ����������)
˼�룺
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
        for(int i=0;i<K;i++){//��i����
            res_min=-1;
            res_max=-1;
            for(int j=0;j<N;j++){//����ÿһ��λ��
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