#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:160777216")
#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <string>
#include <cstdio>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <sstream>
#define eps 1e-6
#define INF 1000000000
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define ALL(x) x.begin() , x.end()
#define PB push_back
#define FOR(i , n) for (i = 0; i < n; i++)
#define FAB(i , a , b) for (i = a; i <= b; i++)
#define ll long long
#define NMAX 100001
using namespace std;

int n, m, q, i, j, k , p;

int a[200];
int u[10];
int d[110][110][110][5];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	d[0][0][0][0] = 0;

	for (i = 0; i <= 100; i++)
		for (j = 0; j <= 100; j++)
			for (k = 0; k <= 100; k++)
				for (m = 0; m < 4; m++)
				{
					if (d[i][j][k][m] < 0)
						continue;

					if (m == 0)
					{
						d[i + 1][j][k][1] = max(d[i + 1][j][k][1], d[i][j][k][0] + 1);
						d[i][j + 1][k][2] = max(d[i][j + 1][k][2], d[i][j][k][0] + 1);
						d[i][j][k + 1][3] = max(d[i][j][k + 1][3], d[i][j][k][0] + 1);
					}
					else
					{
						d[i + 1][j][k][(m + 1) % 4] = max(d[i + 1][j][k][(m + 1) % 4], d[i][j][k][m]);
						d[i][j + 1][k][(m + 2) % 4] = max(d[i][j + 1][k][(m + 2) % 4], d[i][j][k][m]);
						d[i][j][k + 1][(m + 3) % 4] = max(d[i][j][k + 1][(m + 3) % 4], d[i][j][k][m]);
					}
				}

	int t;
	cin >> t;

	

	for (int test = 1; test <= t; test++)
	{
		cin >> n >> p;
		for (i = 0; i <= 4; i++)
			u[i] = 0;

		for (i = 0; i < n; i++)
		{
			cin >> a[i];
			u[a[i] % p]++;
		}

		int ans = 0;

		ans += u[0];

		cout << "Case #" << test << ": ";

		if (p == 2)
		{
			ans += (u[1] + 1) / 2;
			cout << ans << endl;
		} else
			if (p == 3)
			{
				while (u[1] > 0 && u[2] > 0)
				{
					u[1]--;
					u[2]--;
					ans++;
				}

				while (u[1] > 0)
				{
					ans++;
					u[1] -= 3;
				}

				while (u[2] > 0)
				{
					ans++;
					u[2] -= 3;
				}

				cout << ans << endl;
			}
			else
			{
				ans = 0;
				for (i = 0; i < 4; i++)
					ans = max(ans, d[u[1]][u[2]][u[3]][i]);
				cout << ans + u[0]<< endl;
			}
	
	}
	return 0;
}