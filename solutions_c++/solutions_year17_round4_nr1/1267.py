#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <functional>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iomanip>
#include <string.h>
#include <climits>
#include <time.h>
#include <stdio.h>
#include <chrono>

using namespace std::chrono;
using namespace std;

#define mp make_pair
#define sqr(x) ((x)*(x))

int dp[102][102][102][102][4];
int a[4];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		int N, P;
		cin >> N >> P;
		for (int j = 0; j < 4; j++)
			a[j] = 0;
		for (int i = 0; i < N; i++)
		{
			int A;
			cin >> A;
			a[A % P]++;
		}

		for (int i = 0; i <= N; i++)
			for (int j = 0; j <= a[1]; j++)
				for (int q = 0; q <= a[2]; q++)
					for (int z = 0; z <= a[3]; z++)
						for (int ost = 0; ost < 4; ost++)
							dp[i][j][q][z][ost] = 0;
		dp[0][0][0][0][0] = 1;


		for (int i = 0; i <= N; i++)
			for (int j = 0; j <= a[1]; j++)
				for (int q = 0; q <= a[2]; q++)
					for (int z = 0; z <= a[3]; z++)
						for (int ost = 0; ost < 4; ost++)
							for (int go = 0; go < 4; go++)
							{
								if (dp[i][j][q][z][ost] != 0)
								{
									if (go == 0)
									{
										dp[i + 1][j][q][z][ost] = max(dp[i + 1][j][q][z][ost], dp[i][j][q][z][ost] + (ost == 0));
									}
									if (go == 1)
									{
										dp[i + 1][j + 1][q][z][(ost + go) % P] = max(dp[i + 1][j + 1][q][z][(ost + go) % P], dp[i][j][q][z][ost] + (ost == 0));
									}
									if (go == 2)
									{
										dp[i + 1][j][q + 1][z][(ost + go) % P] = max(dp[i + 1][j][q + 1][z][(ost + go) % P], dp[i][j][q][z][ost] + (ost == 0));
									}
									if (go == 3)
									{
										dp[i + 1][j][q][z + 1][(ost + go) % P] = max(dp[i + 1][j][q][z + 1][(ost + go) % P], dp[i][j][q][z][ost] + (ost == 0));
									}
								}
							}
		int ans = 0;
		for (int i = 0; i < 4; i++)
			ans = max(ans, dp[N][a[1]][a[2]][a[3]][i]);
		cout << ans - 1;
		cout << endl;
	}
}