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

const int maxn = 24*60+3;
int dp[maxn][maxn][2][2];
const int INF = 1e9;

void solve() {
	int n, m;
	cin >> n >> m;
	int C = 24 * 60;
	vector < int > used(24*60);
	for (int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;
		for (int i = x; i < y; i++) {
			used[i] = 1;
		}
	}
	for (int i = 0; i < m; i++) {
		int x, y;
		cin >> x >> y;
		for (int i = x; i < y; i++) {
			used[i] = 2;
		}
	}
	for (int i = 0; i <= C; i++) {
		for (int j = 0; j <= C; j++) {
			for (int k = 0; k < 2; k++) {
				for (int fir = 0; fir < 2; fir++) {
					dp[i][j][k][fir] = INF;
				}
			}
		}
	}
	if (used[0] == 1) {
		dp[1][1][0][0] = 0;
	} else if (used[0] == 2) {
		dp[1][0][1][1] = 0;
	} else {
		dp[1][1][0][0] = 0;
		dp[1][0][1][1] = 0;
	}
	for (int i = 2; i <= C; i++) {
		for (int j = 0; j <= i; j++) {
			for (int k = 0; k < 2; k++) {
				for (int fir = 0; fir < 2; fir++) {
					if (used[i-1] == 1) {
						if (j > 0 && k == 0) {
							dp[i][j][k][fir] = min(dp[i-1][j-1][0][fir], dp[i-1][j-1][1][fir] + 1);
						}
					} else if (used[i-1] == 2) {
						if (i - j > 0 && k == 1) {
							dp[i][j][k][fir] = min(dp[i-1][j][1][fir], dp[i-1][j][0][fir] + 1);
						}
					} else {
						if (k == 0 && j > 0) {
							dp[i][j][k][fir] = min(dp[i-1][j-1][0][fir], dp[i-1][j-1][1][fir] + 1);
						} else if (k == 1 && i - j > 0){
							dp[i][j][k][fir] = min(dp[i-1][j][1][fir], dp[i-1][j][0][fir] + 1);
						}
					}
				}
			}
		}
	}
	cout << min(min(dp[C][C/2][0][0], dp[C][C/2][0][1] + 1), min(dp[C][C/2][1][0] + 1, dp[C][C/2][1][1])) << "\n";
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
