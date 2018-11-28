#include <bits/stdc++.h>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		int n, k;
		cin >> n >> k;
		priority_queue<int> q;
		q.push(n);
		for (int i = 0; i < k; ++i) {
			auto to = q.top();
			--to;
			int now = to / 2;
			q.push(now);
			q.push(to - now);
			if (i == k - 1) {
				cout << to - now << " " << now << "\n";
			}
			q.pop();
		}
	}
	return 0;
}