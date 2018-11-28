#include <functional>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cassert>
#include <ctime>
#include <map>
#include <math.h>
#include <cstdio>
#include <set>
#include <deque>
#include <memory.h>
#include <queue>

#pragma comment(linker, "/STACK:64000000")
typedef long long ll;

using namespace std;

const int MAXK = -1;
const int MAXN = -1;
const int MOD = 1; // 1000 * 1000 * 1000 + 7;
const int INF = (int)(1e9);

int fastsolve(vector<int> a, int p) {
	int n = a.size();
	vector<int> cnt(p);
	for (int i = 0; i < n; i++) cnt[a[i] % p]++;

	int ans = 0;

	map<vector<int>, int> mp;
	// 0..p-1 is cnt
	// p is remainder
	function<int(vector<int>)> rec = [&](vector<int> b) {
		if (mp.count(b)) return mp[b];
		int ans = 0;
		int cur = b[p] == 0;
		for (int i = 0; i < p; i++) {
			if (b[i] > 0) {
				vector<int> nb = b;
				nb[i]--;
				nb[p] = (b[p] + p - i) % p;
				ans = max(ans, rec(nb) + cur);
			}
		}
		return mp[b] = ans;
	};
	cnt.push_back(0);
	return rec(cnt);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";

		int n, p;
		cin >> n >> p;
		vector<int> a(n);
		for (int i = 0; i < n; i++) cin >> a[i];

		int ans = fastsolve(a, p);

		cout << ans << endl;
		cerr << ans << endl;
	}

	return 0;
}