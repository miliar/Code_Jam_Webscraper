#define _CRT_SECURE_NO_WARNINGS

#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>


using namespace std;

int g[1000];

int dp[101][101][101][101][4];

void Solve()
{
	int N, P;
	scanf("%d %d", &N, &P);

	int cnt[4] = { 0 };

	for (int i = 0; i < N; ++i){
		scanf("%d", g + i);

		cnt[g[i] % P]++;
	}

	for (int ii = 0; ii <= cnt[0]; ii++)
		for (int i = 0; i <= cnt[1]; i++)
			for (int j = 0; j <= cnt[2]; j++)
				for (int k = 0; k <= cnt[3]; k++)
					for (int l = 0; l < P; l++)
						dp[ii][i][j][k][l] = -N;
	dp[0][0][0][0][0] = 0;

	int result = 0;
	for (int zero = 0; zero <= cnt[0]; ++zero){
		for (int one = 0; one <= cnt[1]; ++one){
			for (int two = 0; two <= cnt[2]; ++two){
				for (int three = 0; three <= cnt[3]; ++three){
					for (int m = 0; m < P; ++m){
						int ans = -N;
						if (zero > 0){
							dp[zero][one][two][three][m] = max(dp[zero][one][two][three][m], dp[zero - 1][one][two][three][m] + ((m == 0) ? 1 : 0));
						}
						if (one > 0){
							int src = (m + P - 1) % P;
							dp[zero][one][two][three][m] = max(dp[zero][one][two][three][m], dp[zero][one - 1][two][three][src] + ((src == 0) ? 1 : 0));
						}
						if (two > 0){
							int src = (m + P - 2) % P;
							dp[zero][one][two][three][m] = max(dp[zero][one][two][three][m], dp[zero][one][two - 1][three][src] + ((src == 0) ? 1 : 0));
						}
						if (three > 0){
							int src = (m + P - 3) % P;
							dp[zero][one][two][three][m] = max(dp[zero][one][two][three][m], dp[zero][one][two][three - 1][src] + ((src == 0) ? 1 : 0));
						}
						result = max(result, dp[zero][one][two][three][m]);
					}
				}
			}
		}
	}

	printf("%d\n", result);
}

int main()
{
	int T;
	freopen("A-large.in", "r", stdin);
	freopen("large_output.txt", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
}