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

const ld pi = acos((ld)-1.0);

#define filename ""

int n;
int m;


int main () {
//	freopen (filename".in", "r", stdin);
//	freopen (filename".out", "w", stdout);	
	int nt;
	cin >> nt;
	for (int tt = 1; tt <= nt; tt++) {
		scanf ("%d%d", &n, &m);
		vii a;
		for (int i = 0; i < n; i++) {
			int r, h;
			scanf ("%d%d", &r, &h);
			a.pb (mp (r, h));
		}
		sort (all (a));
		reverse (all (a));
		double ans = 0;
		for (int i = 0; i + m <= n; i++) {
			vector <double> b;
			for (int j = i + 1; j < n; j++) {
				b.pb (2 * pi * a[j].fi * a[j].se);
			}
			sort (all (b));
			reverse (all (b));
			double res = pi * sqr((double)a[i].fi) + 2 * pi * a[i].fi * a[i].se;
			for (int i = 0; i + 1 < m; i++) {
				res += b[i];
			}
			ans = max (ans, res);
		}
		cout << "Case #" << tt << ": ";
		printf ("%0.10lf", ans);
		cout << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", tt, nt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / tt * nt) / CLOCKS_PER_SEC);
	}
    return 0;
}
