//Brattleship

#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
//includes and helperfunctions based on JAPLJ_0_1.zip
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

struct Pan
{
	double Radius, Height;
	bool operator<(Pan& rhs)
	{
		return Radius > rhs.Radius;
	}
};

bool Solve()
{
	int Num = in();
	int Take = in();

	vector<Pan> Pans;
	for (int i = 0; i < Num; i++)
	{
		Pan P;
		P.Radius = in();
		P.Height = in();
		Pans.push_back(P);
	}
	sort(Pans.begin(), Pans.end());

	double MaxA = 0;
	for (int i = 0; i < Num; i++)
	{
		vector<double> Areas;
		for (int j = i + 1; j < Num; j++)
			Areas.push_back(Pans[j].Radius * 2.0 * M_PI * Pans[j].Height);
		sort(Areas.begin(), Areas.end());
		double A = Pans[i].Radius * 2.0 * M_PI * Pans[i].Height;
		if ((int)Areas.size() < Take - 1)
			continue;
		for (int j = 0; j < Take-1; j++)
			A += Areas[Areas.size()-1-j];
		A += Pans[i].Radius*Pans[i].Radius*M_PI;
		MaxA = max(A, MaxA);
	}
	printf("%.9f\n", MaxA);

	return true;
}

void main()
{
//#define FILE "A-Test"
//#define FILE "A-small-practice"
//#define FILE "A-small-attempt0"
#define FILE "A-large"
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
