#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <cstring>
using namespace std;

int T, n, K, p[4], ans;

int main() {
	scanf("%d", &T);
	for (int it = 1; it <= T; it++) {
		scanf("%d %d", &n, &K);
		memset(p, 0, sizeof p);
		for (int i = 0; i < n; i++) {
			int x;
			scanf("%d", &x);
			p[x % K]++;
		}
		if (K == 2) {
			ans = p[0] + (p[1] + 1) / 2;
		} else if (K == 3) {
			int c = min(p[1], p[2]);
			ans = p[0] + c;
			p[1] -= c;
			p[2] -= c;
			if (p[1] > 0) {
				ans += p[1]/3;
				p[1] %= 3;
			}
			if (p[2] > 0) {
				ans += p[2]/3;
				p[2] %= 3;
			}
			if (p[1] || p[2]) {
				ans++;
			}
		} else {
			ans = p[0];
			ans += p[2]/2;
			p[2] %= 2;

			int c = min(p[1], p[3]);
			ans += c;
			p[1] -= c;
			p[3] -= c;

			if (p[1] > 0) {
				if (p[1] >= 2 && p[2] > 0) {
					ans++;
					p[1] -= 2;
					p[2]--;
				}
				ans += p[1]/4;
				p[1] %= 4;
			}

			if (p[3] > 0) {
				if (p[3] >= 2 && p[2] > 0) {
					ans++;
					p[3] -= 2;
					p[2]--;
				}
				ans += p[3]/4;
				p[3] %= 4;
			}

			if (p[1] || p[2] || p[3]) {
				ans++;
			}
		}
		printf("Case #%d: %d\n", it, ans);
	}
	return 0;
}