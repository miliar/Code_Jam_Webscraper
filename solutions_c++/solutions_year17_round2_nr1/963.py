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
		int d;
		scanf ("%d%d", &d, &n);
//		printf ("%d %d\n", d, n);
		vector <pair <double, double>> a;
		for (int i = 0; i < n; i++) {
			int k, s;
			scanf ("%d%d", &k, &s);
			a.pb (mp (k, s));
//			printf ("%d %d\n", k, s);
		}
		a.pb (mp (d, 0));
		sort (all (a));
		double ans = 1e18;
		double t = 0;
		for (int i = 0; i < n; i++) {
			double dt = 1e18;
			for (int j = 0; j < n; j++)  {
				if (a[j + 1].se >= a[j].se) continue;
//				cout << a[j + 1].fi  - a[j].fi << " " << a[j].se - a[j + 1].se << endl;
				dt = min (dt, (a[j + 1].fi - a[j].fi) / (a[j].se - a[j + 1].se));
//				cout << dt << endl;
			}
			for (int j = 0; j < n; j++) {
				a[j].fi += dt * a[j].se;
//				cout << a[j].fi << endl;
			}
			for (int j = n - 1; j >= 0; j--) {
				if (abs(a[j].fi - a[j + 1].fi) < 1e-9) a[j].se = a[j + 1].se; 
			}
			if (dt == 1e18) break;
			t += dt;
			
			ans = min (ans, a[0].fi / t);
//			cout << t << endl;
		}
		cout << "Case #" << tt << ": ";
		printf ("%0.10lf", ans);
		cout << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", tt, nt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / tt * nt) / CLOCKS_PER_SEC);
	}
    return 0;
}
