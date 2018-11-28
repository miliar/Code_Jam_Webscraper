#include <bits/stdc++.h>

using namespace std;

int T;
int n;
int k;

struct pii {
	int len;
	int begini;
	friend int operator<(const pii &a, const pii &b) {
		if (a.len != b.len)
			return a.len > b.len;
		return a.begini < b.begini;
	}
};

set<pii> seta;

int main() {

	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		seta.clear();

		scanf("%d", &n);
		scanf("%d", &k);

		seta.insert( { n, 0 });

		int ans1, ans2;
		for (int i = 0; i < k; i++) {
			auto it = seta.begin();
			int nowlen = it->len;
			ans1 = (nowlen - 1) / 2;
			int newi = it->begini + ans1;
			pii tp1 = { ans1, it->begini };
			ans2 = ans1;
			if ((nowlen - 1) % 2)
				ans2++;
			pii tp2 = { ans2, newi + 1 };

			seta.erase(it);
			if (tp1.len)
				seta.insert(tp1);
			if (tp2.len)
				seta.insert(tp2);
		}
		printf("Case #%d: ", t);
		printf("%d %d\n", ans2, ans1);
	}
	return 0;
}
