/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

string s[3] = {"R", "Y", "B"};
int c[3];

string get_ans(string ret, int n) {
	int i, j;
	for (i = 1; i < n; i++) {
		int l = -1;
		for (j = 0; j < 3; j++) {
			if (s[j][0] == ret.back() || !c[j]) continue;
			if (l == -1) l = j;
			else if (c[l] < c[j]) l = j;
		}
		if (l == -1) return "";
		ret += s[l];
		--c[l];
	}

	if (ret.back() == ret[0]) return "";

	return ret;
}

//this is a solution for the small cases only.
int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, K = 1;
	scanf("%d", &T);
	while (T--) {
		int n, x, i, k;
		scanf("%d", &n);
		for (i = 0; i < 3; i++) {
			scanf("%d %d", c + i, &x);
		}

		for (i = 0; i < 3; i++) {
			if (!c[i]) continue;
			int color[3];
			for (k = 0; k < 3; k++) color[k] = c[k];

			--c[i];
			string res = get_ans(s[i], n);
			if (res != "") {
				printf("Case #%d: %s\n", K, res.c_str());
				goto NXT;
			}

			for (k = 0; k < 3; k++) c[k] = color[k];
		}

		printf("Case #%d: IMPOSSIBLE\n", K);

		NXT:;
		K++;
	}
	return 0;
}
