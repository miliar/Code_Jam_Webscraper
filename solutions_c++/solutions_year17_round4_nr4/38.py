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


const int N = 33;

char s[N][N];
pi a[N];
pi b[N];
int aa, bb;
int n, m;
int M;

int status[N][N];

int in(int x, int y)
{
    return 0 <= x && x < n && 0 <= y && y < m;
}

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

pi q[N * N];
int st, en;
int d[N][N];

int calc(int mask, int X, int Y)
{
    //eprintf("%d %d --> %d %d\n", a[X].F, a[X].S, b[Y].F, b[Y].S);
    memset(status, 0, sizeof status);
    forn(i, bb) if (!(mask & pw(i)))
    {
        int c = 1;
        if (i == Y) c = 2;

        forn(it, 4)
        {
            int x = b[i].F, y = b[i].S;
            while (in(x, y) && s[x][y] != '#')
            {
                status[x][y] |= c;
                x += dx[it];
                y += dy[it];
            }
        }
    }
    //forn(i, n) forn(j, m) eprintf("%d%c", status[i][j], " \n"[j + 1 == m]);

    forn(i, N) forn(j, N) d[i][j] = inf;
    d[a[X].F][a[X].S] = 0;
    st = en = 0;
    q[en++] = {a[X].F, a[X].S};

    while (st < en)
    {
        int x = q[st].F;
        int y = q[st].S;
        st++;
        //eprintf("bfs %d %d\n", x, y);

        if (status[x][y] & 2) return 1;
        if (d[x][y] == M) continue;
        if (status[x][y] & 1) continue;
        
        forn(it, 4)
        {
            int xx = x + dx[it];
            int yy = y + dy[it];
            if (in(xx, yy) && s[xx][yy] != '#' && d[xx][yy] == inf)
            {
                d[xx][yy] = d[x][y] + 1;
                q[en++] = {xx, yy};
            }
        }
    }
    return 0;
}



int can[1 << 20];
pi from[1 << 20];

int mem[1 << 10][10][10];


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
        scanf("%d%d%d", &m, &n, &M);
        forn(i, n) scanf("%s", s[i]);

        if (!(testL <= tt && tt < testR)) continue;
        printf("Case #%d: ", tt + 1);
        
        //SOLVE
        eprintf("test %d\n", tt);
        memset(can, 0, sizeof can);
        memset(mem, 0, sizeof mem);

        aa = 0, bb = 0;
        forn(i, n) forn(j, m)
        {
            if (s[i][j] == 'S') a[aa++] = {i, j};
            if (s[i][j] == 'T') b[bb++] = {i, j};
        }
        forn(mask, pw(bb)) forn(i, aa)  forn(j, bb) if (!(mask & pw(j)))
        {
            mem[mask][i][j] = calc(mask, i, j);
            //eprintf("mask %d %d %d ==> %d\n", mask, i, j, mem[mask][i][j]);
            //exit(0);
        }

        can[0] = 1;
        int mx = 0;
        int mxmask = 0; 
        forn(mask, pw(aa + bb)) if (can[mask])
        {
            if (__builtin_popcount(mask) > mx)
            {
                mx = __builtin_popcount(mask);
                mxmask = mask;
            }
            int maska = mask & (pw(aa) - 1);
            int maskb = mask >> aa;
            forn(i, aa) if (!(maska & pw(i)))
            {
                forn(j, bb) if (!(maskb & pw(j)))
                {
                    if (mem[maskb][i][j])
                    {
                        int mmask = mask | pw(i) | pw(j + aa);
                        if (can[mmask] == 0)
                        {
                            can[mmask] = 1;
                            from[mmask] = {i, j};
                        }
                    }
                }
            }
        }
        printf("%d\n", mx / 2);
        int mask = mxmask;
        vector<pi> res;
        while (mask > 0)
        {
            int x = from[mask].F;
            int y = from[mask].S;
            mask ^= pw(x) | pw(y + aa);
            res.pb({x, y});
        }
        reverse(all(res));
        for (pi z : res) printf("%d %d\n", z.F + 1, z.S + 1);

    }
            
    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
