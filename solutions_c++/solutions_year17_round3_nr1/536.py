#include <bits/stdc++.h>
using namespace std;

#define iOS ios_base::sync_with_stdio(false)
#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%lld",&a)
#define scs(a) scanf(" %s",a)
#define scc(a) scanf(" %c",&a)
#define flsh fflush(stdout)

typedef long long ll;

const int MAX = 1011;
const int INF = 1e9+55;
const long long MOD = 1e9+7;
const long double EPS = 1e-7;

long long power (long long a,long long e,long long mod)
{
    if (e == 0)
        return 1ll;
    if (e == 1)
        return a % mod;
    if (e & 1)
        return ((a%mod) * power(a,e-1,mod))%mod;
    else
    {
        long long tmp = power(a,e/2,mod);
        return (tmp*tmp)%mod;
    }
}

long long gcd(long long x,long long y)
{
    return __gcd(x,y);
}

long long lcm(long long x,long long y)
{
    return (x*y)/gcd(x,y);
}

bool prime(ll x)
{
    if (x < 2)
        return false;
    for(ll i=2; i*i <= x; i++)
        if ((x%i) == 0)
            return 0;
    return 1;
}

pair<long double,long double> P[MAX];
const long double pi=acos(-1);
int n,k;
bool ok[MAX][MAX];
long double dp[MAX][MAX];
long double solve(int id,int tk){
    if(tk==k)return 0;
    if(id==n) return -INF;
    if(ok[id][tk])return dp[id][tk];
    long double res=0;
    if(tk==0) res=max(res,pi*P[id].first*P[id].first+P[id].second*2*pi*P[id].first+solve(id+1,tk+1));
    else  res=max(res,P[id].second*2*pi*P[id].first+solve(id+1,tk+1));
    res=max(res,solve(id+1,tk));
    ok[id][tk]=1;
    return dp[id][tk]=res;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("sol.txt","w",stdout);
    int t;
    sc(t);
    for(int tc=1;tc<=t;++tc){
        sc(n);
        sc(k);
        memset(ok,0,sizeof ok);
        for(int i=0;i<n;i++)cin>>P[i].first>>P[i].second;
        sort(P,P+n);
        reverse(P,P+n);
        cout<<"Case #"<<tc<<": ";
        cout<<fixed<<setprecision(9)<<solve(0,0)<<endl;
    }

    return 0;
}
