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

S Client
{
    int position;
    int id;
};

int n, k;
vector <vector <int>> g;
vector <int> mt;
vector <char> used;

bool try_kuhn (int v) {
	if (used[v])  return false;
	used[v] = true;
	for (size_t i=0; i<g[v].size(); ++i) {
		int to = g[v][i];
		if (mt[to] == -1 || try_kuhn (mt[to])) {
			mt[to] = v;
			return true;
		}
	}
	return false;
}

int solve_small(int test)
{
    int n, c, m;
    cin >> n >> c >> m;
    vector <Client> v(m);
    vector <vector <int>> cnt(2, vector <int> (2));
    FOR (i, 0, m) {
        cin >> v[i].position >> v[i].id;
    }
    if (c != 2) {
        cout << "Case #" << test << ": " << 0 << " " << 0 << endl;
        return 0;
    }
    FOR (i, 0, m) {
        ++cnt[v[i].id - 1][v[i].position != 1];
    }
    int res = min(cnt[0][0], cnt[1][1]);
    cnt[0][0] -= res;
    cnt[1][1] -= res;
    int res2 = min(cnt[1][0], cnt[0][1]);
    cnt[1][0] -= res2;
    cnt[0][1] -= res2;
    res += res2;
    if (cnt[0][0] != 0 && cnt[1][0] != 0) {
        cout << "Case #" << test << ": " << res + cnt[0][0] + cnt[1][0] << " " << 0 << endl;
        return 0;
    }
    if (cnt[0][1] != 0 && cnt[1][1] != 0) {
        g.assign(m, vector <int> ());
        FOR (i, 0, v.size()) {
            FOR (j, 0, v.size()) {
                if (v[i].id == 1 && v[j].id == 2 && v[i].position != v[j].position && v[i].position != 1 && v[j].position != 1) {
                    g[i].push_back(j);
                }
            }
        }
        mt.assign(m, -1);
        FOR (i, 0, m) {
            used.assign(m, false);
		    try_kuhn(i);
	    }
        int add = 0;
        FOR (i, 0, m) {
		    if (mt[i] != -1) {
			    ++add;
		    }
        }
        cout << "Case #" << test << ": " << res + max(cnt[0][1], cnt[1][1]) << " " << max(min(cnt[0][1], cnt[1][1]) - add, 0) << endl;
        return 0;
    }
    cout << "Case #" << test << ": " << res + cnt[0][0] + cnt[0][1] + cnt[1][0] + cnt[1][1] << " " << 0 << endl;
    return 0;
}

int main()
{
    int n;
    cin >> n;
    FOR (i, 0, n) {
        cerr << "TEST " << i + 1 << endl;
        solve_small(i + 1);
    }
    return 0;
}

