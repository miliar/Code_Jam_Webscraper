#include <cstdio>
#include <map>

using namespace std;

long long n, k;
long long ans0, ans1;
map<long long, long long> c;

int main() {
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		c.clear();
		scanf("%lld%lld", &n, &k);
		c[-n] = 1;
		long long last = -n - 1;
		while (k > 0) {
			auto it = c.upper_bound(last);
			long long num = it->second;
			last = it->first;
			ans0 = -last / 2;
			ans1 = (-last - 1) / 2;
			c[-ans0] += num;
			c[-ans1] += num;
			k -= num;
		}
		printf("Case #%d: %lld %lld\n", cas, ans0, ans1);
	}
	return 0;
}
