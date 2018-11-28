/**
 *    author:  [itmo] enot.1.10
 *    created: 08.04.2017 17:12:51       
**/
#define __USE_MINGW_ANSI_STDIO 0
#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),a.end()
#define pw(x) (1LL<<(x))

using namespace std;

typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef pair<int, int> pi;

const int inf = 1.01e9;
const dbl eps = 1e-9;

/* --- main part --- */

ll L = -1, R = -1;

void go(ll n, ll k)
{
    if (k == 1)
    {
        L = (n - 1) / 2;
        R = n / 2;
        return;
    }
    ll l = (n - 1) / 2;
    ll r = n / 2;
    --k;
    if (k % 2 == 0)
    {
        go(l, k / 2);
    }
    else
    {
        go(r, (k + 1) / 2);
    }
}

int main()
{
    #ifdef home
        assert(freopen("1.in", "r", stdin));
        assert(freopen("1.out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    forn(tt, tn)
    {
        ll n, k;
        scanf("%lld%lld", &n, &k);
        go(n, k);
        printf("Case #%d: %lld %lld\n", tt + 1, R, L);
    }        
    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
