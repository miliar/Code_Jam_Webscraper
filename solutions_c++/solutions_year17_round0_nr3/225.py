#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;

int t;
int64_t n, k;

int main()
{
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		scanf("%lld%lld", &n, &k);
		map<int64_t,int64_t> m;
		m.emplace(n, 1);
		int64_t left = k - 1;
		while (left > 0) {
			auto it = prev(m.end());
			//printf("got %lld %lld\n", it->first, it->second);
			int64_t step = min(it->second, left);
			int64_t ls = it->first / 2;
			int64_t rs = (it->first - 1) / 2;
			if (it->second > step) {
				it->second -= step;
				//printf("m[%lld] = %lld\n", it->first, it->second);
			} else {
				m.erase(it);
				//printf("erase m[%lld]\n", it->first);
			}
			m[ls] += step;
			//printf("m[%lld] = %lld\n", ls, m[ls]);
			m[rs] += step;
			//printf("m[%lld] = %lld\n", rs, m[rs]);
			left -= step;
		}
		auto it = m.rbegin();
		//printf("got %lld %lld\n", it->first, it->second);
		printf("Case #%d: %lld %lld\n", ti+1, it->first / 2, (it->first - 1) / 2);
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
