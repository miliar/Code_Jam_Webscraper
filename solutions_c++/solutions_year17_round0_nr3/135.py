#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <functional>
using namespace std;

void proc(int caseidx) {
	long long n, k;
	scanf("%lld %lld", &n, &k);
	--k;

	printf("Case #%d: ", caseidx);
	vector<pair<long long, long long>> cur{ { n, 1 } };
	long long now = 0;
	while (true) {
		map<long long, long long, greater<long long>> nxt;
		for (const auto& pair : cur) {
			if (now <= k && k < now + pair.second) {
				printf("%lld %lld\n", pair.first / 2, (pair.first - 1) / 2);
				return;
			}
			nxt[(pair.first - 1) / 2];
			nxt[(pair.first - 1) / 2] += pair.second;
			nxt[pair.first / 2];
			nxt[pair.first / 2] += pair.second;
			now += pair.second;
		}

		cur.clear();
		for (const auto& pair : nxt) {
			cur.push_back(pair);
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		proc(i);
	}
	return 0;
}