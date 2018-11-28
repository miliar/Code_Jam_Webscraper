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

int n;
long double arr[55],u,k;

int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("sol.txt","w",stdout);
    int t;
    sc(t);

    for(int tc=1; tc<=t; tc++)
    {
        sc(n);
        cin>>k>>u;
        for(int i=0; i<n; i++)
            cin>>arr[i];
        arr[n]=1;
        sort(arr,arr+n+1);
        long double sm=0,nn=n,opts;
        int opt=n-1;
        for(int i=0; i<=n; i++)
        {
            long double ii = i;
            if(ii*arr[i]-sm>u||i==n)
            {
                opt=i-1;
                opts=sm;
                break;
            }
            sm+=arr[i];
        }
        for(int i=0; i<=opt; i++)
        {
            arr[i]=(u+opts)/((long double)opt+1);
        }
        long double ans=1;
        for(int i=0; i<=n; i++)
            ans*=arr[i];
        cout<<fixed;
        cout.precision(6);
        cout<<"Case #"<<tc<<": "<<ans<<"\n";
    }

    return 0;
}
