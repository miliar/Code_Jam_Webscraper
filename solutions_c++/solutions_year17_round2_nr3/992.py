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

const int N = 100;
const ll inf = 1e18;
double d[N][N];
int l[N], v[N], a[N][N];
ll b[N][N];

int main () {
//	freopen (filename".in", "r", stdin);
//	freopen (filename".out", "w", stdout);	
	int nt;
	cin >> nt;
	for (int tt = 1; tt <= nt; tt++) {
		scanf ("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf ("%d%d", &l[i], &v[i]);
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf ("%d", &a[i][j]);
				if (a[i][j] == -1) b[i][j] = inf;
				else b[i][j] = a[i][j];
			}
		}
		for (int i = 0; i < n; i++) {
			set <pair <ll, int>> st;
			for (int j = 0; j < n; j++) d[i][j] = inf;
			d[i][i] = 0;
			st.insert (mp (0ll, i));
			while (st.size() > 0) {
				ii cur = *st.begin(); st.erase (st.begin());
				int x = cur.se;
				for (int j = 0; j < n; j++) {
					if (d[i][x] + b[x][j] < d[i][j]) {
						st.erase (mp (d[i][j], j));
						d[i][j] = d[i][x] + b[x][j];
						st.insert (mp ((ll)d[i][j], j));
					}
				}
			}
			for (int j = 0; j < n; j++) if (d[i][j] > l[i]) d[i][j] = -1;
		}
		cout << "Case #" << tt << ": ";

		for (int i = 0; i < n; i++) 
			for (int j = 0; j < n; j++) if (d[i][j] != -1) d[i][j] = d[i][j] / v[i];
		for (int i = 0; i < m; i++) {
			int u, v;
			scanf ("%d%d", &u, &v); u--; v--;
			set <pair <double, int>> st;
			vector <double> ds(n, inf);
			ds[u] = 0;
			st.insert (mp (0, u));
			while (st.size() > 0) {
				ii cur = *st.begin(); st.erase (st.begin());
				int x = cur.se;
				if (x == v) break;
				for (int j = 0; j < n; j++) {
					if (d[x][j] == -1) continue;
					if (ds[x] + d[x][j] < ds[j]) {
						st.erase (mp (ds[j], j));
						ds[j] = ds[x] + d[x][j];
						st.insert (mp (ds[j], j));
					}
				}
			}
			printf ("%0.10lf ", ds[v]);
		}
		
		cout << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", tt, nt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / tt * nt) / CLOCKS_PER_SEC);
	}
    return 0;
}
