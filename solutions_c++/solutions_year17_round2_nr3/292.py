#include <bits/stdc++.h>
using namespace std;

void gettl(bool b) {
	int crt = 1;
	if (!b) {
		for (int i = 0; i < (int) 2e9; i++) {
			crt *= 17;
		}
		gettl(false);
	}
}

#ifndef _DEBUG
#define ass(_Expr) ((void)0)
#define dout(...) ((void)0)
#else
#define dout(...) cout << __VA_ARGS__; cout.flush()
#define ass(_Expr) assert(_Expr);
#endif

typedef long long ll;
typedef double ld;
const int INF = 2e9;
const ll LINF = 2e18;
const ll MOD = 1e9 + 9;
const int PRIME = 29;
const ld EPS = 1e-10;
const ld PI = 3.14159265358979323846;

ll tdist[100][100];

ld thorse[100][100];

int hs[100], hend[100];

void solve() {
	int n, q;
	cin >> n >> q;
	for (int i = 0; i < n; i++) {
		cin >> hend[i] >> hs[i];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> tdist[i][j];
			if (tdist[i][j] < 0) {
				tdist[i][j] = LINF;
			}
		}
	}
	for (int k = 0; k < n; k++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				tdist[i][j] = min(tdist[i][j], tdist[i][k] + tdist[k][j]);
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (tdist[i][j] > hend[i]) {
				thorse[i][j] = LINF;
			} else {
				thorse[i][j] = ld(tdist[i][j]) / hs[i];
			}
		}
	}
	for (int k = 0; k < n; k++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				thorse[i][j] = min(thorse[i][j], thorse[i][k] + thorse[k][j]);
			}
		}
	}

	for(int i = 0; i < q; i++){
		int a, b;
		cin >> a >> b;
		cout << thorse[a - 1][b - 1] << " ";
	}
	cout << "\n";
}

int main() {
//	ios_base::sync_with_stdio(false);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
//	freopen("keepcounted.in", "r", stdin);
//	freopen("keepcounted.out", "w", stdout);
#endif
	int t;
	cin >> t;
	cout << fixed << setprecision(10);
	for (int tt = 1; tt <= t; tt++) {
		cout << "Case #" << tt << ": ";
		solve();
	}
	return 0;
}
