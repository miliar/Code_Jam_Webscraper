#include <bits/stdc++.h>

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define forn(i, n) for(int i=0;i<(n);++i)
#define clr(ar, val) memset(ar, val, sizeof(ar))

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<ld, ld> point;

const int MAXN = 1e3 + 200;
const int INF = int(1e9) + 7;
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

int test, iter;

int n;
double d, ans;
vector<pair<double, double>> h;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> test;

    for (int iter = 1; iter <= test; iter++) {
        h.clear();
        cin >> d >> n;
        for (int i = 0; i < n; i++) {
            double x, v;
            cin >> x >> v;
            h.push_back({x, v});
        }
        sort(h.begin(), h.end());
        reverse(h.begin(), h.end());
        ans = 0;
        for (auto p : h) {
            ans = max(ans, (d - p.first) / p.second);
        }
        ans = d / ans;
        cout << "Case #" << iter << ": " << setprecision(18) << ans << endl;
    }
    return 0;
}
