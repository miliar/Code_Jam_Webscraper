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

const int N = 1010;

int p[N], a[N];

int n, c, m, ans;

inline bool check(int mid) {
	int cur = 0; ans = 0;
	for (int i = 1; i <= n; i++) {
		if (a[i] > cur + mid) {
			return 0;
		}
		if (a[i] > mid) {
			ans += a[i] - mid;
		}
		cur = cur + mid - a[i];
	}
	return 1;
}

inline void solve() {
	cin >> n >> c >> m;
	int x, y;
	memset(p, 0, sizeof(p));
	memset(a, 0, sizeof(a));
	int l = 0, r = m, mid;
	for (int i = 1; i <= m; i++) {
		cin >> x >> y;
		p[y]++;
		a[x]++;
		l = max(l, p[y]);
	}
	while (r - l > 1) {
		mid = (l + r) >> 1;
		if (check(mid)) {
			r = mid;
		}
		else {
			l = mid;
		}
	}
	if (check(l)) {
		cout << l << " " << ans << endl;
	}
	else {
		check(r);
		cout << r << " " << ans << endl;
	}
}

int main() {
	freopen (fname"B-large.in.txt", "r", stdin);
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
