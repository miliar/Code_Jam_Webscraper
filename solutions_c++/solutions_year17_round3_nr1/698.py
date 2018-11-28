#include<stdio.h>
#include<algorithm>
#define PI 3.14159265358979323
#define Max(a,b) (a > b ? a : b)
using namespace std;
struct pan {
	int R, H;
	bool operator<(pan a) const{
		return a.R < R;
	}
};
pan P[1001];
long double dp[1001][1001];
long double ans;
int N, K;
long double solve(int x, int r) {

	if (K == r || x == N)
		return 0;
	if (dp[x][r])
		return dp[x][r];

	long double ret = 0;
	
	for (int i = x + 1; i  < N; i++) {
		ret = Max(ret, solve(i, r + 1));
	}
	if (r == 0)
		ret += (long double)P[x].R*P[x].R*PI;
	ret += (long double)2 * PI*P[x].R*P[x].H;
	return dp[x][r] = ret;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, test = 1;
	scanf("%d", &t);
	while (test <= t) {
		ans = 0;
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; i++)
			scanf("%d %d", &P[i].R, &P[i].H);
		for (int i = 0; i <= N; i++)
			for (int j = 0; j <= N; j++)
				dp[i][j] = 0;
		sort(P, P + N);
		for (int i = 0; i <= N - K; i++) {
			ans = Max(ans, solve(i, 0));
		}
		printf("Case #%d: %lf\n",test++, ans + 0.0000001);
	}
}