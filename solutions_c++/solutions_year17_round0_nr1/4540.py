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
    freopen("A-large.in","r",stdin);
    freopen("jam17aout1.txt","w",stdout);
    int tt;
    sf(tt);
    rep(t,tt)
    {
        int n,k,ans;
        ans=0;
        char s[1009];
        scanf("%s",s);
        sf(k);
        printf("Case #%d: ",t+1);
        n=strlen(s);
        int p=0;
        bool flag=true;
        while(1)
        {
            int y=-1;
            for (int i=p;i<n;i++)
                if (s[i]=='-')
                {
                    y=i;
                    break;
                }
            if (y==-1)
                break;
            else
            {
                ans++;
                for (int i=y;i<(y+k);i++)
                    if (i>=n)
                    {
                        flag=false;
                        break;
                    }
                    else
                    {
                        if (s[i]=='-')
                            s[i]='+';
                        else
                            s[i]='-';
                    }
            }
            if (flag==false)
                break;
        }
        if (flag)
            printf("%d\n",ans);
        else
            printf("IMPOSSIBLE\n");
    }
}
