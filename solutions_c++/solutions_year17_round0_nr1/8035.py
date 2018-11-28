#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

int n, m, i, j, T, ti, ans, l;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);
	for (ti = 1; ti <= T; ++ti) {
		string s;
		ans = 0;
		cin >> s >> n;
		bool b[1002];
		l = s.length();
		for (i = 0; i < l; ++i) 
			if (s[i] == '+') b[i] = true;
				else b[i] = false;
		for (i = 0; i <= l - n; ++i) 
			if (!b[i]) {
				for (j = 0; j < n; ++j) 
					b[i + j] = !(b[i + j]);
				ans++;
			}
		bool flag = false;
		for (i = l - n + 1; i < l; ++i) 
			if (!b[i]) flag = true;
		if (flag) {
			printf("Case #%d: IMPOSSIBLE\n", ti);
			continue;
		}
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}