#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>

using namespace std;

void solve() {
	int n, p;
	cin >> n >> p;

	vector<int> r(n);
	for (int i = 0; i < n; i++) {
		cin >> r[i];
	}

	vector<vector<int>> q(n, vector<int>(p));
	vector<vector<int>> L(n, vector<int>(p));
	vector<vector<int>> R(n, vector<int>(p));
	map<int, int> mp;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < p; j++) {
			cin >> q[i][j];
		}
		sort(q[i].begin(), q[i].end());
		for (int j = 0; j < p; j++) {
			L[i][j] = (10 * q[i][j] + 11 * r[i] - 1) / (11 * r[i]);
			R[i][j] = (10 * q[i][j]) / (9 * r[i]);
			mp[L[i][j]];
			mp[R[i][j]];
		}
	}
	int k = 0;
	vector<int> inv;
	for (auto &kv : mp) {
		inv.push_back(kv.first);
		kv.second = k++;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < p; j++) {
			L[i][j] = mp[L[i][j]];
			R[i][j] = mp[R[i][j]];
		}
	}

	int ans = 0;
	vector<vector<bool>> used(n, vector<bool>(p));
	for (int val = 0; val < k; val++) {
		vector<int> ls;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++) {
				if (!used[i][j] && L[i][j] <= val && val <= R[i][j]) {
					ls.push_back(j);
					break;
				}
			}
		}
		if (ls.size() == n) {
			for (int i = 0; i < n; i++) {
				used[i][ls[i]] = true;
			}
			ans++;
			val--;
		}
	}
	cout << ans << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "case #" << i << ": ";
		solve();
	}
}