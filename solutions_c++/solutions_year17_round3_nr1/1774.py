#include <bits/stdc++.h>

using namespace std;

#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(int i=j;i<=k;i++)
#define REV(i,j,k) for(int i=j;i>=k;i--)
#define FORR(i,j,k,l) for(int i=j;i<=k;i+=l)
#define inf         freopen("in.txt", "r", stdin)
#define outf        freopen("out.txt", "w", stdout)
#define pf          printf
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c)    scanf("%d %d %d", &a, &b, &c)
#define minn          (long long)-1000000000000000000
#define maxx          (long long) 1000000000000000000
#define mod          1000000007
#define PI           3.14159265358979323846  /* pi */
#define LL           long long
#define NL '\n'
#define cnd tree[idx]
#define lnd (idx<<1)
#define rnd ((idx<<1)+1)
#define PB push_back
#define F first
#define S second
#define MK make_pair
#define valid(nx,ny)  ((nx >= 0) && (nx < row) && (ny >= 0) && (ny < col))
typedef pair<long double,long double> pr;

long double dp[1001][1001];
int can[1001][1001];
pr ar[1001];
int n,k;

long double rec(int x,int y)
{
    long double a,b,c;
    if(y==0) return 0;
    if(x==n) return minn;
    if(can[x][y]!=-1) return dp[x][y];
    if(y==k)
    {
       a= 2*PI*ar[x].F*ar[x].S+PI*ar[x].F*ar[x].F;
       //b=PI*ar[x].F*ar[x].F;
       dp[x][y]=max(rec(x+1,y),a+rec(x+1,y-1));
    }
    else
    {
       a= 2*PI*ar[x].F*ar[x].S;
       //b=PI*ar[x].F*ar[x].F;
       dp[x][y]=max(rec(x+1,y),a+rec(x+1,y-1));
    }
    can[x][y]=0;
    return dp[x][y];
}
int main()
{
    ios::sync_with_stdio(false);
    inf;
    outf;
    int tc;
    cin>>tc;
    FOR(tt,1,tc)
    {
        mem(can,-1);
        int i,j;
        long double x,y;
        cin>>n>>k;
        FOR(i,0,n-1) cin>>ar[i].F>>ar[i].S;
        sort(ar,ar+n,greater<pr>());
        x=rec(0,k);
        cout<<"Case #"<<tt<<": ";
        cout<<fixed;
        cout<<setprecision(9)<<x<<NL;
    }
    return 0;
}
