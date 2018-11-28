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
const dbl eps = 1e-9;

/* --- main part --- */


/*int get(int x, int y)
{
    int res;
    int p = (x + y / 2) / y * y;
    if ((p * 9 + 9) / 10 <= x && x <= p * 11 / 10) res = p / y;
    else res = -1;
    eprintf("%d %d --> %d\n", x, y, res);
    return res;
} */

int ok(int x, int y, int amount)
{
    ll need = y * (ll)amount;
    if ((need * 9 + 9) / 10 <= x && x <= need * 11 / 10) return 1;
    return 0;
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
        int n, p;
        scanf("%d%d", &n, &p);
        vi r(n);
        forn(i, n) scanf("%d", &r[i]);
        vector<vi> a(n, vi(p));
        forn(i, n) forn(j, p) scanf("%d", &a[i][j]);


        if (!(testL <= tt && tt < testR)) continue;
        printf("Case #%d: ", tt + 1);
        
        //SOLVE

        forn(i, n) sort(all(a[i]));
        vector<vi> u(n, vi(p));    

        int res = 0;
        for (int amount = 1; amount <= 1.01e6; ++amount)
        {
            while (1)
            {
                int have = 1;
                vi v;
                forn(i, n)
                {
                    have = 0;
                    forn(j, p) if (!u[i][j] && ok(a[i][j], r[i], amount))
                    {
                        have = 1;
                        v.pb(j);
                        break;
                    }
                    if (!have) break;
                }
                if (!have) break;
                res += 1;
                forn(i, n) u[i][v[i]] = 1;
            }
        }
        printf("%d\n", res);
    }
            
    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
