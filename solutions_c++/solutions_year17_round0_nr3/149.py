#include <cstdio>
#include <map>
#include <utility>
#include <iostream>
using namespace std;

void addValue(map<long long, long long> &f, long long x, long long y) {
	if (f.count(x)) f[x] += y;
	else f[x] = y;
}

long long solve(long long N, long long K) {
	map<long long, long long> f;
	long long ans;
	f[N] = 1;
	while (K > 0) {
		pair<long long, long long> p = *(--f.end());
		f.erase(--f.end());
		addValue(f, p.first >> 1, p.second);
		addValue(f, (p.first - 1) >> 1, p.second);
		ans = p.first;
		K -= p.second;
	}
	return ans;
}

int main() {
	int T;
	long long N, K;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%lld%lld", &N, &K);
		long long x = solve(N, K);
		printf("Case #%d: %lld %lld\n", t, x >> 1, (x - 1) >> 1);
	}
	return 0;
}
