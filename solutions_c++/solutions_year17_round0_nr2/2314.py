#include <bits/stdc++.h>
using namespace std;

#define iOS ios_base::sync_with_stdio(false)
#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%lld",&a)
#define scs(a) scanf(" %s",a)
#define scc(a) scanf(" %c",&a)
#define flsh fflush(stdout)

const int MAX = 2e5+3;
const long long INF = 1e18+5;
long long MOD = 1e9+7;

const int MAXN = 11;


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

bool prime(int x)
{
    if (x < 2)
        return false;
    for(int i=2; i*i <= x; i++)
        if ((x%i) == 0)
            return false;
    return true;
}

long long dp[22][3][11];
int num[22];
int k;

long long solve(int id=0,int flg=1,int lst=0)
{
    if(id == k)
        return 0;
    long long &ret = dp[id][flg][lst];
    if(ret != -1)
        return ret;

    ret = -INF;

    int en = 9;
    if(flg)
        en = num[id];

    for(int i=lst;i<=en;++i)
        ret = max(ret,1ll*i*power(10,k-id-1,1e18+5)+solve(id+1,flg&&(i==en),i));

    return ret;
}


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("sol.txt", "w", stdout);

    int t;
    cin>>t;
    for(int ii=1;ii<=t;++ii)
    {
        long long n;
        cin>>n;
        k = 0;
        while(n)
        {
            num[k++] = n%10,n/=10;
        }

        for(int i=0;i<k/2;++i)
            swap(num[i],num[k-i-1]);

        memset(dp,-1,sizeof dp);

        cout<<"Case #"<<ii<<": "<<solve()<<endl;
    }

    return 0;
}


