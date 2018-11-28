#include <iostream>
#include <stdio.h>
#include <string>
#include <memory.h>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <time.h>
#include <assert.h>
#include <cmath>
#include <stack>
#include <string.h>
#include <sstream>
#include <algorithm>
using namespace std;
typedef long long ll;
const int N = 100;
int A, B;
pair<int, int> a[N], b[N];
int dp[721][721][2][2];
int canA[24 * 60 + 1];
int canB[24 * 60 + 1];
int calc(int a, int b, bool who, bool last) {
	if (a > 720 || b>720)
		return 1e9;
	if (a + b == 24 * 60)
		return last != who;
	int &ret = dp[a][b][who][last];
	if (ret != -1)
		return ret;
	ret = 1e9;
	int i = a + b;
	if (canA[i])
		ret = min(ret, calc(a + 1, b, who, 0) + last);
	if (canB[i])
		ret = min(ret, calc(a, b + 1, who, 1) + !last);
	return ret;
}
int main()
{
	//freopen("src.txt", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/B-large.in", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T) {
		printf("Case #%d:", T);
		scanf("%d%d", &A, &B);
		memset(canA, 1, sizeof(canA));
		memset(canB, 1, sizeof(canB));
		for (int i = 0; i < A; ++i) {
			scanf("%d%d", &a[i].first, &a[i].second);
			for (int j = a[i].first; j < a[i].second; ++j)
				canA[j] = false;
		}
		for (int i = 0; i < B; ++i) {
			scanf("%d%d", &a[i].first, &a[i].second);
			for (int j = a[i].first; j < a[i].second; ++j)
				canB[j] = false;
		}
		memset(dp, -1, sizeof(dp));
		int res = 1e9;
		if (canA[0])
			res = min(res, calc(1, 0, 0, 0));
		if (canB[0])
			res = min(res, calc(0, 1, 1, 1));
		printf(" %d\n", res);
	}
	return 0;
}