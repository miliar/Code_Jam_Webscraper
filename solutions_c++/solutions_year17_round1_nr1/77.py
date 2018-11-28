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


char s[33][33];


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
        int n, m;
        scanf("%d%d", &n, &m);
        forn(i, n) scanf("%s", s[i]);

        if (!(testL <= tt && tt < testR)) continue;
        printf("Case #%d:\n", tt + 1);
        
        //SOLVE
        vi filled(n);
        forn(i, n)
        {
            int have = 0;
            forn(j, m) if (s[i][j] != '?') have = 1;
            if (!have) continue;
            filled[i] = 1;
            char last = 0;
            forn(j, m) if (s[i][j] != '?')
            {
                last = s[i][j];
                break;
            }
            forn(j, m)
            {
                if (s[i][j] == '?') s[i][j] = last;
                else last = s[i][j];
            }
        }
        forn(i, n - 1) if (filled[i] && !filled[i + 1])
        {
            filled[i + 1] = 1;
            forn(j, m) s[i + 1][j] = s[i][j];
        }
        for (int i = n - 1; i > 0; --i) if (filled[i] && !filled[i - 1])
        {
            filled[i - 1] = 1;
            forn(j, m) s[i - 1][j] = s[i][j];
        }
        forn(i, n) printf("%s\n", s[i]);


    }
            
    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
