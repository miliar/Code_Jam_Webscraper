#include <bits/stdc++.h>
#define int long long
#define pii pair <int,int>
#define piii pair < pair<int,int> ,int>
#define f first
#define s second
#define pb push_back
#define N 100005
#define mod 1000000007
#define INF 4000000000000000000
#define frew freopen ("C:/Users/Sachin/Desktop/out.txt","w",stdout);
#define frer freopen ("C:/Users/Sachin/Desktop/C-small-attempt0.in","r",stdin);

using namespace std;

double dp[105];
int n;
int dist[105][105];
pii a[105];

double solve(int pos)
{
    if(pos==n-1)
        return 0;
    if(abs(dp[pos]+1) > 0.00001)
        return dp[pos];
    int i=pos+1,cur=dist[pos][pos+1];
    dp[pos]=INF;
    while(i<n && cur <= a[pos].f)
    {
        dp[pos]=min(dp[pos],(((double)cur)/a[pos].s)+solve(i));
        cur+=dist[i][i+1];
        i++;
    }
    return dp[pos];
}

main()
{
    frer;
    frew;
    int t;
    cin>>t;
    for(int w=1;w<=t;w++)
    {
        memset(dp,-1,sizeof(dp));
        int i,j,q;
        cin>>n>>q;
        for(i=0;i<n;i++)
            cin>>a[i].f>>a[i].s;
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                cin>>dist[i][j];
        double ti=0;
        for(i=0;i<q;i++)
        {
            int u,v;
            cin>>u>>v;
            u--,v--;
            ti=solve(0);
        }
        cout<<"Case #"<<w<<": ";
        printf("%.15f\n",ti);

    }
}
