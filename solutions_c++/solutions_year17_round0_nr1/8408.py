
// ~/BAU/ACM-ICPC/Teams/A++/BlackBurn95
// ~/sudo apt-get Accpeted

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <memory.h>
#include <limits.h>
#include <math.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <assert.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int N = 1000;
int n, k, vc = 0;
char s[N + 1];
int vis[N + 1];
unordered_set<string> v;

bool check() {
	for (int i = 0; i < n; i++)
		if (s[i] == '-')
			return 0;
	return 1;
}

int calc() {
	if (check())
		return 0;

	int ans = 1e9;

	for (int i = 0; i <= n - k; i++) {
		if (vis[i] != vc) {
			vis[i] = vc;
			for (int j = 0; j < k; j++) {
				if (s[i + j] == '-') s[i + j] = '+';
				else s[i + j] = '-';
			}

			string t = string(s);
			if (v.find(t) == v.end()) {
				v.insert(t);
				ans = min(ans, calc() + 1);
				v.erase(v.find(t));
			}
			vis[i] = 0;
			for (int j = 0; j < k; j++) {
				if (s[i + j] == '-') s[i + j] = '+';
				else s[i + j] = '-';
			}
		}
	}

	return ans;
}

int main() {
	std::ios::sync_with_stdio(false);

#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	
	int tc;
	scanf("%d", &tc);
	for(int c=1; c<=tc; c++) {
		scanf("%s%d", s, &k);
		n = strlen(s);
		
		int ans = 0,cc;
		for (int i = 0; i <= n-k; i++) {
			cc = 0;
			for (int j = 0; j < k; j++) {
				if (s[i + j] == '-') cc++;
				else break;
			}
			
			if (cc > 0) {
				for (int j = 0; j < k; j++)
					s[i + j] = (s[i + j] == '+' ? '-' : '+');
				ans++;
			}
		}

		if (!check()) printf("Case #%d: IMPOSSIBLE\n", c);
		else printf("Case #%d: %d\n", c, ans);
	}
	return 0;
}