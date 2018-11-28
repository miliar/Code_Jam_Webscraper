#include <stdio.h>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <utility>

using namespace std;

#define pb push_back
#define ft first
#define sd second
#define mpr make_pair
#define all(x) begin((x)), end((x))
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int (i) = 0; (i) < (n); ++(i))
#define max3(a, b, c) max((a), max((b), (c)))
#define max4(a, b, c, d) max(max((a), (b)), max((c), (d)))
#define min3(a, b, c) min((a), min((b), (c)))
#define min4(a, b, c, d) min(min((a), (b)), min((c), (d)))
#define isz(x) (int)(x).size()

typedef long long ll;
typedef long double ld;
typedef unsigned int ui;
typedef pair<int, int> pii;
typedef vector<int> vi;

/* <------------------------------------------------------------------------------------> */

const int MX = 1e6;

int r[5], q[5][10], op[10];
bool us[10];
vector<int> g[10];

bool check0(int a)
{
    for (int i = 1; i <= MX; ++i)
    {
        if (i * r[0] >= 2 * MX) return false;
        if (9 * i * r[0] <= 10 * a && 10 * a <= 11 * i * r[0]) return true;
    }
    return false;
}

bool check(int a, int b)
{
    for (int i = 1; i <= MX; ++i)
    {
        if (i * r[0] >= 2 * MX || i * r[1] >= 2 * MX) return false;
        if (9 * i * r[0] <= 10 * a && 10 * a <= 11 * i * r[0] && 9 * i * r[1] <= 10 * b && 10 * b <= 11 * i * r[1])
            return true;
    }
    return false;
}

bool dfs(int v)
{
    if (us[v]) return false;
    us[v] = true;
    for (int & u : g[v])
        if (op[u] == -1 || dfs(op[u]))
        {
            op[u] = v;
            return true;
        }
    return false;
}

void subsolve()
{
    forn (i, 10)
    {
        g[i].clear();
        op[i] = -1;
    }

    int n, p;
    scanf("%d%d", &n, &p);
    forn (i, n) scanf("%d", r + i);
    forn (i, n) forn (j, p) scanf("%d", &q[i][j]);

    if (n == 1)
    {
        int ans = 0;
        forn (i, p) if (check0(q[0][i])) ++ans;
        printf("%d\n", ans);
        return;
    }

    forn (i, p) forn (j, p) if (check(q[0][i], q[1][j]))
        g[i].pb(j);

    forn (i, p)
    {
        memset(us, 0, sizeof us);
        dfs(i);
    }

    int ans = 0;
    forn (i, p) if (op[i] != -1) ++ans;

    printf("%d\n", ans);
}

void solve()
{
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i)
    {
        printf("Case #%d: ", i);
        subsolve();
    }
}

/* <------------------------------------------------------------------------------------> */

 #define LOCAL
// #define FILE_NAME

int main()
{
    #if defined LOCAL
        freopen("B-small-attempt1.in", "r", stdin);
        freopen("output.txt", "w", stdout);
    #elif defined FILE_NAME
        freopen(FILE_NAME".in", "r", stdin);
        freopen(FILE_NAME".out", "w", stdout);
    #endif

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    solve();

    return 0;
}
