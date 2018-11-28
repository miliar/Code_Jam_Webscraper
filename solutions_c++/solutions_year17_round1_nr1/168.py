#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define REP(i,n) for(int i=0; i < (n); ++i)
#define SIZE(c) (int) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define FWD(i,a,b) for (int i=(a); i<(b); ++i)
#define BCK(i,a,b) for (int i=(a); i>(b); --i)
#define PI 3.14159265358979311600
#define pb push_back
#define mp make_pair
#define st first
#define nd second

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

typedef vector < int > VI;
typedef vector<ll> VL;

typedef long double K;

const int N = 55;

int n, m;
char s[N][N];

void solve() {
	cin >> n >> m;
	map<char, int> mnx, mxx, mny, mxy;
	set<char> w;
	REP(i, n) {
		cin >> s[i];
		REP(j, m) if (s[i][j] != '?') {
			char c = s[i][j];
			w.insert(c);
			if (!mnx.count(c)) mnx[c] = i; else mnx[c] = min(mnx[c], i);
			if (!mxx.count(c)) mxx[c] = i; else mxx[c] = max(mxx[c], i);
			if (!mny.count(c)) mny[c] = j; else mny[c] = min(mny[c], j);
			if (!mxy.count(c)) mxy[c] = j; else mxy[c] = max(mxy[c], j);
		}
	}

	for (auto& c : w) {
		for (int i = mnx[c]; i <= mxx[c]; ++i) {
			for (int j = mny[c]; j <= mxy[c]; ++j) {
				s[i][j] = c;
			}
		}
	}

	REP(i, n) REP(j, m) if (s[i][j] == '?') {
		for (int x = 0; x < n; ++x) {
			for (int y = 0; y < m; ++y) {
				set<char> w;
				for (int a = min(i, x); a <= max(i, x); ++a) {
					for (int b = min(j, y); b <= max(j, y); ++b) {
						if (s[a][b] != '?') w.insert(s[a][b]);
					}
				}
				if (w.size() == 1) {
					char c = *w.begin();
					if (mnx[c] >= min(i, x) && mxx[c] <= max(i, x) && mny[c] >= min(j, y) && mxy[c] <= max(j, y)) {
						mnx[c] = min(i, x);
						mxx[c] = max(i, x);
						mny[c] = min(j, y);
						mxy[c] = max(j, y);
						for (int a = min(i, x); a <= max(i, x); ++a) {
							for (int b = min(j, y); b <= max(j, y); ++b) {
								s[a][b] = c;
							}
						}
						goto out;
					}
				}
			}
		}
		out:;
	}
	cout << endl;
	REP(i, n) {
		cout << s[i] << '\n';
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	REP(i, t) {
		cerr << i << endl;
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}