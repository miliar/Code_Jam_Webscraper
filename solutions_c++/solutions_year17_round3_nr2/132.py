#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <tuple>
#include <cmath>
using namespace std;
typedef pair<int,int> P;
typedef tuple<int,int,int> T;

int DP[1441][1441][2][2];//[経過時刻][Cameronが受け持っていた時間][現在Cameron=0,Jamie=1][最初Cameron=0,Jamie=1]の交代回数
bool isbusy[2][1441];//[Cameron=0,Jamie=1][時刻t]:=[t,t+1)の間に仕事があるか否か

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int Ac,Aj;
        cin>>Ac>>Aj;
        fill(isbusy[0],isbusy[2],false);
        for(int i=0;i<Ac;i++){
            int C,D;
            cin>>C>>D;
            for(int t=C;t<D;t++)isbusy[0][t]=true;         
        }
        for(int i=0;i<Aj;i++){
            int J,K;
            cin>>J>>K;
            for(int t=J;t<K;t++)isbusy[1][t]=true;         
        }
        isbusy[0][1440]=isbusy[0][0];
        isbusy[1][1440]=isbusy[1][0];
        fill(DP[0][0][0],DP[1441][0][0],1000);
        if(!isbusy[0][0]){
            DP[0][0][0][0]=0;
        }
        if(!isbusy[1][0]){
            DP[0][0][1][1]=0;            
        }
        for(int t=1;t<=1440;t++){
            for(int c=0;c<=t;c++){
                if(isbusy[0][t]){//Cameronは使えない
                    DP[t][c][0][0]=DP[t][c][0][1]=1000;
                }else{//使える
                    DP[t][c][0][0]=min((c>0?DP[t-1][c-1][0][0]:1000),DP[t-1][c][1][0]+1);
                    DP[t][c][0][1]=min((c>0?DP[t-1][c-1][0][1]:1000),DP[t-1][c][1][1]+1);
                }
                if(isbusy[1][t]){//Jamieは使えない
                    DP[t][c][1][0]=DP[t][c][1][1]=1000;
                }else{//使える
                    DP[t][c][1][0]=min(DP[t-1][c][1][0],(c>0?DP[t-1][c-1][0][0]+1:1000));
                    DP[t][c][1][1]=min(DP[t-1][c][1][1],(c>0?DP[t-1][c-1][0][1]+1:1000));
                }
            }
        }
        int ans=min({DP[1440][720][0][0],DP[1440][720][0][1]+1,DP[1440][720][1][0]+1,DP[1440][720][1][1]});
        printf("Case #%d: %d\n",t,ans);
    }

    return 0;
}