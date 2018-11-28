#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int can(const vector <pair <int, int> > &arr, int n, int c, int mid) {
	int ans = 0;
	vector <vector <int> > dp(mid, vector <int>(n, 0));
	map <int, set <int> > bought;
	for (const auto &p : arr) {
		int pos = p.first - 1;
		int cust = p.second;
		bool ok = false;
		for (int tr = pos; tr >= 0 && !ok; --tr) {
			for (int row = 0; row < mid && !ok; ++row) {
				if (bought[cust].count(row))
					continue;
				if (dp[row][tr] == 0) {
					dp[row][tr] = cust;
					bought[cust].insert(row);
					ok = true;
					if (tr < pos)
						++ans;
					break;
				}
			}
		}
		if (!ok)
			return -1;
	}
	return ans;
}

int can2(const vector <pair <int, int> > &arr, int n, int c, int mid) {
	map <int, int> seats;
	map <int, int> users;
	for (const auto &p : arr) {
		int pos = p.first - 1;
		int cust = p.second;
		++seats[pos];
		++users[cust];
		if (users[cust] > mid)
			return -1;
	}
	int cnt = 0;
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		cnt += mid;
		cnt -= seats[i];
		if (cnt < 0)
			return -1;
		if (seats[i] > mid)
			ans += seats[i] - mid;
	}
	return ans;
}

void solve(int t) {
	int n, c, m;
	cin >> n >> c >> m;
	vector <pair <int, int> > arr(m);
	for (int i = 0; i < m; ++i)
		cin >> arr[i].first >> arr[i].second;
	sort(arr.begin(), arr.end());
	int l = 1, r = m;
	while (l < r) {
		int mid = (l + r) / 2;
		if (can2(arr, n, c, mid) != -1)
			r = mid;
		else
			l = mid + 1;
	}
	cout << "Case #" << t << ": " << l << " " << can2(arr, n, c, l) << endl;
}

int main() {
	freopen("B-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; ++t)
		solve(t);
	return 0;
}