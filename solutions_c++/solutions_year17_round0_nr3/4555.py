#include <bits/stdc++.h>

#define rep(i, n) for(int i = 0; i < n; i ++)
typedef long long LL;

const int N = 1e6 + 5;
LL count[N];

int main() {
	int T;
	LL K, n;
	scanf("%d", &T);
	rep(cas, T) {
		std::cin >> n >> K;
		LL max_dist = 0, min_dist = 0;
		memset(count, 0, sizeof count);
		count[n] = 1;
		for (int j = n; j > 0; j --) {
			K -= count[j];
			count[j >> 1] += count[j];
			count[j - 1 >> 1] += count[j];
			if (K <= 0) {
				max_dist = j >> 1;
				min_dist = j - 1 >> 1;
				break;
			}
		}
		printf("Case #%d: %lld %lld\n", cas + 1, max_dist, min_dist);
	}
	return 0;
}
