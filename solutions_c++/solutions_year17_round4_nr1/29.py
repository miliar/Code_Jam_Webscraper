#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;
const i64 MOD = 0;
template <typename T> void ADD(T &a, const T b) { a = (a + b) % MOD; }
int T;

int N, P, G[101];

int rup(int p, int q)
{
	return p / q + (p % q != 0 ? 1 : 0);
}

int dp[110][110][110];

#define APPLY(x,y,z) if (i >= x && j >= y && k >= z) dp[i][j][k] = max(dp[i][j][k], dp[i-x][j-y][k-z]+1)

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T;) {
		scanf("%d%d", &N, &P);
		int ret = 0;
		int ns[4] = { 0, 0, 0, 0 };

		for (int i = 0; i < N; ++i) {
			scanf("%d", G + i);
			ns[G[i] % P]++;
		}
		
		for (int i = 0; i <= ns[1]; ++i) {
			for (int j = 0; j <= ns[2]; ++j) {
				for (int k = 0; k <= ns[3]; ++k) {
					dp[i][j][k] = 0;
					if (i + j + k != 0) dp[i][j][k] = 1;

					if (P == 2) {
						APPLY(2, 0, 0);
					} else if (P == 3) {
						APPLY(3, 0, 0);
						APPLY(0, 3, 0);
						APPLY(1, 1, 0);
					} else {
					}
				}
			}
		}
		printf("Case #%d: %d\n", t, dp[ns[1]][ns[2]][ns[3]] + ns[0]);
	}

	return 0;
}
