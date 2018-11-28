#include <cstdio>
#include <algorithm>
#include <map>

#define INF (1ll << 62)

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;

map<ll, ll> M;

int main(void)
{
	int T;
	scanf("%d", &T);
	for (int _c = 0; _c < T; _c ++) {
		ll N, K;
		M.clear();
		scanf("%lld%lld", &N, &K);
		pll ans;// = pll(0, 0);
		M[-N] = 1;
		while (K > 0) {
			auto it = M.upper_bound(-INF);
			ll now_n = -it->first;
			ll num = it->second;
			M.erase(it);
			ll a, b;
			K -= num;
			if (now_n & 1) {
				a = now_n >> 1;
				b = a;
			} else {
				a = now_n >> 1;
				b = a - 1;
			}
			M[-a] += num;
			M[-b] += num;
			ans = pll(a, b);
			//puts("!");
		}
		printf("Case #%d: %lld %lld\n", _c + 1, ans.first, ans.second);
	}
	return 0;
}