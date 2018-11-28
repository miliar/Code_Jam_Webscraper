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

const int MX = 30;
char s[MX][MX], us[MX][MX];

void subsolve()
{
    int n, m;
    scanf("%d%d", &n, &m);
    forn (i, n) scanf("%s", s[i]);

    memset(us, 0, sizeof us);
    forn (i, n) forn (j, m) if (s[i][j] != '?' && !us[i][j])
    {
        us[i][j] = true;
        for (int k = i - 1; k >= 0 && s[k][j] == '?'  && !us[k][j]; --k)
        {
            s[k][j] = s[i][j];
            us[k][j] = true;
        }
        for (int k = i + 1; i < n && s[k][j] == '?' && !us[k][j]; ++k)
        {
            s[k][j] = s[i][j];
            us[k][j] = true;
        }
    }

    memset(us, 0, sizeof us);
    forn (i, n) forn (j, m) if (s[i][j] != '?' && !us[i][j])
    {
        us[i][j] = true;
        for (int k = j - 1; k >= 0 && s[i][k] == '?' && !us[i][k]; --k)
        {
            s[i][k] = s[i][j];
            us[i][k] = true;
        }
        for (int k = j + 1; k < m && s[i][k] == '?' && !us[i][k]; ++k)
        {
            s[i][k] = s[i][j];
            us[i][k] = true;
        }
    }

    forn (i, n)
    {
        forn (j, m) printf("%c", s[i][j]);
        puts("");
    }
}

void solve()
{
    int t;
    scanf("%d\n", &t);
    for (int i = 1; i <= t; ++i)
    {
        printf("Case #%d:\n", i);
        subsolve();
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
