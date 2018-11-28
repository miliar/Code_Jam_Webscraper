#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <map>
using namespace std;
#define int long long

int solve() {
	int n, k;
	cin >> n >> k;
	int cnt = k;
	map <int, int> free;
	free[n] = 1;
	while (true && !free.empty()) {
		auto elem = *free.rbegin();
		free.erase(elem.first);
		if (elem.second >= cnt) {
			return elem.first;
		} else {
			int right = (elem.first - 1) / 2;
			int left = elem.first - 1 - right;
			if (right != 0)
				free[right] += elem.second;
			if (left != 0)
				free[left] += elem.second;
			cnt -= elem.second;
		}
	}
}

signed main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int ans = solve();
		int right = (ans - 1) / 2;
		int left = ans - 1 - right;
		printf("Case #%lld: %lld %lld\n", i + 1, left, right); 
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}