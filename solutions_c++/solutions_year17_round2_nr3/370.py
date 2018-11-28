#include <bits/stdc++.h>
using namespace std;
#define ll          long long
#define MOD         1000000007
#define ll          long long
#define pb          push_back
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define endl        '\n'
#define PI          3.14159265359d
#define sz(x)       (int)x.size()
#define INF         1e12
ll adj[105][105],dist[105][105];
int n;
double adj2[105][105],dist2[105][105];
void FloydWarshall (ll adj[105][105],ll dist[105][105])
{
    int i, j, k;
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
            dist[i][j] = adj[i][j];
    for (k = 1; k <= n; k++)
        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
                dist[i][j] = min(dist[i][j],(dist[i][k] + dist[k][j]));
}
void FloydWarshall2 (double adj[105][105],double dist[105][105])
{
    int i, j, k;
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
            dist[i][j] = adj[i][j];
    for (k = 1; k <= n; k++)
        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
                dist[i][j] = min(dist[i][j],(dist[i][k] + dist[k][j]));
}
int main()
{
    freopen("C:/Users/User/Desktop/in.txt","r",stdin);
    freopen("C:/Users/User/Desktop/out.txt","w",stdout);
    int t,T,q,i,j;
    pair<ll,ll> A[105];
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>n>>q;
        for(i=1;i<=n;i++)
            cin>>A[i].F>>A[i].S;
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
            {
                cin>>adj[i][j];
                if(i==j)
                    adj[i][j]=0;
                else if(adj[i][j]<0)
                    adj[i][j]=INF;
            }
        FloydWarshall(adj,dist);
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
                if(i==j)
                    adj2[i][j]=0;
                else if(dist[i][j]==INF)
                    adj2[i][j]=INF;
                else if(dist[i][j]>A[i].F)
                    adj2[i][j]=INF;
                else
                    adj2[i][j]=(1.0d*dist[i][j])/A[i].S;
        FloydWarshall2(adj2,dist2);
        cout<<"Case #"<<t<<": ";
        while(q--)
        {
            cin>>i>>j;
            cout<<fixed<<setprecision(8)<<dist2[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
