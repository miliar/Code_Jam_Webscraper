#include <bits/stdc++.h>
using namespace std;
int main() {
	int T, zzz = 0;
	scanf("%d", &T);
	while (T --) {
		long long n, m;
		scanf("%I64d%I64d", &n, &m);
		map<long long, long long> cnt;
		cnt[n] = 1;
		long long ans = n;
		while (m > 0) {
			long long tmp = (-- cnt.end()) -> second;
			m -= tmp;
			ans = (-- cnt.end()) -> first;
			cnt.erase(-- cnt.end());
			cnt[(ans - 1) / 2] += tmp;
			cnt[ans - 1 - (ans - 1) / 2] += tmp;
		}
		printf("Case #%d: %I64d %I64d\n", ++ zzz, ans - 1 - (ans - 1) / 2, (ans - 1) / 2);
	}
}

