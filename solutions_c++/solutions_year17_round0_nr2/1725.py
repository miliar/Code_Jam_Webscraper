/**
 *    author:  [itmo] enot.1.10
 *    created: 08.04.2017 17:04:36       
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


ll get(char *s)
{
    ll x;
    sscanf(s, "%lld", &x);
    return x;
}


char s[111];
char t[111];

ll calc(int l, int n)
{
    for (int i = l + 1; i < n; ++i) t[i] = t[l];
    return get(t);
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
        scanf("%s", s);
        int n = strlen(s);
        t[n] = 0;
        s[n] = 0;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 9; j >= 0; --j)
            {
                t[i] = '0' + j;
                if (calc(i, n) <= get(s)) break;
            }
        }
        printf("Case #%d: %lld\n", tt + 1, get(t));
    }

    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
