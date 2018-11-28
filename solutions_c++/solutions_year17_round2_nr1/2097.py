
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <limits>
#include <iomanip>
#include <cstdarg>
#define UINT64 unsigned __int64
using namespace std;
ifstream  fin("b.txt");
ofstream  fout("c.txt");
#define MAX(a,b) (((a) > (b)) ? (a) : (b))

UINT64 gArrayLoca[2000];
UINT64 gArraySpeed[2000];

// "", "ONE", "", "THREE", "", "", "", "SEVEN", "", "NINE"

void solve(int numOfHorse, UINT64 d)
{
	long double ans;
	int i;
	int j;
	long double tc;
	long double tSlow;

	for (i = 0; i < numOfHorse; i++)
	{
		tc = ((long double)d - (long double)gArrayLoca[i]) / (long double)gArraySpeed[i];

		if (i==0)
		{
			tSlow = tc;
		}
		else if (tc > tSlow)
		{
			tSlow = tc;
		}
	}

	ans = (long double)d / tSlow;
	int precision = std::numeric_limits<double>::max_digits10;
	fout << std::setprecision(6)<< fixed <<ans<<endl;
}


int main(void)
{
	int i;
	int j;
	int numOfTests;
	int k;
	int c;
	int r;
	
	int length;

//	UINT64 k;
	UINT64 d;
	fin >> numOfTests;

	for (i = 0; i<numOfTests; i++)
	{
		fin >> d;
		fin >> r;
		for (j= 0; j < r; j++)
		{
			fin >> gArrayLoca[j];
			fin >> gArraySpeed[j];
		}

		fout << "Case #"<<i+1<<": ";
		solve(r, d);
	}
}
