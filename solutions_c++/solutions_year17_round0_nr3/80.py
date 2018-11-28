#include <bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)

int main() {
	int T; cin >> T;
	For(TK,1,T) {
		long long n, k; cin >> n >> k;
		map<long long, long long> Map;
		Map[n] = 1;
		int num_iter = 0;
		while (Map.size()) {
			++num_iter;
			auto it = --Map.end();
			long long len = it->first;
			long long num = it->second;
			Map.erase(it);
			if ((k -= num) <= 0) {
				printf("Case #%d: %lld %lld\n", TK, len / 2, (len - 1) / 2);
				break ;
			}
			if (!len) break ;
			Map[(len - 1) / 2] += num;
			Map[len / 2] += num;
		}
	}
	return 0;
}