#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <string>
#include <map>

using namespace std;

using ll = long long;

/*
char buff[10000];

void solve() {
	int size;
	scanf("%s %d", buff, &size);
	int ans = 0;
	int len = strlen(buff);
	for (int i = 0; i < len; ++i) {
		if (buff[i] == '+') {
			continue;
		}
		if (i + size > len) {
			printf("IMPOSSIBLE\n");
			return;
		}
		ans += 1;
		for (int j = 0; j < size; ++j) {
			int pos = i + j;
			if (buff[pos] == '-') {
				buff[pos] = '+';
			} else {
				buff[pos] = '-';
			}
		}
	}
	printf("%d\n", ans);
}*/

/*
string solve() {
	char n[20];
	scanf("%s", &n);
	int len = strlen(n);
	if (len == 1) {
		return n;
	}
	int pos = 0;
	for (int i = 1; i < len; ++i) {
		if (n[i] > n[i - 1]) {
			pos = i;
		}
		if (n[i] < n[i - 1]) {
			--n[pos];
			for (int j = pos + 1; j < len; ++j) {
				n[j] = '9';
			}
			if (n[0] == '0') {
				return n + 1;
			} else {
				return n;
			}
		}
	}
	return n;
}*/

void solve() {
	ll N, K;
	scanf("%lld%lld", &N, &K);
	map<ll, ll> slots;
	slots[N] = 1;
	ll l, r;
	while (K > 0) {
		auto it = slots.end();
		--it;
		ll size = it->first;
		ll cnt = it->second;
		slots.erase(it);
		l = (size - 1) / 2;
		r = size / 2;
		K -= cnt;
		slots[l] += cnt;
		slots[r] += cnt;
	}
	printf("%lld %lld\n", r, l);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		fprintf(stderr, "%d\n", i + 1);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}