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

pair<Int, Int> solve(Int n, Int k)
{
	map<Int, Int> M;
	M[n] = 1;
	pair<Int, Int> res;
	while(k > 0)
	{
		auto last = --M.end();
		auto cnt = min(k, last->second);
		auto a = last->first / 2;
		auto b = last->first - 1 - a;
		res.first = max(a, b);
		res.second = min(a, b);
		M.erase(last);
		M[a] += cnt;
		M[b] += cnt;
		k -= cnt;
	}
	return res;
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; test++)
	{
		Int n, k;
		scanf("%I64d %I64d", &n, &k);
		auto res = solve(n, k);
		printf("Case #%d: %I64d %I64d\n", test, res.first, res.second);
	}
}