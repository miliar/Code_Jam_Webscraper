	//g++ -std=c++0x your_file.cpp -o your_program
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

typedef long long ll;

const int N = 55;

ll r[N], q[N][N];

int n, m;

inline bool validate(int j, ll x) {
	if (!x) {
		return 0;
	}
	for (int i = 1; i <= n; i++) {
		if (!(9ll * x * r[i] <= 10ll * q[i][j] && 10ll * q[i][j] <= 11ll * x * r[i])) {
			return 0;
		}
	}
	return 1;
}

inline bool check(int j) {
	ll x;
	for (int i = 1; i <= n; i++) {
		x = (10 * q[i][j] + 11 * r[i] - 1) / (11 * r[i]);
		if (validate(j, x)) {
			return 1;
		}
	}
	return 0;
}

inline void solve() {
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		cin >> r[i];
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cin >> q[i][j];
		}
	}	
	int ans = 0;
	if (n == 1) {
		for (int j = 1; j <= m; j++) {
			if (check(j)) {
				ans++;
			}
		}
		cout << ans << endl;
		return ;
	}
	sort (q[2] + 1, q[2] + m + 1);
	do {
		int cur = 0;
		for (int j = 1; j <= m; j++) {
			if (check(j)) {
				cur++;
			}
		}
		ans = max(ans, cur);
	}while (next_permutation(q[2] + 1, q[2] + m + 1));
	cout << ans << endl;
}

int main() {
	freopen (fname"B-small-attempt0.in.txt", "r", stdin);
	freopen (fname"out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++) {
		cout << "Case #" << Case << ": ";
		solve();		
	}
	return 0;
}
