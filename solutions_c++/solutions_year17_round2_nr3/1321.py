#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<iomanip>
#include<map>
#define ll long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define tr(v,it) for(auto it=v.begin();it!=v.end();it++)
#define int long long
using namespace std;
int maxd[102],sp[102];
int graph[102][102],dis[102][102];
int inf=1e15;
void floydwarshall(int n)
{
    int i,j,k;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
            dis[i][j]=graph[i][j];
    }
    for(k=0;k<n;k++)
    {
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j]);
            }
        }
    }
}
double dp[102][102],bestdp[102][102];
void solve(int n)
{
    int i,j,k;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            bestdp[i][j]=inf;
            for(k=0;k<n;k++)
            {
                dp[i][j]=inf;
            }
        }
    }
    for(k=0;k<n;k++)
    {
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(i==j)
                {
                    dp[i][j]=0.0;
                    continue;
                }
                if(maxd[k]>=dis[k][j])
                    dp[i][j]=min(dp[i][j],dp[i][k]*1.0+(dis[k][j]*1.0/sp[k]*1.0));
            }
        }
    }
}
main()
{
//    freopen("data.txt","r",stdin);
    //freopen("data5.in","r",stdin);
    //freopen("out6.txt","w",stdout);
    int t,l1=0;
    cin>>t;
    while(t--)
    {
        l1++;
        int n,m,i,j,k,l,q;
        cin>>n>>q;
        for(i=0;i<n;i++)
        {
            cin>>maxd[i]>>sp[i];
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                cin>>graph[i][j];
                if(graph[i][j]==-1)
                    graph[i][j]=inf;
                if(i==j)
                    graph[i][j]=0;
            }
        }
        floydwarshall(n);
        cout<<"Case #"<<l1<<": ";
     /*   for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                cout<<dis[i][j]<<" ";
            }
            cout<<"\n";
        }*/
        solve(n);
        while(q--)
        {
            int x,y;
            cin>>x>>y;
            x--;
            y--;
            cout<<setprecision(12)<<dp[x][y]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
