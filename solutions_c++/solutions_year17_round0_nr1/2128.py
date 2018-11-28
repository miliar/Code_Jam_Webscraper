
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

char gArray[2000];
char gNumberp[10];

void solve(int arrayLength, int k)
{
	unsigned int ans = 0;
	unsigned int j;
	unsigned int i;
	bool isGood = true;

	for (i = 0; i <= arrayLength-k; i++)
	{
		if (gArray[i] == '+')
		{
			continue;
		}
		else
		{
			ans++;
			for (j = i; j < i+k; j++)
			{
				if (gArray[j] == '-')
				{
					gArray[j] = '+';
				}
				else
				{
					gArray[j] = '-';
				}
			}
		}
	}

	for (i = arrayLength - k; i <arrayLength; i++)
	{
		if (gArray[i] == '-')
		{
			isGood = false;
			break;
		}
	}

	if (isGood)
	{
		fout << ans << endl;
	}
	else
	{
		fout << "IMPOSSIBLE" << endl;
	}

}


int main(void)
{
	int i;
	int j;
	int numOfTests;
	int k;
	char c;
	int length;
	fin >> numOfTests;
	fin.getline(gArray, 2000);
	for (i = 0; i<numOfTests; i++)
	{
		memset(gArray, 0, 2000);
		fin.getline(gArray, 2000);
		for (j = 0; j < 2000; j++)
		{
			if (gArray[j] == '-' || gArray[j] == '+')
			{

			}
			else
			{
				sscanf(&gArray[j], "%d", &k);
				break;
			}

		}

		fout << "Case #"<<i+1<<": ";
		solve(j, k);
	}
}
