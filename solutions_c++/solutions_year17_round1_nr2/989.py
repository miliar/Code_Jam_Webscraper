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

int r[60];
int q[60][60];
priority_queue<pair<int, int> > PQ[60];

int main()
{
	int T, n, p, i, j, k, res;

	scanf("%d", &T);

	BL
	{
		for(i = 0; i < 60; i++)
		{
			while(!PQ[i].empty())
			{
				PQ[i].pop();
			}
		}

		scanf("%d%d", &n, &p);

		res = 0;

		for(i = 0; i < n; i++)
		{
			scanf("%d", r + i);
		}

		for(i = 0; i < n; i++)
		{
			for(j = 0; j < p; j++)
			{
				scanf("%d", q[i] + j);

				if((10 * q[i][j] + 11 * r[i] - 1) / (11 * r[i]) <= (10 * q[i][j]) / (9 * r[i]))
				{
					// printf("push %d, %d\n", (10 * q[i][j] + 11 * r[i] - 1) / (11 * r[i]), (10 * q[i][j]) / (9 * r[i]));

					PQ[i].push(mp((10 * q[i][j] + 11 * r[i] - 1) / (11 * r[i]), (10 * q[i][j]) / (9 * r[i])));
				}
			}
		}

		for(k = 1000000; k >= 1; k--)
		{
			for(i = 0; i < n; i++)
			{
				if(PQ[i].empty())
				{
					i = -1;
					break;
				}

				if(PQ[i].top().S < k)
				{
					i = -1;
					break;
				} else {
					while(!PQ[i].empty())
					{
						if(PQ[i].top().F > k)
						{
							PQ[i].pop();
						} else {
							break;
						}
					}

					if(PQ[i].empty())
					{
						i = -1;
						break;
					}
				}
			}

			if(i != -1)
			{
				// printf("add %d\n", k);

				res++;

				for(i = 0; i < n; i++)
				{
					// printf("pack (%d, %d)\n", PQ[i].top().F, PQ[i].top().S);

					PQ[i].pop();
				}

				k++;
			}
		}

		printf("Case #%d: %d\n", K, res);
	}
}
/*
===
6
2 1
500 300
900
660
2 1
500 300
1500
809
2 2
50 100
450 449
1100 1101
2 1
500 300
300
500
1 8
10
11 13 17 11 16 14 12 18
3 3
70 80 90
1260 1500 700
800 1440 1600
1700 1620 900
---
Case #1: 1
Case #2: 0
Case #3: 1
Case #4: 0
Case #5: 3
Case #6: 3
===
---
===
*/