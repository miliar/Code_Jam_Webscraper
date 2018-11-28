#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm>
#include <iostream> 
#include <string.h> 
#include <stdlib.h>
#include <complex>
#include <sstream> 
#include <fstream>
#include <numeric>
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
#define Int long long 
#define INF 0x3F3F3F3F 
#define eps 1e-9
using namespace std;

#define LINF (1ll << 61ll)

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; test++)
	{
		int n, q, i, j, k;
		scanf("%d %d", &n, &q);
		vector<int> total(n), speed(n);
		for (i = 0; i < n; i++)
			scanf("%d %d", &total[i], &speed[i]);
		vector<vector<Int> > d(n, vector<Int>(n));
		vector<vector<double> > dd(n, vector<double>(n, LINF));
		for(i = 0; i < n; i++)
		{
			for(j = 0; j < n; j++)
			{
				scanf("%I64d", &d[i][j]);
				if (d[i][j] == -1)
					d[i][j] = LINF;
			}
		}
		for (i = 0; i < n; i++)
		{
			d[i][i] = 0;
			dd[i][i] = 0;
		}
		for (k = 0; k < n; k++)
			for (i = 0; i < n; i++)
				for (j = 0; j < n; j++)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
		for(i = 0; i < n; i++)
		{
			for(j = 0; j < n; j++)
			{
				if (d[i][j] <= total[i])
					dd[i][j] = 1.0 * d[i][j] / speed[i];
			}
		}
		for (k = 0; k < n; k++)
			for (i = 0; i < n; i++)
				for (j = 0; j < n; j++)
					dd[i][j] = min(dd[i][j], dd[i][k] + dd[k][j]);
		printf("Case #%d:", test);
		while(q--)
		{
			int a, b;
			scanf("%d %d", &a, &b);
			a--, b--;
			printf(" %.9f", dd[a][b]);
		}
		puts("");
	}
}

/*
bool solve(int R, int Y, int B)
{
	string res;
	while(R + Y + B)
	{
		if (R > 0 && R >= Y && R >= B && (res.empty() || res.back() != 'R'))
		{
			res += 'R';
			R--;
		}
		else if (Y > 0 && Y >= R && Y >= B && (res.empty() || res.back() != 'Y'))
		{
			res += 'Y';
			Y--;
		}
		else if (B > 0 && B >= R && B >= Y && (res.empty() || res.back() != 'B'))
		{
			res += 'B';
			B--;
		}
		else
		{
			return false;
		}
	}
	if (res.back() == res[0])
		return false;
	puts(res.c_str());
	return true;
}

bool solve2(int R, int Y, int B)
{
	int r = 0, y = 0, b = 0;
	string res;
	if (R)
		R--, r--, res += 'R';
	else if (Y)
		Y--, y--, res += 'Y';
	else if (B)
		B--, b--, res += 'B';
	while (R + Y + B)
	{
		if (R > 0 && R - r >= Y && R - r >= B && res.back() != 'R')
		{
			res += 'R';
			R--;
		}
		else if (Y > 0 && Y - y >= R && Y - y >= B && res.back() != 'Y')
		{
			res += 'Y';
			Y--;
		}
		else if (B > 0 && B - b >= R && B - b >= Y && res.back() != 'B')
		{
			res += 'B';
			B--;
		}
		else
		{
			return false;
		}
	}
	if (res.back() == res[0])
		return false;
	puts(res.c_str());
	return true;
}

bool solve3(int R, int Y, int B)
{
	string res;
	if (R && R >= Y && R >= B)
		R--, res += 'R';
	else if (Y && Y >= R && Y >= B)
		Y--, res += 'Y';
	else if (B && B >= R && B >= Y)
		B--, res += 'B';
	while (R + Y + B)
	{
		if (R && (R > Y || R == Y && res[0] == 'R') && (R > B || R == B && res[0] == 'R') && res.back() != 'R')
		{
			res += 'R';
			R--;
		}
		else if (Y && (Y > R || Y == R && res[0] == 'Y') && (Y > B || Y == B && res[0] == 'Y') && res.back() != 'Y')
		{
			res += 'Y';
			Y--;
		}
		else if (B && (B > R || B == R && res[0] == 'B') && (B > Y || B == Y && res[0] == 'B') && res.back() != 'B')
		{
			res += 'B';
			B--;
		}
		else
		{
			return false;
		}
	}
	if (res.back() == res[0])
		return false;
	puts(res.c_str());
	return true;
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		int R, Y, B;
		scanf("%*d %d %*d %d %*d %d %*d", &R, &Y, &B);

		printf("Case #%d: ", test);
		if (!solve(R, Y, B) && !solve2(R, Y, B) && !solve3(R, Y, B))
		{
			puts("IMPOSSIBLE");
		}
	}
}
*/
/*
2
6 2 0 2 0 2 0
3 1 0 2 0 0 0


4
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2

*/