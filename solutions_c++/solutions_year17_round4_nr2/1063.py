#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define makeunique(x) sort(all(x)), (x).resize(unique(x) - (x).begin())
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqrt(x) sqrt(abs(x))
#define y0 y3487465
#define y1 y8687969
#define j0 j5743892
#define j1 j542893
                         
typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) { re x > 0 ? x : -x; }
template<class T> T gcd(T a, T b) { re a ? gcd (b % a, a) : b; }
template<class T> T sqr(T a) { re a * a; }
template<class T> T sgn(T a) { re a > 0 ? 1 : (a < 0 ? -1 : 0); }

#define filename ""

int n;
int m;


int main () {
//	freopen (filename".in", "r", stdin);
//	freopen (filename".out", "w", stdout);	
	int nt;
	cin >> nt;
	for (int tt = 1; tt <= nt; tt++) {
		int n, c, m;
		scanf ("%d%d%d", &n, &c, &m);
		vii a;
		for (int i = 0; i < m; i++) {
			int x, y;
			scanf ("%d%d", &x, &y); x--; y--;
			a.pb (mp (x, y));
		}
		sort (all (a));
		int res = 0, ans = 0;
		if (c == 2) {
			int cnt[2] = {0, 0};
			vi b[2] = {vi(n, 0), vi(n, 0)};
			int zero = 0;
			for (int i = 0; i < m; i++) {
				cnt[a[i].se] ++;
				if (a[i].fi == 0) zero ++;
				b[a[i].se][a[i].fi] ++;
			}
			res = max (max (cnt[0], cnt[1]), zero);
			for (int i = 1; i < n; i++)
				ans += max (0, b[1][i] + b[0][i] - res);
		}
		cout << "Case #" << tt << ": ";
		cout << res << " " << ans;
		cout << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", tt, nt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / tt * nt) / CLOCKS_PER_SEC);
	}
    return 0;
}
