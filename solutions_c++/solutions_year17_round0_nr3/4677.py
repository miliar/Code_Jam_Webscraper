#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef vector<int> vi;
typedef vector<pii> vii;

#define rep(i,a) for(int i=0;i<(a);++i)
#define repp(i,a,b) for(int i=(a);i<(b);++i)
#define fill(a,b) memset((a),(b),sizeof((a)))
#define clr(a) memset((a),0,sizeof((a)))
#define foreach(a,it)  for( typeof((a).begin()) it=(a).begin();it!=(a).end();it++ )
#define mp make_pair
#define pb push_back
#define all(s) s.begin(),s.end()
#define sz(a) int(a.size())
#define ft first
#define sd second

#define sf(n) scanf("%d",&n)
#define pf(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define pll(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

const double eps = 1e-8;
const ll inf = 2e9+1;
const ll mod = 1e9+7;
const int N = int(2e5)+10;

ll power(ll x, ll y)
{
    ll t=1;
    while(y>0)
    {
        if (y%2) y-=1, t=t*x%mod;
        else y/=2, x=x*x%mod;
    }
    return t;
}

int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("jam17cout1.txt","w",stdout);
    int tt;
    sf(tt);
    rep(t,tt)
    {
        printf("Case #%d: ",t+1);
        int n,k,x;
        int mn,mx;
        mn=inf;
        mx=-1;
        sf(n); sf(k);
        priority_queue<int> q;
        q.push(n);
        while(k--)
        {
            x=q.top();
            q.pop();
            if (x%2==0)
            {
                mx=x/2;
                q.push(x/2);
                mn=(x-1)/2;
                q.push((x-1)/2);
            }
            else
            {
                mx=x/2;
                q.push(x/2);
                mn=x/2;
                q.push(x/2);
            }
        }
        printf("%d %d\n",mx,mn);
    }
}
