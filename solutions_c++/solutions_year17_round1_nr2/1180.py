#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

bool possible(int n, const int target[], int q[])
{
	for (int i = 0; i < n; i++) {
		int mins = 10 * q[i] / (11 * target[i]), maxs = 10 * q[i] / (9 * target[i]);
		bool ok = true;
		for (int j = 0; j < n; j++) {
			if (10 * q[j] < 9 * target[j] * mins || 11 * target[j] * mins < 10 * q[j]) {
				ok = false;
				break;
			}
		}
		if (ok) 
			return true;
		ok = true;
		for (int j = 0; j < n; j++) {
			if (10 * q[j] < 9 * target[j] * maxs || 11 * target[j] * maxs < 10 * q[j]) {
				ok = false;
				break;
			}
		}
		if (ok) 
			return true;
	}
	return false;
}

int rec2(int p, int c, const vector<int>& target, vector<vector<int>>& v, set<int>& used)
{
	if (p == c) {
		return 0;
	}

	int ret = 0;
	for (int i = 0; i < p; i++) {
		if (used.count(i)) continue;
		int q[2] = {v[0][c], v[1][i]};
		int pp = possible(2, &target[0], q);

		used.insert(i);
		ret = max(ret, pp + rec2(p, c+1, target, v, used));
		used.erase(i);
	}
	return ret;
}


int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int n, p;
		cin >> n >> p;
		vector<int> target(n);
		for (int j = 0; j < n; j++){
			cin >> target[j];
		}
		vector<vector<int>> q(n);
		for (int j = 0; j < n; j++){
			q[j].resize(p);
			for (int k = 0; k < p; k++){
				cin >> q[j][k];
			}
		}
		if (n == 1) {
			int ans = 0;
			for (int k = 0; k < p; k++){
				ans += possible(1, &target[0], &q[0][k]);
			}
			printf("Case #%d: %d\n", i + 1, ans);
		}
		if (n == 2) {
			set<int> used;
			printf("Case #%d: %d\n", i + 1, rec2(p, 0, target, q, used));
		}
	}
	return 0;
}