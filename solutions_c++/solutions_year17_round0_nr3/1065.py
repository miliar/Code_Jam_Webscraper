#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

map<LL, LL> mll;

int main() {
	int T; scanf("%d", &T);
	for (int kk = 1; kk <= T; kk++) {
		mll.clear();
		priority_queue<LL> q;
		LL n, k; scanf("%lld%lld", &n, &k);
		q.push(n); mll[n] = 1;
		while (k > 0) {
			LL u = q.top(); q.pop();
			LL num = mll[u];
			mll[u] = 0;
			u--;
			k -= num;
			if (k <= 0) {
				printf("Case #%d: %lld %lld\n", kk, u - (u >> 1), u >> 1);
			} else {
				if ((u & 1LL) == 0) {
					u >>= 1LL;
					if (mll[u] == 0) q.push(u);
					mll[u] += (num << 1LL);
				} else {
					u >>= 1LL;
					if (mll[u] == 0) q.push(u);
					if (mll[u + 1] == 0) q.push(u + 1);
					mll[u] += num;
					mll[u+1] += num;
				}
			}
		}
	}
	return 0;
}