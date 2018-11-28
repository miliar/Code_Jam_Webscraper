#include<stdio.h>
#include<string.h>
#include<map>

using namespace std;

map<unsigned long long, unsigned long long> tab;

inline void
Insert(const unsigned long long& key, const unsigned long long& num)
{
	if (key == 0) {
		return;
	}
	auto itr = tab.find(key);
	if (itr != tab.end()) {
		itr->second += num;
	} else {
		tab.insert(make_pair(key, num));
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		unsigned long long N, K;
		scanf("%lld %lld", &N, &K);
		tab.clear();
		tab.insert(make_pair(N, 1));
		unsigned long long cnt = 0;
		unsigned long long cur = N;
		while (true) {
			auto itr = tab.rbegin();
			cur = itr->first;
			unsigned long long num = itr->second;
			cnt += num;
			if (cnt >= K) {
				break;
			}
			tab.erase(cur);
			if (cur % 2 == 0) {
				Insert(cur / 2, num);
				Insert(cur / 2 - 1, num);
			} else {
				Insert(cur / 2, num * 2);
			}
		}

		printf("Case #%d: %lld %lld\n", t, cur / 2, (cur - 1) / 2);
	}
	return 0;
}