#include<bits/stdc++.h>
using namespace std;
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		long long n, k;
		cin >> n >> k;
		map<long long, long long> mp;
		mp[n] = 1;
		while(k) {
			auto itr(mp.rbegin());
			if(itr->second >= k) {
				printf("Case #%d: %I64d %I64d\n", qq, itr->first / 2, (itr->first - 1) / 2);
				break;
			}else {
				mp[itr->first / 2] += itr->second;
				mp[(itr->first - 1) / 2] += itr->second;
				k -= itr->second;
				mp.erase(itr->first);
			}
		}
	}
}
