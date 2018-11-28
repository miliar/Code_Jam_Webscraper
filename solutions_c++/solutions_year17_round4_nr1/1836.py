//

#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <array>
#include <list>
#include <stack>
#include <valarray>

using namespace std;

typedef unsigned uint;
typedef long long s64;
typedef unsigned long long u64;

const int Inf32 = 1001001001;
const s64 Inf64 = 1001001001001001001LL;
const double InfD = 1001001001001.0;

template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; int r = scanf("%d", &x); assert(r == 1); return x; }
double inD() { double x; int r = scanf("%lf", &x); assert(r == 1); return x; }
s64 in64() { s64 x; int r = scanf("%lld", &x); assert(r == 1); return x; }
void inS(char* Buffer) { int r = scanf("%s", Buffer); assert(r == 1); }


bool Solve()
{
	int n = in();
	int p = in();
	int Count[4] = { 0 };
	for (int i = 0; i < n; i++)
		Count[in() % p]++;
	int Misses = 0;
	if (p == 2)
		Misses = Count[1] / 2;
	else if (p == 3)
	{
		int m = min(Count[1], Count[2]);
		Misses += m;
		Count[1] -= m;
		Count[2] -= m;
		Misses += Count[1] / 3 * 2;
		if (Count[1] % 3 == 2)
			Misses++;

		Misses += Count[2] / 3 * 2;
		if (Count[2] % 3 == 2)
			Misses++;
	}
	else
		assert(0);
	printf("%i\n", n - Misses);
	return true;
}

void main()
{
//#define FILE "A-Test"
//#define FILE "A-small-practice"
#define FILE "A-small-attempt0"
//#define FILE "A-large"
	if (!freopen(FILE ".in", "r", stdin))
	{
		fprintf(stderr, "Cannot open " FILE ".in for reading!\n");
		return;
	}
	freopen(FILE ".out", "w", stdout);

	int T = in();
	for (int i = 1; i <= T; i++)
	{
		if (i == 5)
			i = i;//breakpoint
		printf("Case #%d: ", i);
		if(!Solve())
			printf("IMPOSSIBLE\n");
	}

	scanf("\n");
	assert(feof(stdin));
}
//	printf("%.9f\n", );
