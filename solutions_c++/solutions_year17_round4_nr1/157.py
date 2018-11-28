#include <cstdio>
#include <algorithm>
using namespace std;

int p,n;
int g[110];
int dp[5][110][110][110];
void dpinit(){
    fill((int*)dp,(int*)dp+5*110*110*110,-1);
    for(int x = 2 ; x <=4 ; x++){
        dp[x][0][0][0]=0;
    }
    {
        int j = 0;
        int k = 0;
        for(int i = 0 ; i < 101 ; i ++){
            if(i>0){
                int c=0;
                if((i-1+j*2+k*3)%2==0)c=1;
                dp[2][i][j][k]=max(dp[2][i][j][k],dp[2][i-1][j][k]+c);
            }
            if(j>0){
                int c=0;
                if((i+(j-1)*2+k*3)%2==0)c=1;
                dp[2][i][j][k]=max(dp[2][i][j][k],dp[2][i][j-1][k]+c);
            }
            if(k>0){
                int c=0;
                if((i+j*2+(k-1)*3)%2==0)c=1;
                dp[2][i][j][k]=max(dp[2][i][j][k],dp[2][i][j][k-1]+c);
            }
        }
    }
    {
        int k = 0;
        for(int i = 0 ; i < 101 ; i ++){
            for(int j = 0 ; j < 101 ; j ++){
                if(i>0){
                    int c=0;
                    if((i-1+j*2+k*3)%3==0)c=1;
                    dp[3][i][j][k]=max(dp[3][i][j][k],dp[3][i-1][j][k]+c);
                }
                if(j>0){
                    int c=0;
                    if((i+(j-1)*2+k*3)%3==0)c=1;
                    dp[3][i][j][k]=max(dp[3][i][j][k],dp[3][i][j-1][k]+c);
                }
                if(k>0){
                    int c=0;
                    if((i+j*2+(k-1)*3)%3==0)c=1;
                    dp[3][i][j][k]=max(dp[3][i][j][k],dp[3][i][j][k-1]+c);
                }
            }
        }
    }
    {
        for(int i = 0 ; i < 101 ; i ++){
            for(int j = 0 ; j < 101 ; j ++){
                for(int k = 0 ; k < 101 ; k ++){
                    if(i>0){
                        int c=0;
                        if((i-1+j*2+k*3)%4==0)c=1;
                        dp[4][i][j][k]=max(dp[4][i][j][k],dp[4][i-1][j][k]+c);
                    }
                    if(j>0){
                        int c=0;
                        if((i+(j-1)*2+k*3)%4==0)c=1;
                        dp[4][i][j][k]=max(dp[4][i][j][k],dp[4][i][j-1][k]+c);
                    }
                    if(k>0){
                        int c=0;
                        if((i+j*2+(k-1)*3)%4==0)c=1;
                        dp[4][i][j][k]=max(dp[4][i][j][k],dp[4][i][j][k-1]+c);
                    }
                }
            }
        }
    }
}
int main (){
    int T;
    scanf("%d",&T);
    dpinit();
    for(int I = 1 ; I <= T ; I ++){
        scanf("%d%d",&n,&p);
        int x[4]={0};
        for(int i = 0 ; i < n ; i ++){
            int tmp;
            scanf("%d",&tmp);
            x[tmp%p]++;
        }
        //printf("!! %d %d \n",dp[3][2][1][0],x[0]);
        printf("Case #%d: %d\n",I,dp[p][x[1]][x[2]][x[3]]+x[0]);
    }
}
