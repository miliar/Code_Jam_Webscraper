#include<map>
#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		static int id = 0;
		long long n, k;
		scanf("%lld%lld", &n, &k);
		map<long long, long long> space;
		space[n] = 1;
		long long ans = 0;
		while (true) {
			long long s = space.rbegin()->first,
				 	  cnt = space.rbegin()->second;
			space.erase(s);
			if (cnt >= k) {
				ans = s;
				break;
			} else {
				k -= cnt;
				if (s >= 1) {
					space[s / 2] += cnt;
				}
				if (s >= 2) {
					space[(s - 1) / 2] += cnt;
				}
			}
		}
		printf("Case #%d: %lld %lld\n", ++id, ans / 2, (ans - 1) / 2);	
	}
	return 0;
}
