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

char inp[30][30];
int n, m;
pair<pair<int, int>, pair<int, int> > box[30];
stack<char> unused;

void expand()
{
	int i, j, k;

	for(k = 0; k < 26; k++)
	{
		int mx = box[k].F.F, my = box[k].F.S, Mx = box[k].S.F, My = box[k].S.S;

		while(mx > 0 && mx != INF)
		{
			for(i = my; i <= My; i++)
			{
				if(inp[mx - 1][i] != '?')
				{
					i = -1;
					break;
				}
			}

			if(i != -1)
			{
				for(i = my; i <= My; i++)
				{
					inp[mx - 1][i] = 'A' + k;
				}
			} else {
				break;
			}

			mx--;
		}

		while(Mx < n - 1 && Mx != -1)
		{
			for(i = my; i <= My; i++)
			{
				if(inp[Mx + 1][i] != '?')
				{
					i = -1;
					break;
				}
			}

			if(i != -1)
			{
				for(i = my; i <= My; i++)
				{
					inp[Mx + 1][i] = 'A' + k;
				}
			} else {
				break;
			}

			Mx++;
		}

		box[k] = mp(mp(mx, my), mp(Mx, My));
	}

	for(k = 0; k < 26; k++)
	{
		int mx = box[k].F.F, my = box[k].F.S, Mx = box[k].S.F, My = box[k].S.S;

		while(my > 0 && my != INF)
		{
			for(i = mx; i <= Mx; i++)
			{
				if(inp[i][my - 1] != '?')
				{
					i = -1;
					break;
				}
			}

			if(i != -1)
			{
				for(i = mx; i <= Mx; i++)
				{
					inp[i][my - 1] = 'A' + k;
				}
			} else {
				break;
			}

			my--;
		}

		while(My < m - 1 && My != -1)
		{
			for(i = mx; i <= Mx; i++)
			{
				if(inp[i][My + 1] != '?')
				{
					i = -1;
					break;
				}
			}

			if(i != -1)
			{
				for(i = mx; i <= Mx; i++)
				{
					inp[i][My + 1] = 'A' + k;
				}
			} else {
				break;
			}

			My++;
		}

		box[k] = mp(mp(mx, my), mp(Mx, My));
	}
}

void fill(int x, int y)
{
	int mx = x, my = y, Mx = x, My = y, i, j;

	while(Mx < n - 1)
	{
		if(inp[Mx + 1][y] == '?')
		{
			Mx++;
		} else {
			break;
		}
	}

	while(My < m - 1)
	{
		for(i = mx; i <= Mx; i++)
		{
			if(inp[i][My + 1] != '?')
			{
				i = -1;
				break;
			}
		}

		if(i != -1)
		{
			My++;
		} else {
			break;
		}
	}

	for(i = mx; i <= Mx; i++)
	{
		for(j = my; j <= My; j++)
		{
			inp[i][j] = unused.top();
		}
	}

	unused.pop();
}

int main()
{
	int T, i, j, k, mx, Mx, my, My;

	scanf("%d", &T);

	BL
	{
		while(!unused.empty())
		{
			unused.pop();
		}

		scanf("%d%d", &n, &m);

		for(i = 0; i < n; i++)
		{
			scanf("%s", inp[i]);
		}

		for(k = 'A'; k <= 'Z'; k++)
		{
			mx = INF;
			Mx = -1;
			my = INF;
			My = -1;

			for(i = 0; i < n; i++)
			{
				for(j = 0; j < m; j++)
				{
					if(inp[i][j] == k)
					{
						mx = min(mx, i);
						Mx = max(Mx, i);

						my = min(my, j);
						My = max(My, j);
					}
				}
			}

			if(mx != INF)
			{
				for(i = mx; i <= Mx; i++)
				{
					for(j = my; j != My; j++)
					{
						inp[i][j] = k;
					}
				}
			} else {
				unused.push((char)k);
			}

			box[k - 'A'] = mp(mp(mx, my), mp(Mx, My));
		}

		expand();

		for(i = 0; i < n; i++)
		{
			for(j = 0; j < m; j++)
			{
				if(inp[i][j] == '?')
				{
					fill(i, j);
				}
			}
		}

		printf("Case #%d:\n", K);

		for(i = 0; i < n; i++)
		{
			printf("%s\n", inp[i]);
		}
	}
}
/*
===
3
3 3
HHG
C?G
CJJ
3 4
CODE
????
?JAM
2 2
CA
KE
---
Case #1:
GGJ
CCJ
CCJ
Case #2:
CODE
COAE
JJAM
Case #3:
CA
KE
===
*/