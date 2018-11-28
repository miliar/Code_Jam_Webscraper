#include<bits/stdc++.h>
using namespace std;

// general
#define ll long long
#define pb push_back
#define pob pop_back
#define f first
#define s second
#define mp make_pair
#define fastio
#define PI 3.14159265358979L
//--------------

// IO funcs
#ifdef fastio

#define SC(x) scanf("%c",&x)
#define SD(x) scanf("%d",&x)
#define SLL(x) scanf("%lld",&x)
#define SS(x) scanf("%s",x)

#define PC(x) printf("%c",x)
#define PD(x) printf("%d",x)
#define PLL(x) printf("%lld",x)
#define PS(x) printf("%s",x)

#else // fastio

#define SC(x) cin>>x
#define SD(x) cin>>x
#define SLL(x) cin>>x
#define SS(x) cin>>x

#define PC(x) cout<<(x)
#define PD(x) cout<<(x)
#define PLL(x) cout<<(x)
#define PS(x) cout<<(x)

#endif

//----fastio-end---

// funcs
#define swap(a,b) a^=b^=a^=b
#define max(a,b) (((a) > (b))? (a) : (b))
#define min(a,b) (((a) < (b))? (a) : (b))
//----------------

// statements
#define LP(i,ii,jj) for(int i=(ii);i<(jj);i++)
#define LPR(i,ii,jj) for(int i=(ii);i>=(jj);i--)
//----------------

// DS
#define Vi vector<int>
#define Pii pair<int,int>
#define Mii map<int,int>
//----------------

const int MOD = 1000000007;

struct Comparer {
    bool operator() (const bitset<1000> &b1, const bitset<1000> &b2) const {
        return b1.to_string() < b2.to_string();
    }
};

int powmod(ll b, ll e, int m)
{
    b %= m;
    ll r = 1;
    while (e > 0) {
        if (e & 1)
            r = (r * b) % m;
        b = (b * b) % m;
        e >>= 1;
    }
    return r;
}

ll gcd(ll u, ll v)
{
    ll t;
    while (v)
    {
        t = u;
        u = v;
        v = t % v;
    }
    return u < 0 ? -u : u;
}

double twoPtDist(double x1, double y1, double x2, double y2)
{
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

bool NonDec(char s[], int l)
{
    LP(i, 0, l - 1)
    {
        if(s[i] > s[i+1])
            return false;
    }
    return true;
}

inline void Solve(int T)
{
    ll n,k;
    SLL(n); SLL(k);
    PS("Case #"); PD(T); PS(": ");
    vector<pair<ll, ll> > cakes;
    LP(i, 0, n)
    {
        int r, h;
        SD(r); SD(h);
        cakes.pb(mp(r,h));
    }
    sort(cakes.begin(), cakes.end());
    ll ans = 0;
    vector<pair<ll, ll> >::iterator it = cakes.begin();
    vector<ll> curCakes;
    LP(i, 0, k - 1)
    {
        curCakes.pb(((*it).f) * ((*it).s));
        it++;
    }
    for(; it != cakes.end(); it++)
    {
        vector<ll>::reverse_iterator jt = curCakes.rbegin();
        ll curAns = ((*it).f) * (((*it).f) + 2 * ((*it).s));
        LP(i, 0, k - 1)
        {
            curAns += 2 * ((*jt));
            jt++;
        }
        ans = max(ans, curAns);
        curCakes.pb(((*it).f) * ((*it).s));
        sort(curCakes.begin(), curCakes.end());
    }
    cout.setf(ios::fixed,ios::floatfield);
    cout.precision(10);
    cout << ans * PI;
    PC('\n');
}

int main()
{
    int t=1;
    SD(t);
    LP(i,0,t)
    {
        Solve(i+1);
    }
    return 0;
}
