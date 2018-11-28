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
#define INF 1000000000000000007LL
#define eps 1e-12
#define ll long long
#define f0(i , n) for (int i = 0; i < n; i++)
#define NMAX 500000
using namespace std;

int i, j, n, m, t, test ;

long long k[100000], s[100000] , u[100000] , d;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	cin >> t;
	for (test = 1; test <= t; test++)
	{
		cin >> d >> n;
		for (i = 0; i < n; i++)
		{
			cin >> k[i] >> s[i];
		}

		for (i = 0; i < n; i++)
			u[i] = 0;

		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				if (i == j)
					continue;

				if (k[i] <= k[j])
				{
					if ((d - k[i]) * s[j] < (d - k[j]) * s[i])
					{
						u[i] = 1;
					} else
						if ((d - k[i]) * s[j] > (d - k[j]) * s[i])
						{
							u[j] = 1;
						}
					
				}
			}
		}

		cout << "Case #" << test << ": ";
		for (i = 0; i < n; i++)
		{
			if (!u[i])
			{
				double t = 1.0 * (d - k[i]) / s[i];
				double ans = d / t;
				printf("%.9lf\n", ans);
				break;
			}

		}

		
	}

	return 0;
}