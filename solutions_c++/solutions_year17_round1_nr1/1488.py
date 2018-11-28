#include <bits/stdc++.h>
using namespace std;

#define iOS ios_base::sync_with_stdio(false)
#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%lld",&a)
#define scs(a) scanf(" %s",a)
#define scc(a) scanf(" %c",&a)
#define flsh fflush(stdout)

const int MAX = 1e5+6;
const int INF = 2e9+5;
const long long MOD = 1e9+7;

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

char in[44][44];
int r,c;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("sol.txt", "w", stdout);

    int t;
    sc(t);

    for(int tc=1;tc<=t;++tc)
    {
        sc(r);
        sc(c);
        for(int i=0;i<r;++i)
            for(int j=0;j<c;++j)
                scc(in[i][j]);
        for(int i=0;i<r;++i)
        {
            int k = 0;
            for(int j=0;j<c;++j)
            {
                if(in[i][j] != '?')
                {
                    while(k<c && (in[i][k]=='?' || in[i][k] == in[i][j]))
                    {
                        in[i][k] = in[i][j];
                        ++k;
                    }
                }
            }
        }
        for(int i=0;i<r;++i)
        {
            for(int j=0;j<c;++j)
            {
                if(in[i][j] == '?')
                {
                    char cc = '.';
                    for(int k=i;k<r;++k)
                        if(in[k][j] != '?')
                        {
                            cc = in[k][j];
                            break;
                        }
                    if(cc == '.')
                    {
                        for(int k=i;k>=0;--k)
                        if(in[k][j] != '?')
                        {
                            cc = in[k][j];
                            break;
                        }
                    }
                    in[i][j] = cc;
                }
            }
        }
        printf("Case #%d:\n",tc);
        for(int i=0;i<r;++i)
        {
            for(int j=0;j<c;++j)
                putchar(in[i][j]);
            puts("");
        }
    }





    return 0;
}
