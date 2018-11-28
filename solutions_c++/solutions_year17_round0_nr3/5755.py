#include <bits/stdc++.h>

using namespace std;

int t, n, k, h;

int main() {
	ios_base::sync_with_stdio(false);
	cin >> t;
	while (t--) {
		priority_queue <int> pq;
		cin >> n >> k;
		pq.push(n);
		cout << "Case #" << ++h << ": ";
		while (k > 1) {
			int p = pq.top() - 1;
			pq.pop();
			pq.push(p / 2), pq.push(p - p / 2), k--;
		}
		int p = pq.top() - 1;
		cout << p - p / 2 << " " << p / 2 << endl;
	}
	return 0;
}
