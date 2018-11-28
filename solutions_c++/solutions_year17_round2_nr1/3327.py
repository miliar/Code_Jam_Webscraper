//OUM HARI OUM, OUM TATSAT
// OUM NAMA VAGABATE BASUDEBAY
// OUM NAMA MA SWARASATI OUM NAMA

#include<bits/stdc++.h>

#define cl(vctr) vctr.clear()
#define ms(v, ar) memset(ar, v, sizeof(ar))
#define pb push_back
#define mp make_pair
#define all(container) container.begin(), container.end()

typedef long long int ll;
#define vi vector<int>
#define vll vector<ll>
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vpii vector<pii>
#define vpll vector<pll>

const double pi=(double)(2.0 * acos( 0.0 ));
const int inf=1 << 30;
const double eps=1E-9;
const double e = exp(1.0);
const int sz=100000 + 5;

using namespace std;
const ll mod=1000000000 + 7;

double s, k;

int main()
{
    //ios_base::sync_with_stdio(0); cin.tie(0);

    freopen("A-large.in", "r", stdin);
    freopen("out.in", "w", stdout);

    int t, T, n;
    double d;
    scanf("%d", &t); T=t;
    while(t--)
    {
        scanf("%lf %d", &d, &n);
        double mx=0.0;
        for(int i=0; i<n; i++)
        {
            scanf("%lf %lf", &k, &s);
            if(mx+eps<(d-k)/s)
                mx=(d-k)/s;
        }


        double res=1.0*d/mx;

        printf("Case #%d: %0.6lf\n", T-t, res);
    }

    return 0;
}

























