/**************************************************
    WhatTheFua
    Anan Schuett
    arnan_s@msn.com
**************************************************/

#define BK back()
#define BL for(int K = 1; K <= T; K++)
#define F first
#define INF 2147483647LL
#define LNF 8000000000000000000LL
#define P107 1000000007LL
#define P109 1000000009LL
#define PB push_back
#define PF push_front
#define I insert
#define E erase
#define S second
#define SZ size()
#define IT iterator
#define db double
#define ll long long int
#define mp make_pair

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int dp[800][800][2];	// 0 = C, 1 = J
bool C[1500], J[1500];

int main()
{
	int T, ac, aj, i, j, s, e;

	scanf("%d", &T);

	BL
	{
		scanf("%d%d", &ac, &aj);

		for(i = 0; i < 1500; i++)
		{
			C[i] = 1;
			J[i] = 1;
		}

		for(i = 0; i < ac; i++)
		{
			scanf("%d%d", &s, &e);

			for(j = s; j < e; j++)
			{
				C[j] = 0;
			}
		}

		for(i = 0; i < aj; i++)
		{
			scanf("%d%d", &s, &e);

			for(j = s; j < e; j++)
			{
				J[j] = 0;
			}
		}

		for(i = 0; i < 800; i++)
		{
			for(j = 0; j < 800; j++)
			{
				dp[i][j][0] = INF / 2;
				dp[i][j][1] = INF / 2;
			}
		}

		dp[0][0][0] = 0;
		dp[0][0][1] = 0;

		for(i = 0; i <= 720; i++)
		{
			for(j = 0; j <= 720; j++)
			{
				if(i != 0)
				{
					if(C[i + j])
					{
						dp[i][j][0] = min(dp[i][j][0], dp[i - 1][j][0]);
						dp[i][j][0] = min(dp[i][j][0], dp[i - 1][j][1] + 1);
					}
				}

				if(j != 0)
				{
					if(J[i + j])
					{
						dp[i][j][1] = min(dp[i][j][1], dp[i][j - 1][1]);
						dp[i][j][1] = min(dp[i][j][1], dp[i][j - 1][0] + 1);
					}
				}
			}
		}

		printf("Case #%d: %d\n", K, (min(dp[720][720][0], dp[720][720][1]) + 1) / 2 * 2);
	}
}
/*
===
---
===
---
===
*/