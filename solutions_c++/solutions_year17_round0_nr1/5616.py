#include <bits/stdc++.h>

using namespace std;

string s;
int n, k;
vector<int> d;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		cin >> s;
		n = s.length();
		cin >> k;
		d.assign(n+1, 0);
		bool notFound = false;
		int res = 0;
		for (int i = 0; i < n; ++i) {
			int v = (s[i] == '+') ? 0 : 1;
			if (i > 0) d[i] += d[i-1];
			if ((v+d[i])&1) {
				if (i >= n-k+1) notFound = true;
				else {
					++res;
					++d[i];
					--d[i+k];
				}
			}
		}
		printf("Case #%d: ", test);
		if (notFound) puts("IMPOSSIBLE");
		else printf("%d\n", res);
	}
	return 0;
}