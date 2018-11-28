#include <bits/stdc++.h>
using namespace std;

#define iOS ios_base::sync_with_stdio(false)
#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%lld",&a)
#define scs(a) scanf(" %s",a)
#define scc(a) scanf(" %c",&a)
#define flsh fflush(stdout)

const int MAX = 1e5+6;
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

map<long long, long long> ans;
map<long long, int> vis;
vector<pair<long long,long long> > v;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("sol.txt", "w", stdout);

    int t;
    sc(t);

    for(int tc=1; tc<=t; ++tc)
    {
        vis.clear();
        ans.clear();
        v.clear();
        long long n, k;
        scll(n);
        scll(k);
        long long v1=n,v2=0;
        queue<long long> q;
        q.push(n);
        vis[n] = 1;
        ans[n] = 1;
        while(!q.empty())
        {
            long long cur = q.front();
            q.pop();
            long long tmp;
            if(cur != n)
            {
                if(ans.count(cur*2))
                    ans[cur] += ans[cur*2];
                if(ans.count(cur*2+2))
                    ans[cur] += ans[cur*2+2];
                if(ans.count(cur*2+1))
                    ans[cur] += ans[cur*2+1]*2;
            }
            cur--;
            tmp = cur/2;
            long long tmp2 = cur - tmp;
            if(tmp2 > 0 && !vis[tmp2])
                vis[tmp2] = 1,q.push(tmp2);
            if(tmp > 0 && !vis[tmp])
                vis[tmp] = 1,q.push(tmp);
        }

        for(auto u: ans)
            v.push_back(u);

        for(int i=v.size()-1; i>=0; --i)
        {
            if(k <= v[i].second)
            {
                long long tmp1,tmp2;
                long long cc = v[i].first;
                cc--;
                tmp1 = cc/2;
                cc -= tmp1;
                tmp2 = cc;
                printf("Case #%d: %lld %lld\n",tc,tmp2,tmp1);
                break;
            }
            k -= v[i].second;
        }
    }

    return 0;
}


