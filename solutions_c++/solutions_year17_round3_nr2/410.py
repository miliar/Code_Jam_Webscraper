//

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
	int NumA = in();
	int NumB = in();
	int Start[200], End[200];
	for (int i = 0; i < NumA + NumB; i++)
	{
		Start[i] = in();
		End[i] = in();
	}
	vector<int> AFrees, BFrees;
	int Switches = 0;
	int ATime = 0, BTime = 0;
	for (int i = 0; i < NumA + NumB; i++)
	{
		int Next = -1;
		int MinDist = 10000;
		for (int j = 0; j < NumA + NumB; j++)
		{
			int Dist = Start[j] - End[i];
			if (Dist < 0)
				Dist += 60 * 24;
			if (Dist < MinDist)
			{
				MinDist = Dist;
				Next = j;
			}
		}
		if (i < NumA)
			ATime += End[i] - Start[i];
		else
			BTime += End[i] - Start[i];
		if ((i < NumA) == (Next < NumA))
		{
			if (MinDist)
			{
				if (i < NumA)
					AFrees.push_back(MinDist);
				else
					BFrees.push_back(MinDist);
			}
		}
		else
			Switches++;
	}
	int AFreeTime = 60 * 12 - ATime;
	int BFreeTime = 60 * 12 - BTime;
	sort(AFrees.begin(), AFrees.end());
	sort(BFrees.begin(), BFrees.end());
	while (true)
	{
		if (!AFrees.empty() && AFreeTime >= AFrees[0])
		{
			AFreeTime -= AFrees[0];
			AFrees.erase(AFrees.begin());
		}
		else
			break;
	}
	while (true)
	{
		if (!BFrees.empty() && BFreeTime >= BFrees[0])
		{
			BFreeTime -= BFrees[0];
			BFrees.erase(BFrees.begin());
		}
		else
			break;
	}
	Switches += AFrees.size() * 2;
	Switches += BFrees.size() * 2;
	printf("%d\n", Switches);
	return true;
}

void main()
{
//#define FILE "B-Test"
//#define FILE "B-small-practice"
//#define FILE "B-small-attempt0"
#define FILE "B-large"
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
