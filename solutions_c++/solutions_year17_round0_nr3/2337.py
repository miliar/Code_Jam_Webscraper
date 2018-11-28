#include <cstdio>
#include <map>
#include <cassert>

void solveOne(int iTest) {
	long long n, k;
	scanf("%lld %lld", &n, &k);
	std::map<long long, long long> count;
	count[n] = 1;
	long long done = 0;
	while (true) {
		assert(!count.empty());
		auto it = count.rbegin();
		long long key = it->first;
		long long amount = it->second;
		if (done + amount >= k) {
			printf("Case #%d: %lld %lld\n", iTest, key / 2, (key - 1) / 2);
			return;
		}
		count.erase(key);
		done += amount;
		count[(key - 1) / 2] += amount;
		count[key / 2] += amount;
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		solveOne(i);
	}
	return 0;
}
