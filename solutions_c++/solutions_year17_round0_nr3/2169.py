
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

typedef struct __MaxAndMin
{
	UINT64 max;
	UINT64 min;
}MaxAndMin;

MaxAndMin solve1(UINT64 n)
{
	MaxAndMin ans;

	if (n%2)
	{
		ans.max = n / 2;
		ans.min = n / 2;
	}
	else
	{
		ans.max = (n / 2);
		ans.min = (n / 2)-1;
	}

	return ans;

}

MaxAndMin solve2(UINT64 n)
{
	MaxAndMin ans;

	ans = solve1(n);
	ans = solve1(ans.max);

	return ans;
}

MaxAndMin solve3(UINT64 n)
{
	MaxAndMin ans;
	MaxAndMin ans1;
	MaxAndMin ans2;

	ans = solve1(n);
	ans1 = solve1(ans.max);
	ans2 = solve1(ans.min);

	return ans;
}


void solve(UINT64 n, UINT64 k)
{
	MaxAndMin ans;
	MaxAndMin ans1;
	MaxAndMin ans2;


	
	do
	{
		ans = solve1(n);

		if (k == 1)
		{
			break;
		}

		if (k == 2)
		{
			ans = solve2(n);
			break;
		}

		k--;

		if (k%2)
		{
			n = ans.max;
			k = k / 2 + 1;
			//ans = solve(ans.min, k / 2);
		}
		else
		{
			n = ans.min;
			k = k / 2;
		}
		
	} while (true);




	fout << ans.max<<" "<<ans.min << endl;

}


int main(void)
{
	int i;
	int j;
	int numOfTests;
	//int k;
	char c;
	int length;
	UINT64 k;
	UINT64 n;
	fin >> numOfTests;
	

	for (i = 0; i<numOfTests; i++)
	{
		fin >> n;
		fin >> k;

		fout << "Case #"<<i+1<<": ";
		solve(n , k);
	}
}
