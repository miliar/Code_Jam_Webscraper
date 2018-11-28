#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
using namespace std;
typedef long long ll;
priority_queue<int> q;

int main() {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-ans.out", "w", stdout);
	int T, ca = 1; scanf("%d", &T);
	while (T--) {
		int n, k; scanf("%d%d", &n, &k);
		while (!q.empty()) q.pop();
		q.push(n);
		printf("Case #%d: ", ca++);
		rep(i, k) {
			int x = q.top(); q.pop();
			int y = x / 2, z = x - y - 1;
			if (y > 0) q.push(y);
			if (z > 0) q.push(z);
			if (i == k - 1) {
				printf("%d %d\n", max(y, z), min(y, z));
			}
		}
	}
	return 0;
}

