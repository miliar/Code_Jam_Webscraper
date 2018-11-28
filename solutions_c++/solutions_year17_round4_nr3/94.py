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

const int N = 222;

vi v[N];
vi vrev[N];
int NEG(int x)
{
    return x ^ 1;
}

void add(int x, int y)
{
    v[x].pb(y);
    vrev[y].pb(x);
    v[NEG(y)].pb(NEG(x));
    vrev[NEG(x)].pb(NEG(y));
}            

int n, m;
char s[55][55];


int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int in(int x, int y)
{
    return 0 <= x && x < n && 0 <= y && y < m;
}

int rot(char tp, int dir)
{
    if (tp == '/')
    {
        if (dir == 0) return 3;
        if (dir == 1) return 2;
        if (dir == 2) return 1;
        if (dir == 3) return 0;
    }
    if (tp == '\\')
    {
        if (dir == 0) return 2;
        if (dir == 1) return 3;
        if (dir == 2) return 0;
        if (dir == 3) return 1;
    }
    assert(false);
}

vi can[55][55];

int fail1(pi z, int tp, int id)
{
    int x = z.F;
    int y = z.S;
    
    int ld, rd;
    if (tp == 0) ld = 0, rd = 1;
    else ld = 2, rd = 3;

    for (int sd = ld; sd <= rd; ++sd)
    {
        int xx = x, yy = y, dir = sd;
        while (in(xx, yy) && s[xx][yy] != '#')
        {
            can[xx][yy].pb(id);
            if (s[xx][yy] == '/' || s[xx][yy] == '\\')
            {
                dir = rot(s[xx][yy], dir);
            }
            xx += dx[dir];
            yy += dy[dir];
            if (xx == x && yy == y) return 1;
        }
    }
    return 0;
}


int used[N];
int ans[N];
int st[N];
int stc = 0;
int col[N];

void dfs1(int x)
{
    used[x] = 1;
    for (int y : v[x]) if (!used[y]) dfs1(y);
    st[stc++] = x;
}

void dfs2(int x, int cc)
{
    col[x] = cc;
    used[x] = 2;
    if (ans[x] == -1)
    {
        ans[x] = 1;
        ans[x ^ 1] = 0;
    }
    for (int y : vrev[x]) if (used[y] == 1) dfs2(y, cc);
}



            
            
int fail2(pi z1, int tp1, pi z2, int tp2)
{
    int x1 = z1.F;
    int y1 = z1.S;
    int x2 = z2.F;
    int y2 = z2.S;
    
    int ld, rd;

    if (tp1 == 0) ld = 0, rd = 1;
    else ld = 2, rd = 3;

    for (int sd = ld; sd <= rd; ++sd)
    {
        int xx = x1, yy = y1, dir = sd;
        while (in(xx, yy) && s[xx][yy] != '#')
        {
            if (s[xx][yy] == '/' || s[xx][yy] == '\\')
            {
                dir = rot(s[xx][yy], dir);
            }
            xx += dx[dir];
            yy += dy[dir];
            if ((xx == x1 && yy == y1) || (xx == x2 && yy == y2)) return 1;
        }
    }
    if (tp2 == 0) ld = 0, rd = 1;
    else ld = 2, rd = 3;

    for (int sd = ld; sd <= rd; ++sd)
    {
        int xx = x2, yy = y2, dir = sd;
        while (in(xx, yy) && s[xx][yy] != '#')
        {
            if (s[xx][yy] == '/' || s[xx][yy] == '\\')
            {
                dir = rot(s[xx][yy], dir);
            }
            xx += dx[dir];
            yy += dy[dir];
            if ((xx == x1 && yy == y1) || (xx == x2 && yy == y2)) return 1;
        }
    }

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
        scanf("%d%d", &n, &m);
        forn(i, n) scanf("%s", s[i]);


        if (!(testL <= tt && tt < testR)) continue;
        printf("Case #%d: ", tt + 1);
        
        //SOLVE
        vector<pi> a;
        forn(i, n) forn(j, m) if (s[i][j] == '-' || s[i][j] == '|') a.pb({i, j});

        forn(i, 2 * sz(a)) v[i].clear(), vrev[i].clear();
        forn(i, n) forn(j, m) can[i][j].clear();

        int sz = 2 * sz(a);

        assert(sz <= 200);

        forn(i, sz(a))
        {
            if (fail1(a[i], 0, 2 * i))
            {
                add(2 * i, 2 * i + 1);
            }
            if (fail1(a[i], 1, 2 * i + 1))
            {
                add(2 * i + 1, 2 * i);
            }
        }
            

        forn(i, sz(a)) forn(j, i) forn(tp1, 2) forn(tp2, 2)
        {
            if (fail2(a[i], tp1, a[j], tp2))
            {
                add(i * 2 + tp1, NEG(j * 2 + tp2));
                add(j * 2 + tp2, NEG(i * 2 + tp1));
            }
        }

        int ok = 1;
        forn(i, n) forn(j, m) if (s[i][j] == '.')
        {
            assert(sz(can[i][j]) <= 2);
            if (sz(can[i][j]) == 0)
            {
                ok = 0;
            }
            if (sz(can[i][j]) == 1)
            {
                int x = can[i][j][0];
                add(NEG(x), x);
            }
            if (sz(can[i][j]) == 2)
            {
                int x = can[i][j][0];
                int y = can[i][j][1];
                add(NEG(x), y);
                add(NEG(y), x);
            }
                
        }

        forn(i, sz) used[i] = 0;

        stc = 0;
        forn(i, sz) if (!used[i]) dfs1(i);

        forn(i, sz) ans[i] = -1;

        int cc = 0;
        for (int ii = stc - 1; ii >= 0; --ii)
        {
            int i = st[ii];
            if (used[i] == 1)
            {
                cc++;
                dfs2(i, cc);
            }
        }

        forn(i, sz(a)) if (col[2 * i] == col[2 * i + 1]) ok = 0;

        if (ok)
        {
            printf("POSSIBLE\n");
            forn(i, sz(a))
            {
                if (ans[2 * i]) s[a[i].F][a[i].S] = '-';
                else  s[a[i].F][a[i].S] = '|';
            }
            forn(i, n) printf("%s\n", s[i]);
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
 
    }
            
    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
