#include<cstdio>
#include<map>
int main() {
	int tcn;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++) {
		long long int n, k;
		scanf("%lld %lld", &n, &k);
		std::map<long long int, long long int> mp;
		mp[n] = 1;
		long long int l, r;
		while (1) {
			auto it = mp.end();
			it--;
			long long int sz = it->first;
			long long int val = it->second;
			mp.erase(sz);
			l = sz / 2;
			r = (sz - 1) / 2;
			k -= val;
			if (k <= 0) {
				break;
			}
			mp[l] += val;
			mp[r] += val;
		}
		printf("Case #%d: %lld %lld\n", tc, l, r);
	}
	return 0;
}