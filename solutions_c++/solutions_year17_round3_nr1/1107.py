#include <bits/stdc++.h>
#define pi acos(-1)
#define pii pair<int,int>
#define f first
#define s second
#define mp make_pair
#define inf 1000000000000000000000000000.0
using namespace std;
const int N = 1005;
int n,k;
vector<pii> rh;
int t;
double dp[N][N];

double surbas(int r)
{
    return (double)r*(double)r*pi;
}
double surlat(int r,int h)
{
    return (double)r*(double)h*2.0*pi;
}

double fun(int ind,int rem)
{
    if(!rem) return 0;
    if(ind>=n) return -inf;
    if(dp[ind][rem] != -1.0) return dp[ind][rem];
    double ans(0);
    int r = rh[ind].f;
    int h = rh[ind].s;
    //cout<<r<<" "<<h<<" "<<
    if(rem == 1)
    {
        return dp[ind][rem] = surlat(r,h);
    }
    for(int i=ind+1;i<n;i++)
    {
        double sur = surlat(r,h);
        ans = max(ans,sur + fun(i,rem-1));
    }
    return dp[ind][rem] = ans;
}

int main()
{
    ifstream cin("A-large(1).in");
    ofstream cout("out");
    cin>>t;
    int tc(1);
    while(t--)
    {
        cin>>n>>k;
        rh.clear(); rh.resize(n);
        for(int i=0;i<n;i++)
        {
            int r,h;
            cin>>r>>h;
            rh.push_back(mp(r,h));
        }
        sort(rh.rbegin(),rh.rend());
        for(int i=0;i<=n;++i)
        {
            for(int j=0;j<=n;++j) dp[i][j] = -1.0;
        }
        double out = 0.0;
        for(int i=0;i<n-k+1;i++)
        {
            out = max(out, surbas(rh[i].f) + fun(i,k));
        }
        cout<<"Case #"<<tc++<<": ";
        cout<<fixed<<setprecision(9)<<out<<endl;
        //return 0;
    }
    return 0;
}
