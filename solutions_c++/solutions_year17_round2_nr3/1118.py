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

int e[110], s[110];
ll d[110];
db dist[110];

int main()
{
	int T, n, q, i, j, x, u, v;

	scanf("%d", &T);

	BL
	{
		scanf("%d%d", &n, &q);

		for(i = 1; i <= n; i++)
		{
			scanf("%d%d", e + i, s + i);
		}

		d[1] = 0;

		for(i = 1; i <= n; i++)
		{
			for(j = 1; j <= n; j++)
			{
				scanf("%d", &x);

				if(x != -1)
				{
					d[i + 1] = (ll)x + d[i];
				}
			}
		}

		scanf("%d%d", &u, &v);

		dist[n] = (db)0;

		for(i = n - 1; i >= 1; i--)
		{
		 	dist[i] = (db)1000000000000;

		 	for(j = i + 1; j <= n; j++)
		 	{
		 		if(d[j] - d[i] <= e[i])
		 		{
		 			dist[i] = min(dist[i], dist[j] + ((db)(d[j] - d[i]) / (db)s[i]));
		 			// printf("(%d, %d): %lf\n", i, j, ((db)(d[j] - d[i]) / (db)s[i]));
		 		}
		 	}
		}

		printf("Case #%d: %.9lf\n", K, dist[1]);
	}
}
/*
===
---
===
---
===
*/