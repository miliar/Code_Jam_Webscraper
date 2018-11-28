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

db k[1010], s[1010];

int main()
{
	int T, n, i;
	db d;
	db st, md, ed;
	scanf("%d", &T);

	BL
	{
		scanf("%lf%d", &d, &n);

		for(i = 0; i < n; i++)
		{
			scanf("%lf%lf", k + i, s + i);
		}

		st = (db)0;
		ed = (db)100000000000000;

		while(ed - st > st / (db)10000000)
		{
			md = (st + ed) / (db)2;

			// printf("%.9lf %.9lf %.9lf\n", st, md, ed);

			for(i = 0; i < n; i++)
			{
				if(d / md < (d - k[i]) / s[i])
				{
					break;
				}
			}

			if(i != n)
			{
				ed = md;
			} else {
				st = md;
			}
		}

		printf("Case #%d: %.09lf\n", K, st);
	}
}
/*
===
1
1000000000 1
999999999 1
---
0
===
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
---
Case #1: 101.000000
Case #2: 100.000000
Case #3: 33.333333
===
*/