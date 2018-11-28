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

string gen_str(char A, char B, int n)
{
	string s;
	for (int i = 0; i < n; i++) s += A, s += B;
	re s; 
}

int to[255][255];

int main () {
//	freopen (filename".in", "r", stdin);
//	freopen (filename".out", "w", stdout);	
	to['G']['R'] = 1; to['R']['G'] = 1;
	to['Y']['V'] = 1; to['V']['Y'] = 1;
	to['B']['O'] = 1; to['B']['O'] = 1;

	to['R']['B'] = 1; to['B']['R'] = 1;
	to['R']['Y'] = 1; to['Y']['R'] = 1;
	to['B']['Y'] = 1; to['Y']['B'] = 1;

	int nt;
	cin >> nt;
	for (int tt = 1; tt <= nt; tt++) {
		int r, o, y, g, b, v;
		scanf ("%d %d %d %d %d %d %d\n", &n, &r, &o, &y, &g, &b, &v);
		vector <pair <ii, char>> a = {{{r - g, 0}, 'R'}, {{y - v, 0}, 'Y'}, {{b - o, 0}, 'B'}};
		sort (all (a));
		a[0].fi.se = 0;
		a[1].fi.se = 1;
		a[2].fi.se = 2;
		string ans = "IMPOSSIBLE";
		if (a[2].fi.fi == 0) {
			if (r  > 0 && y == 0 && b == 0) ans = gen_str('R', 'G', g);
			if (r == 0 && y  > 0 && b == 0) ans = gen_str('Y', 'V', v);
			if (r == 0 && y == 0 && b > 0 ) ans = gen_str('B', 'O', o);
		} else {
			if (a[0].fi.fi + a[1].fi.fi >= a[2].fi.fi) { 
				ans = "";
				for (int i = 0; i < n; i++) {
					sort (all (a));
					if (a[2].fi.fi > 0) ans += a[2].se, a[2].fi.fi--;
					if (a[1].fi.fi > 0) ans += a[1].se, a[1].fi.fi--;
				}
			}
			for (int i = 0; i < sz (ans); i++) if (ans[i] == 'R') { ans = ans.substr(0, i) + gen_str('R', 'G', g) + ans.substr(i); break; }
			for (int i = 0; i < sz (ans); i++) if (ans[i] == 'Y') { ans = ans.substr(0, i) + gen_str('Y', 'V', v) + ans.substr(i); break; }
			for (int i = 0; i < sz (ans); i++) if (ans[i] == 'B') { ans = ans.substr(0, i) + gen_str('B', 'O', o) + ans.substr(i); break; }
		}
		if (ans != "IMPOSSIBLE") {
			for (int i = 0; i + 1 < n; i++) {			
				if (to[ans[i]][ans[i + 1]] == 0) printf ("%c %c\n", ans[i], ans[i + 1]);
				assert (to[ans[i]][ans[i + 1]]);
			}
			if (to[ans[n - 1]][ans[0]] == 0) printf ("%c %c\n", ans[n - 1], ans[0]);
			assert (to[ans[n - 1]][ans[0]]);
		}

		cout << "Case #" << tt << ": ";
		cout << ans << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", tt, nt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / tt * nt) / CLOCKS_PER_SEC);
	}
    return 0;
}

