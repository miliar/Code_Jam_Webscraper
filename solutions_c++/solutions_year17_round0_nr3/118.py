#include <cstdio>
#include <set>

typedef long long ll;

ll total, k;

struct state {
	ll n;
	mutable ll count;

	bool operator < (const state &t) const {
		return n < t.n;
	}
};

void insertToSet(std::set < state > &set, ll n, ll count) {
	auto it = set.find(state {n, 0});
	if (it != set.end()) {
		it->count += count;
	} else {
		set.insert(state { n, count });
	}
}

void solve() {
	state start = { total, 1 };

	std::set < state > set;
	set.insert(start);

	while (k) {
		auto it = --set.end();
		if (it->count >= k) {
			printf("%lld %lld\n", it->n/2, (it->n-1)/2);
			return;
		} else {
			k -= it->count;
			insertToSet(set, it->n/2, it->count);
			insertToSet(set, (it->n-1)/2, it->count);
			set.erase(it);
		}
	}
}

int main() {
	freopen("output.txt", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for (int nowCase = 1; nowCase <= numCase; nowCase++) {
		scanf("%lld%lld", &total, &k);

		printf("Case #%d: ", nowCase);
		solve();
	}

	return 0;
}