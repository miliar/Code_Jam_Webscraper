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

const ll INF = 1e18;
const ld pi = acos(-1.0);
const int maxn = 1003;
ll dp[maxn][maxn];

void solve() {
	int n, k;
	cin >> n >> k;
	vector < pair < int, int > > a(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i].fst >> a[i].snd;
	}
	sort(a.begin(), a.end());
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= n; j++) {
			dp[i][j] = -INF;
		}
	}
	dp[0][0] = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0) {
				dp[i][j] = 0;
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 2*1ll*a[i-1].fst*1ll*a[i-1].snd);
			}
		}
	}
	ll ans = 0;
	for (int i = k; i <= n; i++) {
		ans = max(ans, dp[i-1][k-1] + 2 * 1ll * a[i-1].fst * 1ll * a[i-1].snd + a[i-1].fst*1ll*a[i-1].fst);
	}
	cout.precision(10);
	cout << fixed << ans * pi << "\n";
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
