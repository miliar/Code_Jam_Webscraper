#include <bits/stdc++.h>

#define ll long long
#define pii pair<ll,ll>
#define fi first
#define se second

using namespace std;

int t;
ll n,h,k;
map<ll,ll> que;

int main() {
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%lld %lld", &n, &k);

		que.clear();
		que[-n] = 1;
		while (!que.empty()) {
			h = -que.begin()->fi;
			ll size = que.begin()->se;
			que.erase(que.begin());

			k -= size;
			if (k <= 0 || h == 0)
				break;

			if (h == 1) que[0] += size;
			else if (h == 2) que[-1] += size;
			else if (h % 2LL) que[-h/2LL] += 2LL * size;
			else que[-h/2LL] += size, que[-h/2LL+1LL] += size;
		}

		printf("Case #%d: %lld %lld\n", tc, h/2, h/2 + (h % 2 == 0 ? -1 : 0));
	}

	return 0;
}