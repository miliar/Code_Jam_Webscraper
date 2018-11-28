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

db r[1010], h[1010];
vector<db> tmp;

bool cmp(db a, db b)
{
	return a > b;
}

int main()
{
	int T, n, k, i, j;
	db mx, res;

	scanf("%d", &T);

	BL
	{
		scanf("%d%d", &n, &k);

		for(i = 0; i < n; i++)
		{
			scanf("%lf%lf", r + i, h + i);
		}

		mx = 0.0;

		for(i = 0; i < n; i++)
		{
			tmp.clear();

			for(j = 0; j < n; j++)
			{
				if(j != i)
				{
					if(r[j] <= r[i])
					{
						tmp.PB(2.0 * M_PI * r[j] * h[j]);
					}
				}
			}

			if(tmp.SZ < k - 1)
			{
				continue;
			}

			sort(tmp.begin(), tmp.end(), cmp);

			res = M_PI * r[i] * r[i] + 2.0 * M_PI * r[i] * h[i];

			for(j = 0; j < k - 1; j++)
			{
				res += tmp[j];
			}

			mx = max(res, mx);
		}

		printf("Case #%d: %.12lf\n", K, mx);
	}
}
/*
===
4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
---
Case #1: 138230.076757951
Case #2: 150796.447372310
Case #3: 43982.297150257
Case #4: 625.176938064
===
*/