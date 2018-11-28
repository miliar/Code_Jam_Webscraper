#include <bits/stdc++.h>
using namespace std;

#define iOS ios_base::sync_with_stdio(false)
#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%lld",&a)
#define scs(a) scanf(" %s",a)
#define scc(a) scanf(" %c",&a)
#define flsh fflush(stdout)

const int MAX = 1e3+6;
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

char in[MAX];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("sol.txt", "w", stdout);

    int t;
    sc(t);
    for(int tc=1;tc<=t;++tc)
    {
        scs(in);
        int n = strlen(in);
        int k;
        sc(k);

        int res = 0;
        bool ok = 1;
        for(int i=0;i<n;++i)
        {
            if(in[i] == '-')
            {
                if(i+k > n)
                    ok = 0;
                else
                {
                    ++res;
                    for(int j=i;j<i+k;++j)
                        if(in[j] == '+')
                            in[j] = '-';
                        else
                            in[j] = '+';
                }
            }
        }

        if(ok)
            printf("Case #%d: %d\n",tc,res);
        else
            printf("Case #%d: IMPOSSIBLE\n",tc);
    }

    return 0;
}


