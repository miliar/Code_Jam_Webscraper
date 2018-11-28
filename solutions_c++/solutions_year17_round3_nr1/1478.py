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

const double MINF = -1e15, EPS = 1e-6, PI = 3.141592653589793;

bool eq(double a, double b)
{
    return fabs(a - b) < EPS;
}

typedef pair<double, double> pdd;

pdd a[1003]; //r, h
double d[1003][1003];
int n, k;

double f(int i = 0, int l = k)
{
    if (!eq(d[i][l], -1.0)) return d[i][l];
    if (!l) return d[i][l] = PI * a[i].ft * a[i].ft;
    if (i == n) return d[i][l] = MINF;
    double ans = MINF;
    for (int j = i + 1; n - j + 1 >= l; ++j)
    {
        ans = max(ans, PI * (a[(i ? i : j)].ft * a[(i ? i : j)].ft - a[j].ft * a[j].ft + 2.0 * a[j].ft * a[j].sd) + f(j, l - 1));
    }
    return d[i][l] = ans;
}

bool comp(const pdd & a, const pdd & b)
{
    if (!eq(a.ft, b.ft)) return a.ft > b.ft;
    return a.sd > b.sd;
}

void subsolve()
{
    forn (i, 1003) forn (j, 1003) d[i][j] = -1.0;
    scanf("%d%d", &n, &k);
    for (int i = 1; i <= n; ++i)
        scanf("%lf%lf", &a[i].ft, &a[i].sd);
    sort(a + 1, a + n + 1, comp);
    a[0] = a[1];

    printf("%.10f", f());
}

void solve()
{
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i)
    {
        printf("Case #%d: ", i);
        subsolve();
        puts("");
    }
}

/* <------------------------------------------------------------------------------------> */

 #define LOCAL
// #define FILE_NAME

int main()
{
    #if defined LOCAL
        freopen("A-large.in", "r", stdin);
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
