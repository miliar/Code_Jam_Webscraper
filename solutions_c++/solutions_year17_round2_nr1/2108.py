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
#define MAX 100005

int main()
{
    READ("A-large.in");
    WRITE("A-large.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0, n, i, j, k, cnt;
    double d, x, y, ans, mx, z;

    cin >> cases;

    while(cases--)
    {
        cin >> d >> n;

        mx = 0.000000000001;

        FOR(i,1,n)
        {
            cin >> x >> y;
            //mx = max(mx, (d-x)/y);
            z = (d-x)/y;
            if(mx-z < 0.000000001) mx = z;
        }

        ans = d/mx;

        cout << "Case #" << ++caseno << ": ";
        cout << fixed;
        cout << setprecision(6);
        cout << ans << NL;
    }

    return 0;
}

