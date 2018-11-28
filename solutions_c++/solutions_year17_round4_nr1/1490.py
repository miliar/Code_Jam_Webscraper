#include <iostream>
#include <cstdio>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <cmath>

#define INF 2000000000
#define MOD 1000000007
#define PI acos(-1.0)

using namespace std;

int dp[101][101][101][4];
int main() {
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum << ": ";
		int n, p;
		int arr[100];
		int ans = 0;
		cin >> n >> p;
		int cnt[4];
		for (int i = 0; i < 4; i++)
			cnt[i] = 0;
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
			if (arr[i] % p == 0)
				ans++;
			else
				cnt[arr[i] % p]++;
		}
		for (int i = 0; i <= cnt[1]; i++)
			for (int j = 0; j <= cnt[2]; j++)
				for (int k = 0; k <= cnt[3]; k++)
					for (int x = 0; x < 4; x++)
						dp[i][j][k][x] = -INF;
		dp[0][0][0][0] = 0;
		for (int i = 0; i <= cnt[1]; i++)
			for (int j = 0; j <= cnt[2]; j++)
				for (int k = 0; k <= cnt[3]; k++)
					for (int x = 0; x < p; x++) {
						if (i > 0) {
						int add = 0;
							if ((x + p - 1) % p == 0)
								add = 1;
							dp[i][j][k][x] = max(dp[i][j][k][x], dp[i - 1][j][k][(x + p - 1) % p] + add);
						}
						if (j > 0) {
							int add = 0;
							if ((x + p - 2) % p == 0)
								add = 1;
							dp[i][j][k][x] = max(dp[i][j][k][x], dp[i][j - 1][k][(x + p - 2) % p] + add);
						}
						if (k > 0) {
							int add = 0;
							if ((x + p - 3) % p == 0)
								add = 1;
							dp[i][j][k][x] = max(dp[i][j][k][x], dp[i][j][k - 1][(x + p - 3) % p] + add);
						}
					}

		cout << ans + max(0, max(dp[cnt[1]][cnt[2]][cnt[3]][1], max(dp[cnt[1]][cnt[2]][cnt[3]][0],
			max(dp[cnt[1]][cnt[2]][cnt[3]][2], dp[cnt[1]][cnt[2]][cnt[3]][3])))) << endl;
	}
	return 0;
}