#include <cstdio>
#include <algorithm>
#include <cassert>
using namespace std;


int A,B;
int X[10][2], Y[10][2];

int dp[1500][800][2][2];
int mapA[1500], mapB[1500];

int f(int curr, int sum1, int now, int start){
    if(curr == 1440 && sum1 == 720){
        return now != start;
    }
    if(sum1 > 720) return 1e9;
    if(curr - sum1 > 720) return 1e9;
    if(now == 0 && mapA[curr] == 1) return 1e9;
    if(now == 1 && mapB[curr] == 1) return 1e9;

    if(dp[curr][sum1][now][start] != 0) return dp[curr][sum1][now][start];


    int min_ans = 1e9;
    if(now == 0){
        if(!mapA[curr]){
            min_ans = min(min_ans, f(curr+1,sum1+1,now, start));
            min_ans = min(min_ans, 1 + f(curr+1,sum1,!now, start));
        }else{
            min_ans = min(min_ans, 1 + f(curr+1,sum1,!now, start));
        }
    }else{
        if(!mapB[curr]){
            min_ans = min(min_ans, f(curr+1,sum1,now, start));
            min_ans = min(min_ans, 1 + f(curr+1,sum1+1,!now, start));
        }else{
            min_ans = min(min_ans, 1 + f(curr+1,sum1+1,!now, start));
        }
    }
    
    // if(min_ans < 10 && min_ans > 0) printf("[%d][%d][%d] = %d\n",curr,sum1,now,min_ans); 
    return dp[curr][sum1][now][start] = min_ans;
}

void run(){
    memset(mapA,0,sizeof mapA);
    memset(mapB,0,sizeof mapB);
    scanf("%d %d",&A,&B);
    for(int i=1;i<=A;i++){
        scanf("%d %d",&X[i][0], &X[i][1]);
        for(int j=X[i][0];j<X[i][1];j++) mapA[j%1440] = 1;
    }
    for(int i=1;i<=B;i++){
        scanf("%d %d",&Y[i][0], &Y[i][1]);
        for(int j=Y[i][0];j<Y[i][1];j++) mapB[j%1440] = 1;
    }
    memset(dp,0,sizeof dp);
    int ans = min(f(0,0,0,0),f(0,0,1,1));
    // if(ans > 2) ans--;
    printf("%d\n",ans);
}

int main(){
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        run();
    }
    return 0;
}