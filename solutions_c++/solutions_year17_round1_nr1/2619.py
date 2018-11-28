
/// Bismillahir Rahmanir Rahim
/// S. M. Shakir Ahsan Romeo ( Pure_Protea, #theromeo421, Cosmos_Freak )
/// CSE Discipline, Khulna University, Khulna
/// Monirampur, Jessore.

#include <bits/stdc++.h>
using namespace std;

typedef long long lng;
typedef vector < int >  vi;
typedef vector < lng >  vl;
typedef pair < int, int >  pii;
typedef vector < pii >  vpii;

const int inf = 1 << 30;
const long long linf = 1LL << 62;
const double PI = acos(-1.0), dinf = (double)(1LL << 62), eps = (double)(1e-9);

double distance(double x1, double y1, double x2, double y2)
{
    x1 -= x2;
    y1 -= y2;
    return sqrt(x1 * x1 + y1 * y1);
}
long long POW(long long b, long long p)
{
    if(p == 0)
        return 1;
    long long t = POW(b, p >> 1);
    if(p & 1)
        return t * t * b;
    return t * t;
}
long long bigmod(long long b, long long p, long long m)
{
    if(p == 0)
        return 1;
    long long t = POW(b, p >> 1) % m;
    t = (t * t) % m;
    if(p & 1)
        t = (t * b) % m;
    return t;
}
inline int getint()
{
    int x;
    scanf("%d", &x);
    return x;
}
inline long long getlng()
{
    long long x;
    scanf("%lld", &x);
    return x;
}

lng gcd(lng a, lng b)
{
    return !b ? a : gcd(b, a % b);
}

lng lcm(lng a, lng b)
{
    return (a / gcd(a, b)) * b;
}

int dx4[] = {-1, 0, 1, 0};
int dy4[] = {0, 1, 0, -1};
int dx8[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy8[] = {-1, 0, 1, -1, 1, -1, 0, 1};

#define theromeo421 main()
#define segtree int lft = node << 1, rgt = lft | 1, mid = (b + e) >> 1;
#define mem(x, y) memset(x, y, sizeof x);
#define II getint()
#define LL getlng()
#define sz(x) ((int)x.size())
#define sqr(x) ((x) * (x))
#define max3(a,b,c) max(a, max(b,c))
#define min3(a,b,c) min(a, min(b,c))
#define pr1(x) cout << x << endl
#define pr2(x,y) cout << x << ' ' << y << endl
#define pr3(x,y,z) cout << x << ' ' << y << ' ' << z << endl
#define pr4(a,b,c,d) cout << a << ' ' << b << ' ' << c << ' ' << d << endl
#define rep(i, n) for(int i = 0; i < n; ++i)
#define rep1(i, n) for(int i = 1; i <= n; ++i)
#define repab(i, a, b) for(int i = a; i <= b; ++i)
#define repstl(it, x) for(auto it = x.begin(); it != x.end(); it++)
#define repbstl(it, x) for(auto it = x.rbegin(); it != x.rend(); it++)
#define forch(it, x) for(auto it : x)
#define pb push_back
#define all(x) x.begin(), x.end()
#define xx first
#define yy second
#define dbg(x) cerr << #x << " :  " << x << endl;
#define read(a) freopen(a, "r", stdin);
#define write(a) freopen(a, "w", stdout);
#define prv(v) rep(i, v.size()) cout << v[i] << " \n"[i + 1 == v.size()];
#define prmp(x) repstl(it, x) pr2(it->xx, it->yy)
#define pause int ppause; cin >> ppause;
#define pf printf
#define sc scanf

/// Google Code Jam 2017 Round 1A

void solve();

void IO()
{
    read("A-large.in");
    write("out.txt");
}


int theromeo421
{
    IO();

    int T = II;
    rep1(cas, T)
    {
        printf("Case #%d:\n", cas);
        solve();
        cerr << cas << " done" << endl;
    }
    return 0;
}

const int N = 30;
char mat[N][N];
//bool vis[N][N];
int R, C;

//map < char, pair < pii, pii > > mp;

void solve()
{
    R = II;
    C = II;
    rep1(i, R)
    {
        scanf("%s", mat[i] + 1);
    }
    rep1(i, R)
    {
        rep1(j, C)
        {
            if(mat[i][j] != '?')
            {
                char c = mat[i][j];
                for(int jj = j - 1; jj >= 1 && mat[i][jj] == '?'; --jj)
                {
                    mat[i][jj] = c;
                }
                for(int jj = j + 1; jj <= C && mat[i][jj] == '?'; ++jj)
                {
                    mat[i][jj] = c;
                }
            }
        }
    }
    rep1(i, R)
    {
        if(mat[i][1] == '?')
        {
            if(i > 1)
            {
                for(int j = 1; j <= C; ++j)
                {
                    mat[i][j] = mat[i - 1][j];
                }
            }
            else
            {
                int en = -1;
                for(int ii = 2; ii <= R; ++ii)
                {
                    if(mat[ii][1] != '?')
                    {
                        en = ii;
                        break;
                    }
                }
                for(int ii = 1; ii < en; ++ii)
                {
                    for(int jj = 1; jj <= C; ++jj)
                    {
                        mat[ii][jj] = mat[en][jj];
                    }
                }
            }
        }
    }
    //cout << endl << endl;
    rep1(i, R)
    {
        puts(mat[i] + 1);
    }
}
