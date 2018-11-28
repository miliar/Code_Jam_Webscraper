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

struct node
{
	vector<int> C;
	int d;
	bool v;
};

node V[1010];
int maxd;
int r, o, y, g, b, v;

void dfs(int c)
{
	if(V[c].v == 1)
	{
		return;
	}

	V[c].v = 1;

	for(int i = 0; i < V[c].C.size(); i++)
	{
		V[V[c].C[i]].d = max(V[c].d + 1, V[V[c].C[i]].d);
		maxd = max(maxd, V[V[c].C[i]].d);
		dfs(V[c].C[i]);
	}
}

int getval(int x)
{
	switch(x)
	{
		case 0: return r;
		case 1: return y;
		case 2: return b;
	}
}

char getchar(int x)
{
	switch(x)
	{
		case 0: return 'R';
		case 1: return 'Y';
		case 2: return 'B';
	}
}

void dec(int x)
{
	switch(x)
	{
		case 0: r--; break;
		case 1: y--; break;
		case 2: b--; break;
	}
}

int main()
{
	int T, n, i, j, re, oe, ye, ge, be, ve, p0, lp;

	scanf("%d", &T);

	BL
	{
		scanf("%d", &n);
		scanf("%d%d%d%d%d%d", &r, &o, &y, &g, &b, &v);

		if(r * 2 <= n && y * 2 <= n && b * 2 <= n)
		{
			printf("Case #%d: ", K);

			if(r >= y && r >= b)
			{
				printf("R");
				p0 = 0;
				lp = 0;
				r--;
			} else if(y >= r && y >= b) {
				printf("Y");
				p0 = 1;
				lp = 1;
				y--;
			} else {
				printf("B");
				p0 = 2;
				lp = 2;
				b--;
			}

			for(i = 1; i < n; i++)
			{
				if(getval(p0) >= r && getval(p0) >= y && getval(p0) >= b && lp != p0)
				{
					printf("%c", getchar(p0));
					lp = p0;
					dec(p0);
				} else {
					if(lp == 0)
					{
						if(y > b)
						{
							printf("Y");
							y--;
							lp = 1;
						} else {
							printf("B");
							b--;
							lp = 2;
						}
					} else if(lp == 1) {
						if(r > b)
						{
							printf("R");
							r--;
							lp = 0;
						} else {
							printf("B");
							b--;
							lp = 2;
						}
					} else {
						if(r > y)
						{
							printf("R");
							r--;
							lp = 0;
						} else {
							printf("Y");
							y--;
							lp = 1;
						}
					}
				}
			}

			printf("\n");
		} else {
			printf("Case #%d: IMPOSSIBLE\n", K);
		}

		// re = r;
		// oe = re + o;
		// ye = re + y;
		// ge = re + g;
		// be = re + b;
		// ve = re + v;

		// for(i = 1; i <= n; i++)
		// {
		// 	V[i].C.clear();
		// }

		// for(i = 1; i <= re; i++)
		// {
		// 	for(j = oe + 1; j <= be; j++)
		// 	{
		// 		V[i].C.PB(j);
		// 		V[j].C.PB(i);
		// 	}
		// }

		// for(i = oe + 1; i <= ye; i++)
		// {
		// 	for(j = ge + 1; j <= ve; j++)
		// 	{
		// 		V[i].C.PB(j);
		// 		V[j].C.PB(i);
		// 	}
		// }

		// for(i = ge + 1; i <= be; i++)
		// {
		// 	for(j = re + 1; j <= oe; j++)
		// 	{
		// 		V[i].C.PB(j);
		// 		V[j].C.PB(i);
		// 	}
		// }

		// V[1].d = 1;
		// maxd = 1;

		// dfs(1);

		// printf("%d\n", maxd);
	}
}
/*
===
2
6 2 0 2 0 2 0
3 1 0 2 0 0 0
---
Case #1: RYBRBY
Case #2: IMPOSSIBLE
===
---
===
*/