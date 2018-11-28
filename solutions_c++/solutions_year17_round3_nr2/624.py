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

int f[2][2][721][2], a[1441];
const int inf = 1e5;

int main () {
//	freopen (filename".in", "r", stdin);
//	freopen (filename".out", "w", stdout);	
	int nt;
	cin >> nt;
	for (int tt = 1; tt <= nt; tt++) {
		scanf ("%d%d", &n, &m);
		memset (a, 0, sizeof (a));
		int x, y;
		for (int i = 0; i < n; i++) {
			scanf ("%d%d", &x, &y); x++; y++;
			for (int j = x; j < y; j++) a[j] = 1;
		}
		for (int i = 0; i < m; i++) {
			scanf ("%d%d", &x, &y); x++; y++;
			for (int j = x; j < y; j++) a[j] = 2;
		}
		memset (f, 127, sizeof (f));
		f[0][0][0][0] = 0;
		f[0][1][0][1] = 0;
		int cur, prv;
		for (int i = 1; i <= 1440; i++) {
			cur = i & 1, prv = cur ^ 1;
			memset (f[cur], 127, sizeof (f[cur]));
			for (int j = 0; j < 2; j++) {
				for (int s = 0; s <= 720; s++) {
					if (a[i] == 1 || a[i] == 0) {
						f[cur][0][s][j] = min (s > 0 ? f[prv][1][s - 1][j] + 1 : inf, s > 0 ? f[prv][0][s - 1][j] : inf);
					}
				}
				for (int s = 0; s <= 720; s++) {
					if (a[i] == 2 || a[i] == 0) {
						f[cur][1][s][j] = min (f[prv][1][s][j], f[prv][0][s][j] + 1);
					}
				}
			}
		}
		cout << "Case #" << tt << ": ";
		int ans = inf;
		for (int i = 0; i < 2; i++) 
			for (int j = 0; j < 2; j++) 
				//cout << f[cur][j][720][i] + (i != j) << " ";
				ans = min (f[cur][j][720][i] + (i != j), ans);
		cout << ans << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", tt, nt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / tt * nt) / CLOCKS_PER_SEC);
	}
    return 0;
}
