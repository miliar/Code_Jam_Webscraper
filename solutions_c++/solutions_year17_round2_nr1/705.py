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

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; test++)
	{
		int D, n, i, k, s;
		scanf("%d %d", &D, &n);
		double res = 0;
		for(i = 0; i < n; i++)
		{
			scanf("%d %d", &k, &s);
			res = max(res, 1.0 * (D - k) / s);
		}
		printf("Case #%d: %.9f\n", test, D / res);
	}
}