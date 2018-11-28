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
    freopen("B-large.in","r",stdin);
    freopen("jam17bout4.txt","w",stdout);
    int tt;
    sf(tt);
    rep(t,tt)
    {
        ll n,k,ans;
        sll(n);
        printf("Case #%d: ",t+1);
        k=n;
        ll p=0;
        //bool flag=false;
        while(k>0)
        {
            p++;
            k/=10;
        }
        ll a[p];
        k=n;
        ll y=p-1;
        while(k>0)
        {
            a[y]=k%10;
            k/=10;
            y--;
        }

            y=0;
            ll x=-1;
            repp(i,1,p)
                if (a[i]<a[i-1])
                {
                    x=i;
                    break;
                }
            if (x!=-1)
            {
                ll z=-1;
                for (int i=x-1;i>=0;i--)
                    if (a[i]!=a[x-1])
                    {
                        z=i;
                        break;
                    }
                a[z+1]--;
                repp(i,z+2,p)
                    a[i]=9;
            }
            if (a[x-1]==0)
            {
                a[0]=0;
                repp(i,1,p)
                    a[i]=9;
            }
            rep(i,p)
                if (a[i]!=0)
                    printf("%d",a[i]);
            printf("\n");

    }
}
