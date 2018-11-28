#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <cmath>
#define r first
#define h second
using namespace std;
long double dp[1005][1005][2];
int N,K,T;
pair<long double,long double> P[1005];
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        cin>>N>>K;
        for(int i=1;i<=N;i++)
            cin>>P[i].r>>P[i].h;
        sort(P+1,P+1+N);
        for(int i=1;i<=N;i++)
        {
            for(int j=1;j<=K&&j<=i;j++)
            {
                dp[i][j][0]=max(dp[i-1][j][0],dp[i-1][j-1][0]+1.0f*2*M_PI*P[i].r*P[i].h);
                dp[i][j][1]=max(dp[i-1][j][1],dp[i-1][j-1][0]+1.0f*M_PI*P[i].r*P[i].r+1.0f*2*M_PI*P[i].r*P[i].h);
            }
        }
        cout<<setprecision(10)<<fixed<<dp[N][K][1]<<"\n";
    }
    return 0;
}
