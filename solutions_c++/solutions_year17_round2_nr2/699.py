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

bool doInsert(string &v, char c, int count)
{
	if (v.empty())
	{
		while (count--)
			v += c;
		return true;
	}

	for(int i = 0; i < (int)v.size() && count; i++)
	{
		if (v[i] == v[(i - 1 + (int)v.size()) % v.size()])
		{
			v.insert(v.begin() + i, c);
			count--;
			i++;
		}
	}
	for(int i = 0; i < (int)v.size() && count; i++)
	{
		if (v[i] != c && v[(i - 1 + (int)v.size()) % v.size()] != c)
		{
			v.insert(v.begin() + i, c);
			count--;
			i++;
		}
	}
	return count == 0;
}

bool solve4(int R, int Y, int B)
{
	string res;

	bool ans = true;
	for (int k = 0; k < 3; k++)
	{
		if (R >= Y && R >= B)
			ans &= doInsert(res, 'R', R), R = 0;
		else if (Y >= R && Y >= B)
			ans &= doInsert(res, 'Y', Y), Y = 0;
		else if (B >= R && B >= Y)
			ans &= doInsert(res, 'B', B), B = 0;
	}
	if (!ans)
		return false;
	for (int i = 0; i < (int)res.size(); i++)
		if (res[i] == res[(i + 1) % res.size()] || res[i] == res[(i - 1 + (int)res.size()) % res.size()])
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
		if (!solve(R, Y, B) && !solve2(R, Y, B) && !solve3(R, Y, B) && !solve4(R, Y, B))
		{
			puts("IMPOSSIBLE");
		}
	}
}

/*
2
3 1 0 2 0 0 0
6 2 0 2 0 2 0


4
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2

*/