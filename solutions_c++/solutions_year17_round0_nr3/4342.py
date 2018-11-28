#include "stdc++.h"
using namespace std;

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++) {
		long long n, k;
		cin >> n >> k;
		priority_queue<long long> q;
		q.push(n+2);
		long long l1, l2;
		for (int j = 0; j < k; j++) {
			long long top = q.top();
			q.pop();
			if (top%2 == 0) {
				if (top > 2) {
					q.push(top/2 + 1);
					q.push(top/2);
				}
				l1 = (top/2) - 1;
				l2 = (top/2 - 1) - 1;
			} else {
				if (top > 3) {
					q.push(top/2 + 1);
					q.push(top/2 + 1);
				}
				l1 = (top/2) - 1;
				l2 = (top/2) - 1;
			}
		}
		cout << "Case #" << i+1 << ": " << l1 << " " << l2 << endl;
	}
	return 0;
}