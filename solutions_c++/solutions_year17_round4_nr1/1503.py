#include <bits/stdc++.h>
using namespace std;

#ifdef HELTHAZAR
	#define DEBUG true
#else
	#define DEBUG false
#endif

#define dout if (DEBUG) cout

map<vector<int>, int> dp;

int rec(vector<int> v, int p, int sum) {
	if (dp.find(v) != dp.end()) {
		return dp[v];
	}

	int maxdp = 0;
	for (int i = 0; i < 4; i++) {
		if (v[i] == 0) {
			continue;
		}

		int sumi = (sum - i + p) % p;
		int dpi = 0;
		if (sumi == 0) {
			dpi++;
		}

		v[i]--;
		dpi += rec(v, p, sumi);
		maxdp = max(maxdp, dpi);
		v[i]++;
	}

	dp[v] = maxdp;
	return maxdp;
}

void solve() {
	dp.clear();

	int n, p;
	cin >> n >> p;

	vector<int> v(4, 0);
	int sum = 0;
	for (int i = 0; i < n; i++) {
		int val;
		cin >> val;
		v[val % p]++;
		sum = (sum + val) % p;
	}

	cout << rec(v, p, sum);
}

int main() {
	int test;
	//scanf("%d", &test);
	cin >> test;

	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";

		solve();

		cout << endl;
		//printf("\n");
	}
}
