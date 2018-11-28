#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>

using namespace std;

int s1, s2, v1 = -1, v2 = -1;

void f(int n, int &l, int &r) {
	l = r = (n >> 1);
	if (!(n % 2)&&r>0)
		r--;
}

void dfs(int n, int deph) {
	if (deph == 0) {
		int l, r;

		f(n, l, r);

		if (v1 == -1)
			v1 = l;
		if (v2 == -1 && v1 != r)
			v2 = r;

		if (v1 == l)
			s1++;
		if (l == r)
			s1++;
		if (v2 == r)
			s2++;

		//printf("%d %d ", l, r);

		return;
	}
	dfs(n >> 1, deph - 1);
	int tmp = n;
	if (!(n % 2))
		tmp--;
	dfs(tmp >> 1, deph - 1);
}

int main() {

	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);

	int t;

	cin >> t;
	int cnt = 0;
	while (t--) {
		cnt++;
		s1 = s2 = 0;
		v1 = v2 = -1;
		int n, k;

		scanf("%d %d", &n, &k);

		int l, r;
		if (k == 1) {
			f(n, l, r);
			printf("Case #%d: %d %d\n", cnt, l, r);
			continue;
		}


		int deph = log2(k);

		int sub = k - ((1 << deph) - 1);

		dfs(n, deph - 1);

		if (s1 >= sub)
			f(v1, l, r);
		else
			f(v2, l, r);

		printf("Case #%d: %d %d\n", cnt, l, r);
	}
	return 0;
}