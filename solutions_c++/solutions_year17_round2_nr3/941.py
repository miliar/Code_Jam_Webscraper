#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cassert>
#include <bitset>
#include <fstream>
#include <stack>
#include <cstdlib>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define fst first
#define snd second

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef long double ld;

template<class T>
bool chmin(T& x, const T& y) {
	if (y < x) {
		x = y;
		return true;
	}
	return false;
}

template<class T>
bool chmax(T& x, const T& y) {
	if (x < y) {
		x = y;
		return true;
	}
	return false;
}

template<class T, class P>
ostream& operator <<(ostream& os, const pair<T, P>& p) {
	return os << "(" << p.first << ", " << p.second << ")";
}

template<class T>
ostream& operator <<(ostream& os, const vector<T>& v) {
	os << "[";
	bool was = false;
	for (const T& x : v) {
		if (was) {
			os << ", ";
		} else {
			was = true;
		}
		os << x;
	}
	os << "]";
	return os;
}

template<class T>
ostream& operator <<(ostream& os, const set<T>& v) {
	os << "[";
	bool was = false;
	for (const T& x : v) {
		if (was) {
			os << ", ";
		} else {
			was = true;
		}
		os << x;
	}
	os << "]";
	return os;
}

template<class T, class P>
ostream& operator <<(ostream& os, const map<T, P>& v) {
	os << "[";
	bool was = false;
	for (const auto& x : v) {
		if (was) {
			os << ", ";
		} else {
			was = true;
		}
		os << x;
	}
	os << "]";
	return os;
}

template<class T>
T sqr(const T& x) {
	return x * x;
}

//////////////////////////////////////////////

const int maxn = 103;
ll E[maxn], S[maxn], a[maxn][maxn];
bool used[maxn];
const ll INF = 1e18;
ld d[maxn];

void solve() {
	int n, q;
	cin >> n >> q;
	for (int i = 1; i <= n; i++) {
		cin >> E[i] >> S[i];
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> a[i][j];
			if (a[i][j] == -1) {
				if (i == j) {
					a[i][j] = 0;
				} else {
					a[i][j] = INF;
				}
			}
		}
	}
	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
			}
		}
	}
	while (q--) {
		fill(used, used + maxn, 0);
		int x, y;
		cin >> x >> y;
		for (int i = 1; i <= n; i++) {
			d[i] = INF;
		}
		d[x] = 0;
		for (int j = 1; j <= n; j++) {
			int num = -1;
			for (int i = 1; i <= n; i++) {
				if (!used[i] && (num == -1 || d[num] > d[i])) {
					num = i;
				}
			}
			used[num] = true;
			for (int i = 1; i <= n; i++) {
				if (used[i]) {
					continue;
				}
				if (a[num][i] <= E[num]) {
					d[i] = min(d[i], d[num] + a[num][i] * 1./S[num]);
				}
			}
		}
		cout.precision(10);
		cout << fixed << d[y] << " ";
	}
	cout << "\n";
}

int main() {
#ifdef LOCAL
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	//cout << endl << endl;
	
#endif
	
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cout << "Case #" << test << ": ";
		solve();
	}
	
	
	return 0;

}
