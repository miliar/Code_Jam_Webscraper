#include <bits/stdc++.h>

using namespace std;

#define PI 3.14159265358979323846
#define F first
#define S second
const int MAX = 1001;

int n, k;
pair<int, int> arr[MAX];

double dp[MAX][MAX][2];

double compute(int x, int no, int last) {
	if (x == n) {
		if (no == k)
			return 0.0;
		return -1.0;
	}
	if (dp[x][no][last] != 0.0)
		return dp[x][no][last];
	if (no == k)
		dp[x][no][last] = compute(x + 1, no, last);
	else if (last == 0)
		dp[x][no][last] = max(compute(x + 1, no, last), PI * arr[x].F * arr[x].F + 2 * PI * arr[x].F * arr[x].S +  compute(x + 1, no + 1, 1));
	else dp[x][no][last] = max(compute(x + 1, no, last), 2 * PI * arr[x].F * arr[x].S  + compute(x + 1, no + 1, 1));
	return dp[x][no][last];
}


int main () {
	int test, cnt = 0;
	scanf("%d", &test);
	while (test--) {
		cnt++;
		printf("Case #%d: ", cnt);

		memset(dp, 0, sizeof dp);
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; i++)
			scanf("%d %d", &arr[i].F, &arr[i].S);
		sort(arr, arr + n);
		reverse(arr, arr + n);
		printf("%.8f\n", compute(0, 0, 0));
	}
	return 0;
}