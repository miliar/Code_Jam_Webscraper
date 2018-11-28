#include<bits/stdc++.h>
#include <ext/numeric>
using namespace std;
#define sc(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sc4(a,b,c,d) scanf("%d%d%d%d",&a,&b,&c,&d)
#define scd(a) scanf("%lf",&a)
#define scd2(a,b) scanf("%lf%lf",&a,&b)
#define scd3(a,b,c) scanf("%lf%lf%lf",&a,&b,&c)
#define scd4(a,b,c,d) scanf("%lf%lf%lf%lf",&a,&b,&c,&d)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ALL(x) x.begin(), x.end()
#define BUFF ios::sync_with_stdio(false);
#define endl "\n"
#define power(a,x) __gnu_cxx::power(a, x)
#define forN(i,n) for(int i=0;i<n;i++)
#define eps 1e-5
#define INF INT_MAX
#define INFLL LLONG_MAX
#define gcd(a,b) __gcd(a,b)
typedef unsigned long long int ull;
typedef long long int ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vector<int> >vvi;
#define MAXN 110
ll e[MAXN];
ll v[MAXN];
ll dist[MAXN][MAXN];
double dp[MAXN][MAXN];
double dpAux[MAXN][MAXN];
bool vis[MAXN][MAXN];
int n,q;
int beg;
double solve(int i,int j)
{

    if(dp[i][j]!=-1)return dp[i][j];
    //cout<<" "<<i<<" "<<j<<endl;
    vis[i][j]=true;
    if(i==beg)
    {
        if(i==j)
        {
            dpAux[i][j]=e[j];
            vis[i][j]=false;
            return dp[i][j]=0;;
        }
        else
        {
            vis[i][j]=false;
            return dp[i][j]=INFLL;
        }
    }
    if(i==j)
    {
        double best=INFLL;
        for(int k=0;k<n;k++)
        {
            if(!vis[i][k])
            {
                double cost=solve(i,k);
                best=min(best,cost);
            }
        }
        if(best==INFLL)
        {
            dp[i][j]=INFLL;
            dpAux[i][j]=-1;
        }
        else
        {
            dp[i][j]=best;
            dpAux[i][j]=e[j];
        }
        vis[i][j]=false;
        return dp[i][j];
    }
    dp[i][j]=INFLL;
    dpAux[i][j]=-1;
    for(int k=0;k<n;k++)
    {
        if(vis[k][j] || dist[k][i]==-1)continue;
        double cost=solve(k,j);
        if(cost==INFLL || dpAux[k][j]-dist[k][i] <0)continue;
        cost=cost+((double)dist[k][i])/v[j]; //tempo gasto
        if(cost< dp[i][j])
        {
            //cout<<cost<<" "<<i<<" "<<j<<endl;
            dp[i][j]=cost;
            dpAux[i][j]=dpAux[k][j]-dist[k][i];
        }
    }
    vis[i][j]=false;
    return dp[i][j];
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
       std::cout << std::fixed;
        std::cout << std::setprecision(6);
    for(int tt=1;tt<=t;tt++)
    {
        cin>>n>>q;
        for(int i=0;i<n;i++)
        {
            cin>>e[i]>>v[i];
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                cin>>dist[i][j];
            }
        }
        cout<<"Case #"<<tt<<": ";

        for(int i=0;i<q;i++)
        {
            for(int j=0;j<n;j++)
            {
                for(int k=0;k<n;k++)
                {
                    dp[j][k]=-1;
                    vis[j][k]=false;
                }
            }
            int v0,vf;
            cin>>v0>>vf;
            v0--;
            vf--;
            beg=v0;
            if(i>0)cout<<" ";
            cout<<solve(vf,vf);
            //cout<<dp[0][0]<<endl;
            //cout<<dp[1][0]<<endl;
        }
        cout<<endl;
    }
    return 0;
}
