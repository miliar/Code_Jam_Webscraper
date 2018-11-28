#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <omp.h>
#include <unordered_map>
using namespace std;

const int mn = 101, mS = (1 << 24) + 5, mp = 4;
char f[mS];
int a[mn];
int n, p;

unordered_map<int, int> cache;

inline int tonum(int *st) {
	int ret = 0;
	for (int i = 1; i < p; ++i)
		ret = (ret << 8) | st[i];
	return ret;
}

int calc(int *st, int cur) {
	int v = tonum(st);
	if (!v) {
		if (cur == 0) return 0;
		else return -1;
	}
	v = (v << 8) | cur;
	auto itr = cache.find(v);
	if (itr != cache.end())
		return itr->second;

	int ret = -1;
	for (int i = 1; i < p; ++i) {
		if (st[i] > 0) {
			--st[i];
			int tmp = calc(st, (cur + p - i) % p);
			if (tmp < 0) {
				++st[i];
				continue;
			}
			if ((cur + p - i) % p == 0)
				++tmp;
			if (ret == -1 || tmp > ret)
				ret = tmp;
			++st[i];
		}
	}

	return cache[v] = ret;
}
int main() {
	int Tn;
	scanf("%d", &Tn);

	for (int Tc = 1; Tc <= Tn; ++Tc) {
		scanf("%d%d", &n, &p);

		int st[mp] = { };
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", a + i);
			a[i] %= p;
			st[a[i]]++;
			if (a[i] == 0)
				ans++;
		}
//		memset(f, -1, sizeof(f));

//		cout << ans << endl;
		cache.clear();
		int tmax = 0;
		for (int i = 0; i < p; ++i) {
			tmax = max(tmax, calc(st, i));
//			printf("%d: %d\n", i, calc(st, i));
		}

		ans += tmax;

		printf("Case #%d: ", Tc);
		printf("%d\n", ans);
	}
	return 0;
}
