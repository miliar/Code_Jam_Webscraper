#include <queue>
#include <iostream>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>

long long T, n, k;
std::priority_queue<long long> queue;
std::map<long long, long long> map;
std::set<long long> set;

void add(long long x, long long value) {
	if (set.count(x) == 0) {
		queue.push(x);
		set.insert(x);
	}
	map[x] += value;
}

int main() {
	freopen("C.in", "r", stdin);
	scanf("%lld", &T);
	for (long long cs = 1; cs <= T; cs++) {
		while (!queue.empty()) queue.pop();
		map.clear();
		set.clear();
		scanf("%lld%lld", &n, &k);
		add(n, 1);
		while (!queue.empty()) {
			long long now = queue.top();
			queue.pop();
			if (now & 1) {
				if (now / 2 >= 1) {
					add(now / 2, map[now]);
					add(now / 2, map[now]);
				}
			} else {
				if (now / 2 >= 1) {
					add(now / 2, map[now]);
				}
				if (now / 2 >= 2) {
					add(now / 2 - 1, map[now]);
				}
			}
		}
		bool flag = false;
		for (std::map<long long, long long>::reverse_iterator it = map.rbegin(); it != map.rend(); it++) {
			std::cerr << it -> first << " " << it -> second << std::endl;
			if (k > it -> second) k -= it -> second;
			else{
				flag = true;
				printf("Case #%lld: %lld %lld\n", cs, it -> first >> 1, it -> first - 1 >> 1);
				break;
			}
		}
		assert(flag);
	}
}
