#include <bits/stdc++.h>
using namespace std;

#define iOS ios_base::sync_with_stdio(false)
#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%lld",&a)
#define scs(a) scanf(" %s",a)
#define scc(a) scanf(" %c",&a)
#define flsh fflush(stdout)

typedef long long ll;

const int MAX = 1460;
const int INF = 1e7+5;
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

int fa[MAX];
int mo[MAX];
int dp[MAX][MAX/2][2][2];

int solve(int mn,int motaken,int flg,int st)
{
    if(mn == 1440)
    {
        if(motaken == 720)
            return st!=flg;
        return INF;
    }

    if(motaken > 720 || mn-motaken > 720)
        return INF;

    int &ret = dp[mn][motaken][flg][st];

    if(ret != -1)
        return ret;

    ret = INF;

    if(!fa[mn])
        ret = min(ret,solve(mn+1,motaken,0,st)+flg);

    if(!mo[mn])
        ret = min(ret,solve(mn+1,motaken+1,1,st)+!flg);

    return ret;
}


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("sol.txt","w",stdout);
    int t;
    sc(t);

    for(int tc=1;tc<=t;++tc)
    {
        memset(fa,0,sizeof fa);
        memset(mo,0,sizeof mo);
        int n,m;
        sc(n);
        sc(m);
        for(int i=0;i<n;++i)
        {
            int x,y;
            sc(x);
            sc(y);
            for(int j=x;j<y;++j)
                fa[j] = 1;
        }
        for(int i=0;i<m;++i)
        {
            int x,y;
            sc(x);
            sc(y);
            for(int j=x;j<y;++j)
                mo[j] = 1;
        }
        memset(dp,-1,sizeof dp);
        int res = INF;

        if(!fa[0])
            res = min(res,solve(1,0,0,0));
        if(!mo[0])
            res = min(res,solve(1,1,1,1));

        printf("Case #%d: %d\n",tc,res);
    }

    return 0;
}
