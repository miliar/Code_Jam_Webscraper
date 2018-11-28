#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef pair<int, int> ii;

ll arr[1005];
vector<ll> v;

int main() {
	freopen("/Users/vlwk/Documents/Victor Folder/repo/C++/GCJ 2017/Qualification/C-small-2-attempt0.in", "r", stdin);
	freopen("/Users/vlwk/Documents/Victor Folder/repo/C++/GCJ 2017/Qualification/C.out", "w", stdout);
	ll T;
	scanf("%lld", &T);
	ll N, K, y, z;
	for (ll i = 1; i <= T; i++) {
		printf("Case #%lld: ", i);
		scanf("%lld%lld", &N, &K);
		ll tmp = (1 << ((ll)log2(K) + 1));
		ll N2 = N - K - (tmp / 2);
		if (N2 < 0) y = 0;
		else y = N2 / tmp + 1;
		printf("%lld ", y);
		N2 = N - K - tmp;
		if (N2 < 0) z = 0;
		else z = N2 / tmp + 1;
		printf("%lld\n", z);
	}
}