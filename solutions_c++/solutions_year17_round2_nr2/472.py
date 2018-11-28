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

string get_ans(const vector <int> &v, const string &colors)
{
    vector <int> horses;
    FOR (i, 0, 6) {
        FOR (j, 0, v[i]) {
            horses.push_back(i);
        }
    }
    int n = horses.size();
    int delta = (n + 1) / 2;
    vector <int> res;
    FOR (i, 0, (n + 1) / 2) {
        res.push_back(horses[i]);
        if (n % 2 == 0 || i != (n + 1) / 2 - 1) {
            res.push_back(horses[(i + delta) % horses.size()]);
        }
    }
    vector <int> res2 = res;
    FOR (i, 0, n) {
        if (!(1 <= abs(res[i] - res[(i + 1) % n]) && abs(res[i] - res[(i + 1) % n]) <= 4)) {
            return "";
        }
    }
    string ans;
    for (auto i: res) {
        ans += colors[i];
    }
    sort(IT(res));
    sort(IT(horses));
    assert(res == horses);
    return ans;
}

int solve(int test)
{
    int n;
    cin >> n;
    vector <int> v(6);
    GET(v, 6);
    string colors = "ROYGBV";
    FOR (i, 0, 6) {
        auto tres = get_ans(v, colors);
        if (tres == "") {
            std::rotate(v.begin(), v.begin() + 1, v.end());
            std::rotate(colors.begin(), colors.begin() + 1, colors.end());
            continue;
        }
        CASE(test, tres);
        return 0;
    }
    CASE(test, "IMPOSSIBLE");
    return 0;
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

