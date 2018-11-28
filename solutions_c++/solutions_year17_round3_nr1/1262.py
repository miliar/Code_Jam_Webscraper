#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;
int R[2009],H[2000];
struct Pan
{
    int R,H;
    bool operator<(const Pan &obj) const{return R>obj.R;}
}pa[2000];
double dp[2000][2000];
#define PI 3.1415926535897932
int main()
{
    ios::sync_with_stdio(false);
    int T,cas=0;
    cin >> T;
    while(T--)
    {
        printf("Case #%d: ",++cas);
        int N,K;
        cin >> N >> K;
        for(int i=1;i<=N;++i)
            cin >> pa[i].R >> pa[i].H;
        pa[0].R=10000000;
        pa[0].H=0;
        sort(pa+1,pa+1+N);

        memset(dp,0,sizeof(dp));
        double ans=pa[1].R*pa[1].R*PI;
        for(int i=1;i<=N;++i)
        {
            dp[i][1]=max(dp[i-1][1],2*PI*pa[i].R*pa[i].H+PI*pa[i].R*pa[i].R);
            for(int j=2;j<=K;j++)
        {
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+2*PI*pa[i].R*pa[i].H);
        }
        ans=max(ans,dp[i][K]);
        }
        printf("%0.9f\n",ans);
    }
    return 0;
}

