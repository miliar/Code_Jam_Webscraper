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

S Horse
{
    int dist;
    int speed;
};

const LL INF = 1e14;

int solve(int test)
{
    int n, q;
    cin >> n >> q;
    vector <Horse> horses(n);
    FOR (i, 0, n) {
        cin >> horses[i].dist >> horses[i].speed;
    }
    vector <vector <LL>> d(n, vector <LL> (n));
    GETM(d, n, n);
    FOR (i, 0, n) {
        d[i][i] = 0;
    }
    FOR (i, 0, n) {
        FOR (j, 0, n) {
            if (d[i][j] == -1) {
                d[i][j] = INF;
            }
        }
    }
    FOR (k, 0, n) {
        FOR (i, 0, n) {
            FOR (j, 0, n) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
    vector <long double> ans;
    FOR (tt, 0, q) {
        int start, end;
        cin >> start >> end;
        --start;
        --end;
        vector <long double> best(n, INF);
        best[start] = 0;
        vector <int> used(n);
        FOR (i, 0, n) {
            LD good = INF;
            FOR (j, 0, n) {
                if (!used[j] && best[j] < good) {
                    start = j;
                    good = best[j];
                }
            }
            used[start] = 1;
            FOR (j, 0, n) {
                if (d[start][j] <= horses[start].dist) {
                    best[j] = min(best[j], best[start] + d[start][j] * 1.0 / horses[start].speed);
                }
            }
        }
        ans.push_back(best[end]);
    }
    cout << "Case #" << test << ": ";
    FOR (i, 0, q) {
        cout << ans[i] << " ";
    }
    cout << endl;
}

int main()
{
    int n;
    cin >> n;
    cout << fixed << setprecision(10);
    FOR (i, 0, n) {
        cerr << "TEST #" << i + 1 << endl;
        solve(i + 1);
    }
    return 0;
}

