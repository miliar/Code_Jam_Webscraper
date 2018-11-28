#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

const int N = 205;

struct Interval {
	int l, r;
	int c;

	bool operator <(const Interval &that) const {
		return l < that.l;
	}
} a[N];
int cnt[2];
vector<int> b[2];
int n, m;

int main() {
	int testCases;
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		cnt[0] = cnt[1] = 0;
		b[0].clear();
		b[1].clear();

		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", &a[i].l, &a[i].r);
			a[i].c = 0;
			cnt[0] += a[i].r - a[i].l;
		}
		for (int i = n; i < n + m; ++i) {
			scanf("%d%d", &a[i].l, &a[i].r);
			a[i].c = 1;
			cnt[1] += a[i].r - a[i].l;
		}
		n += m;

		int ret = 0;
		sort(a, a + n);
		int flex = 0;
		for (int i = 0; i < n; ++i) {
			int j = (i + 1) % n;
			int t = (a[j].l - a[i].r + 1440) % 1440;
			if (a[i].c == a[j].c) {
				b[a[i].c].push_back(t);
				cnt[a[i].c] += t;
			} else {
				flex += t;
				++ret;
			}
		}
		/*
		for (int i = 0; i < (int)b[0].size(); ++i) {
			cerr << b[0][i] << endl;
		}
		*/
		int delta = abs(cnt[0] - cnt[1]);
		if (flex < delta) {
			delta -= flex;
			int i;
			if (cnt[0] > cnt[1]) {
				i = 0;
			} else {
				i = 1;
			}
			vector<int> &bRef = b[i];
			sort(bRef.begin(), bRef.end());
			while (delta > 0) {
				int tmp = bRef.back();
				bRef.pop_back();
				ret += 2;
				delta -= tmp * 2;
			}
		}

		printf("Case #%d: %d\n", _, ret);
	}
	return 0;
}
