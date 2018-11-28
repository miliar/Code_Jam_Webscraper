/**
 *    author:  [itmo] enot.1.10
 *    created: 21.01.2017 23:42:28       
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
const ll INF = 1.01e18;
const dbl eps = 1e-9;

/* --- main part --- */

int Hd, Ad, Hk, Ak, B, D;
ll res;

unordered_map<ll, ll> mem;

ll get(int bk, int dk)
{
    ll POS = bk * pw(30) + dk;
    if (mem.find(POS) != mem.end()) return mem[POS];
    ll &ans = mem[POS];
    ans = 0;

    int h1 = Hd, a1 = Ad, h2 = Hk, a2 = Ak;
    int full = 1;

    //eprintf("%d %d\n", bk, dk);
    
    forn(i, dk)
    {
        ans++;
        if (h2 <= a1) return ans;
        if (h1 <= a2 - D)
        {
            if (full) return ans = INF;
            full = 1;
            h1 = Hd;
        }
        else
        {
            a2 = max(0, a2 - D);
            full = 0;
        }

        h1 -= a2;
    }
    forn(i, bk)
    {
        ans++;
        if (h2 <= a1) return ans;

        if (h1 <= a2)
        {
            if (full) return ans = INF;
            full = 1;
            h1 = Hd;
        }
        else
        {
            a1 += B;
            full = 0;
        }

        h1 -= a2;
    }
    while (1)
    {
        //eprintf("%d %d %d %d\n", h1, a1, h2, a2);
        ans++;
        if (h2 <= a1) return ans;

        if (h1 <= a2)
        {
            if (full) return ans = INF;
            full = 1;
            h1 = Hd;
        }
        else
        {
            full = 0;
            h2 -= a1;
        }

        h1 -= a2;
    }
}

    

ll get(int bk)
{
    int l = 0;
    int r;
    if (D > 0) r = min((int)1e5, (Ak + D - 1) / D);
    else r = 0;
    r = 100;

    while (0 && l + 5 < r)
    {
        int m1 = (2 * l + r) / 3;
        int m2 = (l + 2 * r) / 3;
        ll v1 = get(bk, m1);
        ll v2 = get(bk, m2);
        if (v1 <= v2) r = m2;
        else l = m1;
    }
    ll best = INF;
    for (int m = l; m <= r; ++m)
    {
        ll val = get(bk, m);
        if (val < best) best = val;
    }
    res = min(res, best);
    return best;
}

int main(int argc, char* argv[])
{
    assert(freopen("1.in", "r", stdin));
    int tn;
    scanf("%d", &tn);
    int testL = 0, testR = tn;
    if (argc == 4)
    {
        sscanf(argv[1], "%d", &testL);
        sscanf(argv[2], "%d", &testR);
        assert(freopen(argv[3], "w", stdout));
    }
    else
    {
        assert(freopen("1.out", "w", stdout));
    }


    forn(tt, tn)
    {
        //READ
        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

        if (!(testL <= tt && tt < testR)) continue;
        printf("Case #%d: ", tt + 1);
        
        mem.clear();
        //SOLVE
        res = INF;

        int l = 0, r;
        if (B > 0) r = min((int)1e5, (Hk - Ad + B - 1) / B);
        else r = 0;
        r = 100;

        /*while (0 && l + 5 < r)
        {
            int m1 = (2 * l + r) / 3;
            int m2 = (l + 2 * r) / 3;
            ll v1 = get(m1);
            ll v2 = get(m2);
            if (v1 >= v2) l = m1;
            else r = m2;
        }
        for (int m = l; m <= r; ++m) get(m);
          */

        forn(bk, 101) forn(dk, 101) res = min(res, get(bk, dk));
        
        if (res < INF) printf("%I64d\n", res);
        else printf("IMPOSSIBLE\n");
    }
            
    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
