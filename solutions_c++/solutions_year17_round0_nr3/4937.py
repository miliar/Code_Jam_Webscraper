#include <cstdio>
#include <vector>
#include <set>
#include <utility>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;
typedef pair<int, ii> iii;

void print(vector<int> &v) {
	for (auto e : v) if (e) printf("%2d ", e); else printf("   "); printf("\n");
}

pair<int, int> solver(int n, int k) {
	set<iii> s;
	s.insert({0, {-n, 1}});

	int ls = 0;
	int rs = 0;

	// For each person who is about to enter the bathroom.
	for (int i = 0; i < k; i++) {
		int lvl = s.begin()->first;
		int sz = -s.begin()->second.first;
		int l = s.begin()->second.second;
		int r = sz + l - 1;
		s.erase(*s.begin());

		// printf("(%d, %d, %d, %d)\n", lvl, sz, l, r);

		int m = (l + r) / 2;
		ls = (m - l);
		rs = (r - m);

		int l1 = l;
		int r1 = m - 1;

		if (l1 <= r1) {
			s.insert({lvl + 1, {-(r1 - l1 + 1), l1}});
			// printf("   (%d, %d)\n", l1, r1);
		}

		int l2 = m + 1;
		int r2 = r;
		if (l2 <= r2) {
			s.insert({lvl + 1, {-(r2 - l2 + 1), l2}});
			// printf("   (%d, %d)\n", l2, r2);
		}
	}

	return {max(ls, rs), min(ls, rs)};
}

int main(void) {
	int t;
	scanf("%d", &t);

	// For each test case.
	for (int tc = 1; tc <= t; tc++) {
		int n, k;
		scanf("%d %d", &n, &k);
		pair<int, int> output = solver(n, k);

		printf("Case #%d: %d %d\n", tc, output.first, output.second);
	}

	return 0;
}