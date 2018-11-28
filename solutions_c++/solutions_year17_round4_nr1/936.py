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
    int n, s;
    cin >> n >> s;
    vector <int> v(n);
    GET(v, n);
    FOR (i, 0, n) {
        v[i] %= s;
    }
    int zero = count(IT(v), 0);
    int one = count(IT(v), 1);
    int two = count(IT(v), 2);
    int three = count(IT(v), 3);
    vector <vector <vector <vector <int>>>> dp(zero + 2, vector <vector <vector <int>>> (one + 2, vector <vector <int>> (two + 2, vector <int> (three + 2, -2))));
    dp[0][0][0][0] = 0;
    FOR (i, 0, zero + 1) {
        FOR (j, 0, one + 1) {
            FOR (k, 0, two + 1) {
                FOR (l, 0, three + 1) {
                    int current = !((j + 2 * k + 3 * l) % s);
                    dp[i][j][k][l + 1] = max(dp[i][j][k][l + 1], dp[i][j][k][l] + current);
                    dp[i][j][k + 1][l] = max(dp[i][j][k + 1][l], dp[i][j][k][l] + current);
                    dp[i][j + 1][k][l] = max(dp[i][j + 1][k][l], dp[i][j][k][l] + current);
                    dp[i + 1][j][k][l] = max(dp[i + 1][j][k][l], dp[i][j][k][l] + current);
                }
            }
        }
    }
    CASE(test, dp[zero][one][two][three]);
}

int main()
{
    int n;
    cin >> n;
    FOR (i, 0, n) {
        solve(i + 1);
    }
    return 0;
}

