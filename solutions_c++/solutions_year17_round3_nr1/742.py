#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define NL '\n'
#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%I64d",&x)
#define sd(x) scanf("%lf",&x)
#define ss(x) scanf("%s",x)
#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(i=j;i<=k;i++)
#define REV(i,j,k) for(i=j;i>=k;i--)
#define READ(f) freopen(f,"r",stdin)
#define WRITE(f) freopen(f,"w",stdout)
#define cnd tree[idx]
#define lnd tree[idx*2]
#define rnd tree[(idx*2)+1]
#define lndp (idx*2),(b),((b+e)/2)
#define rndp (idx*2+1),((b+e)/2+1),(e)
#define pi 2.0*acos(0.0)
#define MOD 1000000007
#define MAX 1005

pair <LL,LL> p[MAX];
LL a[MAX];

LL go(int n, int k)
{
    if(k == 0) return 0;
    for(int i = 0; i < n; i++)
        a[i] = p[i].yy * p[i].xx * 2;
    sort(a, a+n);
    LL ret = 0;
    for(int i = n-1; i >= 0 && k > 0; i--, k--)
        ret += a[i];
    return ret;
}

int main()
{
    //READ("A-large.in");
    //WRITE("A-large.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0, n, i, j, k;
    LL x, y, sum, mx;
    long double ans;

    cin >> cases;

    while(cases--)
    {
        cin >> n >> k;

        FOR(i,0,n-1)
        {
            cin >> x >> y;
            p[i] = mp(x, y);
        }

        sort(p, p+n);

        sum = 0;
        mx = 0;

        REV(i,n-1,k-1)
        {
            sum = p[i].xx * p[i].xx;
            sum += (2 * p[i].xx * p[i].yy);
            mx = max(mx, sum+go(i, k-1));
            //cout << i << " " << sum+go(i, k-1) << NL;
        }

        ans = (long double)mx * pi;

        cout << "Case #" << ++caseno << ": ";
        cout << fixed;
        cout << setprecision(10) << ans << NL;
    }

    return 0;
}


