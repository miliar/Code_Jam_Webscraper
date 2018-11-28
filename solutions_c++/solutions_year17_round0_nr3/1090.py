#include <bits/stdc++.h>
#ifndef M_PI
#define M_PI 3.14159265358979323846264338327
#endif // M_PI
#define endl "\n"
#define S struct
#define X first
#define Y second
#define V vector
#ifndef __linux__
#define LLD "%I64d"
#else
#define LLD "%ll""d"
#endif
#define FOR(x, y, z) for (int x = (y); x < (z); ++x)
#define FORR(x, y, z) for (int x = (y); x > (z); --x)
#define GET(a, n) for (int __i = 0; __i < (n); ++__i) cin >> a[__i];
#define GETM(a, n, m) for (int __i = 0; __i < (n); ++__i) for (int __j = 0; __j < m; ++__j) cin >> a[__i][__j];
#define PRINTM(a, n, m) for (int __i = 0; __i < (n); ++__i) { for (int __j = 0; __j < m; ++__j) cout << a[__i][__j] << " ";  cout << endl; };
#define PRINT(a, n) for (int __i = 0; __i < (n); ++__i) cout << a[__i] << " ";
#define IT(a) a.begin(), a.end()
#define SQR(x) (x) * (x)
#define CASE(a, s) cout << "Case #" << a << ": " << s << endl;
#define DEB(a) cout << #a << " = " << (a) << endl; cout.flush();
#define DEBA(a) for (auto __i: a) cout << __i << " "; cout << endl; cout.flush();
#define IFDEB(b, a) if (b) { cout << #a << " = " << (a) << endl; cout.flush(); }
using namespace std;
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair <int, int> PII;
typedef pair <LL, LL> PLL;
const int MOD = 1000000007;
void sync_stdio() { cin.tie(NULL); ios_base::sync_with_stdio(false); }
S Sync_stdio { Sync_stdio() { cin.tie(NULL); ios_base::sync_with_stdio(false); } } _sync_stdio;
S FAIL { FAIL () { cout << "CHANGE!!!" << endl;}};

int solve(int test)
{
    LL n, k;
    cin >> n >> k;
    queue <PLL> q;
    q.push({n, 1});
    LL res = 0;
    while (q.size()) {
        PLL t = q.front();
        q.pop();
        res += t.Y;
        if (res >= k) {
            CASE(test, t.X / 2 << " " << (t.X - 1) / 2);
            return 0;
        }
        if (t.X % 2) {
            if (t.X / 2 > 0) {
                if (q.size() && q.back().X == t.X / 2) {
                    q.back().Y += 2 * t.Y;
                } else {
                    q.push({t.X / 2, 2 * t.Y});
                }
            }
        } else {
            if (t.X / 2 > 0) {
                if (q.size() && q.back().X == t.X / 2) {
                    q.back().Y += t.Y;
                } else {
                    q.push({t.X / 2, t.Y});
                }
            }
            if ((t.X - 1) / 2 > 0) {
                q.push({(t.X - 1) / 2, t.Y});
            }
        }
    }
    return 0;
}

int main()
{
    int n;
    cin >> n;
    FOR (i, 0, n) {
        cerr << "TEST #" << i << endl;
        solve(i + 1);
    }
    return 0;
}

