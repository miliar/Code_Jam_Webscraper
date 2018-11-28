#include <bits/stdc++.h>
using namespace std;
int T;
int a[2000];
int OP;
int dp[1500][800][2][2];
int vis[1500][800][2][2];
int DP(int i,int num,int s,int e)
{
    if (a[i-1]!=-1 && a[i-1]!=e)
        return 100000000;
    if (i==1440)
    {
        if (num==720)
            return (s!=e);
        return 100000000;
    }
    if (vis[i][num][s][e]==OP)
        return dp[i][num][s][e];
    vis[i][num][s][e]=OP;
    if (num==720)
        return dp[i][num][s][e]=DP(i+1,num,s,1)+(e!=1);
    return dp[i][num][s][e]=min(DP(i+1,num+1,s,0)+(e!=0),DP(i+1,num,s,1)+(e!=1));
}
int main()
{

    freopen("in","r",stdin);
    freopen("out","w",stdout);

    cin>>T;
    for (int tt=1;tt<=T;tt++)
    {
        OP=tt;
        int n,m;
        cin>>n>>m;
        for (int i=0;i<=1440;i++)
            a[i]=-1;
        for (int i=0;i<n;i++)
        {
            int s,e;
            cin>>s>>e;
            for (int j=s;j<e;j++)
                a[j]=0;
        }
        for (int i=0;i<m;i++)
        {
            int s,e;
            cin>>s>>e;
            for (int j=s;j<e;j++)
                a[j]=1;
        }
        printf("Case #%d: ",tt);
        cout<<min(DP(1,0,1,1),DP(1,1,0,0))<<endl;
    }
}

