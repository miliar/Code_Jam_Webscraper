#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>
#include <cmath>
using namespace std;

bool tag[2][1444];
int dp[1444][722][2][2];
int main()
{
    freopen("data.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        memset(tag,false,sizeof(tag));
        memset(dp,0x3f,sizeof(dp));
        int AC,AJ;
        scanf("%d%d",&AC,&AJ);
        for(int i=0;i<AC;i++){
            int s,t;
            scanf("%d%d",&s,&t);
            for(int j=s;j<t;j++) tag[0][j]=true;
        }
        for(int i=0;i<AJ;i++){
            int s,t;
            scanf("%d%d",&s,&t);
            for(int j=s;j<t;j++) tag[1][j]=true;
        }
        //now remain member
    for(int l=0;l<2;l++)
        for(int i=0;i<1440;i++){
            for(int j=0;j<720;j++){
                for(int k=0;k<2;k++){
                    if(tag[k^1][i]) continue;
                    if(i==0&&j==0){
                        if(l==k)
                        dp[i][j+1][k][l]=1;
                    }
                    else if(i==1439){
                        dp[i][j+1][k][l]=min(dp[i-1][j][k][l],dp[i-1][i-j][k^1][l]+1);
                        if(k==l)
                            dp[i][j+1][k][l]--;
                    }
                    else{
                        dp[i][j+1][k][l]=min(dp[i-1][j][k][l],dp[i-1][i-j][k^1][l]+1);
                    }
                }
            }
        }
        int res=0x3f3f3f3f;
        for(int i=0;i<2;i++)
            for(int j=0;j<2;j++)
                res=min(dp[1439][720][i][j],res);
        printf("Case #%d: %d\n",kase,res);
    }
    return 0;
}
