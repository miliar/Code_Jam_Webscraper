#include <bits/stdc++.h>
using namespace std;

#define iOS ios_base::sync_with_stdio(false)
#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%lld",&a)
#define scs(a) scanf(" %s",a)
#define scc(a) scanf(" %c",&a)
#define flsh fflush(stdout)

typedef long long ll;

const int MAX = 1e3+53;
const int INF = 1e9+5;
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

bool prime(int x)
{
    if (x < 2)
        return false;
    for(int i=2; i*i <= x; i++)
        if ((x%i) == 0)
            return false;
    return true;
}

pair<int,int> arr[MAX];
int n,d;

int main()
{
    freopen("A-large (1).in", "r", stdin);
    freopen("sol.txt", "w", stdout);

    int t;
    sc(t);

    for(int tc = 1;tc <= t;++tc)
    {
        sc(d);
        sc(n);
        for(int i=0;i<n;++i)
        {
            sc(arr[i].first);
            sc(arr[i].second);
        }
        sort(arr,arr+n);

        long double mx = 0.0;
        for(int i=n-1;i>=0;--i)
        {
            mx = max(mx,((long double)d-arr[i].first)/arr[i].second);
        }

        printf("Case #%d: ",tc);
        cout<<setprecision(6)<<fixed<<1.0*d/mx<<endl;
    }

    return 0;
}
