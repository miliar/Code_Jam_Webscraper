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

db P[60];

int main()
{
	int T, n, k, i, mncnt;
	db u, prob, mn, mn2;

	scanf("%d", &T);

	BL
	{
		scanf("%d%d", &n, &k);

		scanf("%lf", &u);

		for(i = 0; i < n; i++)
		{
			scanf("%lf", P + i);
		}

		while(u != 0.0)
		{
			mn = 2.0;
			mn2 = 2.0;
			mncnt = 0;

			for(i = 0; i < n; i++)
			{
				if(P[i] < mn)
				{
					mn = P[i];
					mncnt = 1;
				} else if(P[i] == mn) {
					mncnt++;
				}
			}

			for(i = 0; i < n; i++)
			{
				if(P[i] > mn)
				{
					mn2 = min(mn2, P[i]);
				}
			}

			if(mn2 == 2.0)
			{
				for(i = 0; i < n; i++)
				{
					P[i] += u / (db)n;
				}

				u = 0.0;
			} else {
				if(u <= (mn2 - mn) * (db)mncnt)
				{
					for(i = 0; i < n; i++)
					{
						if(P[i] == mn)
						{
							P[i] += u / (db)mncnt;
						}
					}

					u = 0.0;
				} else {
					for(i = 0; i < n; i++)
					{
						if(P[i] == mn)
						{
							P[i] = mn2;
						}
					}

					u -= (mn2 - mn) * (db)mncnt;
				}
			}
		}

		prob = 1.0;

		for(i = 0; i < n; i++)
		{
			prob *= P[i];
		}

		printf("Case #%d: %.12E\n", K, prob);
	}
}
/*
===
---
===
---
===
*/