#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

#define IOS ios_base::sync_with_stdio(0);cin.tie(0);
#define MP make_pair
#define PB push_back
#define FF first
#define SS second

int main() {
	IOS;
	LL t, kase = 0;
	cin >> t;
	while (t--) {
		LL k, n;
		cin >> k >> n;
		if (k == n) {
			cout << "Case #" << ++kase << ": 0 0\n";
			continue;
		}
		priority_queue<LL> pq;
		pq.push(k);
		LL x, y;
		while (n--) {
			LL tmp = pq.top();
			pq.pop();
			tmp--;
			LL mid = tmp / 2;
			pq.push(y = mid);
			if (tmp % 2) pq.push(x = mid + 1);
			else pq.push(x = mid);
		}
		cout << "Case #" << ++kase << ": " << x << " " << y << "\n";
	}
}
