#include <bits/stdc++.h>

using namespace std;

map<int, int> dp;

int best(vector<int> gcts, int p) {
	if(gcts[0] > 0) {
		int zct = gcts[0];
		gcts[0] = 0;

		return zct + best(gcts, p);
	}

	int pos = 0;
	for(int i = 1; i < 4; i++) {
		pos += gcts[i];
		pos *= 101;
	}
	pos += p;

	if(dp.count(pos)) {
		return dp[pos];
	}

	int ret = 0;

	for(int i = 1; i <= 3; i++) {
		if(gcts[i] == 0) continue;

		for(int j = 1; j <= 3; j++) {
			if(gcts[j] == 0) continue;

			vector<int> ngcts = gcts;
			ngcts[i]--;
			ngcts[j]--;
			if(ngcts[i] < 0 || ngcts[j] < 0) {
				continue;
			}

			int ng = (i + j) % p;
			int bc = 0;
			if(ng == 0) {
				bc = 1;
			}
			else {
				ngcts[ng]++;
			}

			ret = max(bc + best(ngcts, p), ret);
		}
	}

	dp[pos] = ret;

	return ret;
}

void runTestCase(int t) {
	int n, p;
	cin >> n >> p;

	vector<int> gcts(4, 0);

	int sum = 0;

	for(int i = 0; i < n; i++) {
		int g;
		cin >> g;

		sum += g;

		g %= p;

		gcts[g]++;
	}

	int ans = best(gcts, p);
	if(sum % p != 0) {
		ans++;
	}

	cout << "Case #" << t << ": ";
	cout << ans << endl;
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		runTestCase(i);
	}

	return 0;
}

