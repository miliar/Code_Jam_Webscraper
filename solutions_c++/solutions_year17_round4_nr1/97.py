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

int p;

unordered_map<ll, int> mem;

int go(vi v, int ost = 0)
{
    int ok = 0;
    for (int i = 1; i < p; ++i) ok |= v[i] > 0;
    if (!ok) return 0;

    ll hash = ost;
    for (int i = 1; i < p; ++i) hash = hash * 239ll + v[i];

    if (mem.find(hash) != mem.end()) return mem[hash];

    int &res = mem[hash];

    for (int i = 1; i < p; ++i) if (v[i] > 0)
    {
        v[i]--;
        res = max(res, go(v, (ost + i) % p));
        v[i]++;
    }
    if (ost == 0) res++;
    return res;
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
        int n;
        scanf("%d%d", &n, &p);
        vi g(n);
        forn(i, n) scanf("%d", &g[i]);

        if (!(testL <= tt && tt < testR)) continue;
        printf("Case #%d: ", tt + 1);
        
        //SOLVE
        vi v(p);
        forn(i, n) v[g[i] % p]++;

        /*int res = 0;
        if (p == 2)
        {
            res = v[0] + (v[1] + 1) / 2;
        }
        else
        {
            res = v[0];
            res += min(v[1], v[2]) + (max(v[1], v[2]) - min(v[1], v[2]) + 2) / 3;
        } */
        mem.clear();
        int res = go(v) + v[0];
        printf("%d\n", res);

    }
            
    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
