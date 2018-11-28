#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<iostream>
#include<algorithm>
using namespace std;

const int maxn = 25*65;

int dp[maxn][maxn/2][2][2];
int can[maxn];

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;scanf("%d",&T);
    int CASE = 0;
    while(T--){
        memset(can,-1,sizeof can);
        int M = 24*60;
        int n1,n2,a,b;
        scanf("%d%d",&n1,&n2);
        while(n1--){
            scanf("%d%d",&a,&b);
            for(int i=a;i<b;i++)
                can[i] = 0;
        }
        while(n2--){
            scanf("%d%d",&a,&b);
            for(int i=a;i<b;i++)
                can[i] = 1;
        }
        memset(dp,-1,sizeof dp);
        dp[1][1][0][0] = 0;
        dp[1][0][1][1] = 0;
        for(int i=0;i<M;i++)
            for(int j=0;j<=min(M/2,i);j++)
                for(int s1=0;s1<2;s1++)
                    for(int s2=0;s2<2;s2++){
                        if( can[i] != -1 && can[i] != s2 )
                            continue;
                        if( dp[i][j][s1][s2] == -1 )
                            continue;
                        for(int s3=0;s3<2;s3++){
                            int jj = s3?j:j+1;
                            int t = (s2==s3)?dp[i][j][s1][s2]:dp[i][j][s1][s2]+1;
                            if( dp[i+1][jj][s1][s3] == -1 )
                                dp[i+1][jj][s1][s3] = t;
                            dp[i+1][jj][s1][s3] = min(dp[i+1][jj][s1][s3],t);
                        }
                    }
        int Ans =1e9+7;
        for(int s=0;s<2;s++)
            if( dp[M][M/2][s][s] != -1 )
                Ans = min(dp[M][M/2][s][s],Ans);
        printf("Case #%d: %d\n",++CASE,Ans);
    }
    return 0;
}
