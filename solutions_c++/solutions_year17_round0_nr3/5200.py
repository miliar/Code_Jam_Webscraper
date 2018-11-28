#include <bits/stdc++.h>
using namespace std;
int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, counter1 = 1;
	cin >> t;
	while (t--) {
		long long n, k, mn = 0, mx = 0, h = 0;
		cin >> n >> k;
		queue<long long> q;
		map<long long, long long> counter;
		q.push(n), counter[n]++;
		while (!q.empty() && h < k) {
			h += counter[q.front()];
			long long mid = ceil(q.front() / 2.0) - 1;
			if (max(mid, q.front() - mid - 1) > 0
					&& !counter[max(mid, q.front() - mid - 1)]) {
				q.push(max(mid, q.front() - mid - 1));
			}
			counter[max(mid, q.front() - mid - 1)] += counter[q.front()];
			if (min(mid, q.front() - mid - 1) > 0
					&& !counter[min(mid, q.front() - mid - 1)]) {
				q.push(min(mid, q.front() - mid - 1));
			}
			counter[min(mid, q.front() - mid - 1)] += counter[q.front()];
			if (h >= k) {
				mn = min(mid, q.front() - mid - 1);
				mx = max(mid, q.front() - mid - 1);
			}
			counter[q.front()] = 0;
			q.pop();
		}
		cout << "Case #" << counter1 << ": " << mx << " " << mn << endl;
		counter1++;
	}
}
