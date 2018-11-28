#pragma comment(linker, "/STACK:256000000")
 
#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>
#include <assert.h>
#include <time.h>
#include <memory.h>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <algorithm>
#include <random>
#include <unordered_map>
#include <unordered_set>
#include <complex>
using namespace std;
 
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;
typedef complex < double > base;
const int INF = (int)(1e9);
const int64 LINF = (int64)(1e18);
const double EPS = 1e-13;
#define sq(x) ((x)*(x))
#define FAIL() ((*(int*)(0))++)
const int MAXN = 100100;
const int BUBEN = 600000;
int n, k;
string s;
pll solve(int64 n, int64 k)
{
	int64 l, r;
	int64 sum = 0;
	int64 deg = 0;
	while(sum + (1ll << deg) < k)
	{
		sum += (1 << deg);
		deg++;
	}
	int64 ot = (n - sum) / (1 << deg);
	int64 a = (n - sum) % (1 << deg);
	k -= sum;
	if (k <= a)
	{
		l = (ot) / 2;
		r = (ot - l);
	}
	else
	{
		l = (ot - 1) / 2;
		r = ot - 1 - l;
	}
	return pll(max(l, r), min(l, r));
}

int main()
{
	cin.tie(0); ios_base::sync_with_stdio(false);
#ifdef _MY_DEBUG
    freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
#else
#endif
    srand(88);
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		int64 n, k;
		cin >> n >> k;
		pll t = solve(n, k);
		//cout << "Case #" << i + 1 << ": " << t << '\n'; 
		printf("Case #%d: %lld %lld\n", i + 1, t.first, t.second);
		
	}
    return 0;
}