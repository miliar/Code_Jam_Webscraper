//Technobabble

#define _CRT_SECURE_NO_WARNINGS
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

bool Solve()
{
	int Num = in();
	int K = in();
	double Rem = inD();
	vector<double> Prob;
	for (int i = 0; i < Num; i++)
	{
		Prob.push_back(inD());
	}
	sort(Prob.begin(), Prob.end());
	for (int i = 0; i < Num-1; i++)
	{
		if ((Prob[i + 1] - Prob[i]) * double(i + 1) < Rem)
		{
			Rem -= (Prob[i + 1] - Prob[i]) * double(i + 1);
			for (int j = 0; j < i + 1; j++)
				Prob[j] = Prob[i + 1];
		}
		else if(Rem)
		{
			double Factor = Rem / ((Prob[i + 1] - Prob[i]) * double(i + 1));
			Rem = 0;
			for (int j = 0; j < i + 1; j++)
				Prob[j] += (Prob[i + 1] - Prob[j]) * Factor;
		}
	}
	for (int i = 0; i < Num; i++)
		Prob[i] += Rem / double(Num);
	double P = 1;
	for (int i = 0; i < Num; i++)
		P *= min(Prob[i], 1.0);
	printf("%.9f\n", P);
	return true;
}
void main()
{
//#define FILE "C-Test"
//#define FILE "C-small-practice"
#define FILE "C-small-1-attempt1"
//#define FILE "C-large"
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
