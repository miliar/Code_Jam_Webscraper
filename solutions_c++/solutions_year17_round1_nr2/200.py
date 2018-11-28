#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <string>
using namespace std;

const int inf = (int)1e7 + 10;
const int maxn = 55;
int R[maxn];
int Q[maxn][maxn];
int n, p;
pair<int, int> arr[maxn][maxn];
int at[maxn];

void solve(int testcase) {
	//printf("===\n");
	scanf("%d%d", &n, &p);
	for (int i = 1; i <= n; i ++)
		scanf("%d", &R[i]);
	for (int i = 1; i <= n; i ++) {
		at[i] = 1;
		for (int j = 1; j <= p; j ++) {
			scanf("%d", &Q[i][j]);
			double l = Q[i][j] / (double)R[i] * 100 / 110.0;
			double r = Q[i][j] / (double)R[i] * 100 / 90.0;
			int intl = (int)(l - 1e-7) + 1;
			int intr = (int)(r + 1e-7);
			arr[i][j] = make_pair(intl, intr);
		}
		sort(arr[i] + 1, arr[i] + 1 + p);
		//for (int j  = 1; j <= p; j ++)
		//	printf("(%d,%d) ", arr[i][j].first, arr[i][j].second);
		//printf("\n");
	}
	int ans = 0;
	while (true) {
		bool end = false;
		for (int i = 1; i <= n; i ++)
			if (at[i] > p) end = true;
		if (end) {
			break;
		}
		int maxl = -inf;
		int minr = inf;
		for (int i = 1; i <= n; i ++) {
			maxl = max(maxl, arr[i][at[i]].first);
			minr = min(minr, arr[i][at[i]].second);
		}
		if (maxl <= minr) {
			ans ++;
			for (int i = 1; i <= n ;i ++) {
				at[i] ++;
			}
			continue;
		} else {
			for (int i = 1; i <= n; i ++) 
				if (arr[i][at[i]].second == minr) {
					at[i] ++;
					break;
				}
		}
	}
	printf("Case #%d: %d\n", testcase, ans);
}

int main() {
	int tst;
	scanf("%d", &tst);
	for (int t = 1; t <= tst; t ++) {
		solve(t);
	}
	return 0;
}
