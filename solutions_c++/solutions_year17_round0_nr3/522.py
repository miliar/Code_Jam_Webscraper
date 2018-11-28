#include <stdio.h>
#include <map>

int main() {
	int T;
	scanf("%d", &T);
	
	for (int t = 0; t < T; t++) {
		std::map<long long, long long> map;
		long long n, k;
		scanf("%I64d %I64d", &n, &k);

		long long count = 0;
		map[n - 1] = 1;
		while (true) {
			long long space, amt;
			space = map.rbegin()->first;
			amt = map.rbegin()->second;
			map.erase(space);

			count += amt;
			if (count >= k) {
				printf("Case #%d: %I64d %I64d\n", t + 1,
					space / 2 + space % 2,
					space / 2);
				break;
			}

			long long nextSpace = space / 2 + space % 2 - 1;
			long long nextAmount = amt;
			int odd = space % 2 == 1;
			if (!odd) {
				nextAmount *= 2;
			}
			for (int side = 0; (side < 2 && odd) || (side < 1); side++) {
				if (nextSpace >= 0) {
					map[nextSpace] += nextAmount;
				}
				nextSpace = space / 2 - 1;
			}
		}
	}

	return 0;
}
