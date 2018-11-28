#define SUBMIT
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

#define PI acos(-1.0)
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define INF 100000000000000007LL
#define eps 1e-12
#define ll long long
#define f0(i , n) for (int i = 0; i < n; i++)
#define NMAX 500000
using namespace std;

int i, j, n, m, t, test , k ;

ll maxdis[1000], speed[1000];
ll d[201][201];
double a[201][201];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);



	cin >> t;
	int q;
	for (test = 1; test <= t; test++)
	{
		cin >> n >> q;
		for (i = 0; i < n; i++)
			cin >> maxdis[i]>>speed[i];

		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				cin >> d[i][j];
				if (d[i][j] == -1)
					d[i][j] = INF;
			}
		}

		for (k = 0; k < n; k++)
			for (i = 0; i < n; i++)
				for (j = 0; j < n; j++)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

		
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				if (i == j)
					continue;

				if (d[i][j] <= maxdis[i])
				{
					a[i][j] = 1.0 * d[i][j] / speed[i];
				}
				else
					a[i][j] = INF;
			}

			a[i][j] = 0;
		}

		for (k = 0; k < n; k++)
			for (i = 0; i < n; i++)
				for (j = 0; j < n; j++)
					a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
		
		
		
		cout << "Case #" << test << ":";
		while (q--)
		{
			int x, y;
			cin >> x >> y;
			x--;
			y--;
			printf(" %.9lf", a[x][y]);
			

		}

		cout << endl;
		
	}

	return 0;
}