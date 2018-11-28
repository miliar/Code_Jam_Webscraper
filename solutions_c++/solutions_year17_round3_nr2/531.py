#include <bits/stdc++.h>
using namespace std;

#define scan(a) scanf("%d",&a)

typedef long long ll;

const int MX = 1460;
const int INF = 1e7+169;

int GGA[MX];
int GGO[MX];
int dp[MX][MX/2+10][2][2];

int solve(int mn,int GGOtaken,int flg,int st)
{
    if(mn == 1440)
    {
        if(GGOtaken == 720)
            return st!=flg;
        return INF;
    }

    if(GGOtaken > 720 || mn-GGOtaken > 720)
        return INF;

    int &ret = dp[mn][GGOtaken][flg][st];

    if(ret != -1)
        return ret;

    ret = INF;

    if(!GGA[mn])
        ret = min(ret,solve(mn+1,GGOtaken,0,st)+flg);

    if(!GGO[mn])
        ret = min(ret,solve(mn+1,GGOtaken+1,1,st)+!flg);

    return ret;
}


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scan(t);
    for(int tc=1;tc<=t;++tc)
    {
        memset(GGA,0,sizeof GGA);
        memset(GGO,0,sizeof GGO);
        int n,m;
        scan(n);
        scan(m);
        for(int i=0;i<n;++i)
        {
            int x,y;
            scan(x);
            scan(y);
            for(int j=x;j<y;++j)
                GGA[j] = 1;
        }
        for(int i=0;i<m;++i)
        {
            int x,y;
            scan(x);
            scan(y);
            for(int j=x;j<y;++j)
                GGO[j] = 1;
        }
        memset(dp,-1,sizeof dp);
        int ans = INF;

        if(!GGA[0])
            ans = min(ans,solve(1,0,0,0));
        if(!GGO[0])
            ans = min(ans,solve(1,1,1,1));

        printf("Case #%d: %d\n",tc,ans);
    }

    return 0;
}
