#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
#include <iostream>
#include "C.h"
using namespace std;
using namespace C;
namespace C {
	int64_t n, k;
	void input() {
		//scanf("%d%d", &n, &k);
		std::cin >> n >> k;
	}
	void solve() {
		map<int64_t, int64_t> mp;
		mp[n] = 1;
		k--;
		while (k > 0) {
			auto rit = mp.end();
			rit--;
			int64_t band = rit->first;
			int64_t m = rit->second;
			if (m <= k) 
				mp.erase(rit);
			int64_t p = std::min(m, k);
			k -= p;
			if (band % 2 == 1) {
				mp[band / 2] += 2*p;
			} else {
				mp[band / 2] += p;
				mp[band / 2-1] += p;
			}
		}
		{
			auto rit = mp.end(); rit--;
			int64_t band = rit->first;
			//printf("band %lld\n", band);
			if (band % 2 == 1) {
				printf("%lld %lld\n", band/2, band/2);
			} else {
				printf("%lld %lld\n", band/2, band/2-1);
			}
		}
	}

	void main() {
		int zz;
		scanf("%d", &zz);
		for (int kase = 1; kase <= zz; kase++) {
			input();
			printf("Case #%d: ", kase);
			solve();
		}
	}
}
// 15 1000000000000000