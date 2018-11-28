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
int a[100];

int main () {
//	freopen (filename".in", "r", stdin);
//	freopen (filename".out", "w", stdout);	
	int nt;
	cin >> nt;
	for (int tt = 1; tt <= nt; tt++) {
		int n, p; 
		scanf ("%d%d", &n, &p);
		for (int i = 0; i < n; i++) scanf ("%d", &a[i]);
		int ans = 0;
		if (p == 2) {
			int cnt[2] = {0, 0};
			for (int i = 0; i < n; i++) {
				cnt[a[i] % 2]++;
			}
			ans = cnt[0] + (cnt[1] + 1) / 2;
		} else if (p == 3) {
			int cnt[3] = {0, 0};
			for (int i = 0; i < n; i++) {
				cnt[a[i] % 3]++;
			}
			int res = min (cnt[1], cnt[2]);
			cnt[1] -= res, cnt[2] -= res;
//			cout << cnt[0] << " " << res << " " << cnt[1] + cnt[2] << endl;
			ans = cnt[0] + res + (cnt[1] + cnt[2] + 2) / 3;
		} else if (p == 4) {
		
		}
		cout << "Case #" << tt << ": ";
		cout << ans;
		cout << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", tt, nt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / tt * nt) / CLOCKS_PER_SEC);
	}
    return 0;
}
