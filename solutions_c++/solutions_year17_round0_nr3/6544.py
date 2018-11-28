
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

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int N = 1000000;
int n, k;
int b[N + 2];
int pre[N + 2], last[N + 2];

int main() {
	std::ios::sync_with_stdio(false);

#ifdef LOCAL
	freopen("C-small-1-attempt2.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif

	int tc;
	scanf("%d", &tc);

	for (int cc = 1; cc <= tc; cc++) {
		scanf("%d%d", &n, &k);
		memset(b, 0, sizeof(b));
		b[0] = 1, b[n + 1] = 1;

		int ml = -1, mr = -1;
		for (int i = 0; i < k; i++) {
			pre[0] = 0;
			for (int i = 1; i <= n; i++) {
				pre[i] = pre[i - 1];
				if (b[i] == 1) pre[i] = i;
			}
			last[n + 1] = n + 1;
			for (int i = n; i >= 1; i--) {
				last[i] = last[i + 1];
				if (b[i] == 1) last[i] = i;
			}

			int mn = -1e9, mx = -1e9, at = -1;
			for (int i = 1; i <= n; i++) {
				if (b[i] == 0 && (min(i-pre[i]-1,last[i]-i-1)>mn || (min(i - pre[i] - 1, last[i] - i - 1)==mn && max(i - pre[i] - 1, last[i] - i - 1)>mx))) {
					mn = min(i - pre[i] - 1, last[i] - i - 1);
					mx = max(i - pre[i] - 1, last[i] - i - 1);
					at = i;
				}
			}

			b[at] = 1;
			ml = mn, mr = mx;
		}

		printf("Case #%d: %d %d\n", cc, mr, ml);

	}
	return 0;
}