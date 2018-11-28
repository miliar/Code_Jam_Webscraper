#include <iostream>
#include <bits/stdc++.h>


using namespace std;

#define re return
#define mp make_pair
#define forn(i, n) for (int i = 0; i < n; i++)
#define sz(a) int(a.size())
#define fi first
#define se second

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


void solve() {
	int n, m, c;
	int x = 0, y = 0;
	vector<int> kk(1000 + 1, 0), pp(1000 + 1, 0);
	cin >> n >> c >> m;
	forn (i, m) {
		int b, p;
		cin >> p >> b;
		p--;
		b--;
		kk[b]++;
		x = max(x, kk[b]);
		pp[p]++;
	}
	int sum = 0;
	forn (i, n) {
		sum += pp[i];
		x = max(x, (sum + i) / (i + 1));
	}
	forn (i, n) {
		y += max(0, pp[i] - x);
	}	
	cout << x << " " << y << "\n";
}

int main() {
	iostream::sync_with_stdio(0), cin.tie(0);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	forn (i, t) {
		cout << "Case #" << i + 1 <<": ";
		solve();
	}
	re 0;
}