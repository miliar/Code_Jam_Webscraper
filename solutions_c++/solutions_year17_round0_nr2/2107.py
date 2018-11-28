
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

void solve(int arrayLength)
{
	unsigned int ans = 0;
	unsigned int j;
	unsigned int i;

	ans = 7;

	for (i = 0; i <arrayLength-1; )
	{
		if (gArray[i] <= gArray[i+1])
		{
			i++;
			continue;
		}
		else if(i == 0 && gArray[i] == '1')
		{
			memset(gArray, 0, 2000);
			memset(gArray, '9', arrayLength-1);
			break;
		}
		else //if(gArray[i] != '1')
		{
			gArray[i]--;
		
			for (j = i+1; j < arrayLength; j++)
			{
				gArray[j] = '9';
			}
			i--;
		}
	}

	fout << gArray << endl;

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
		for (j = 0; gArray[j] != 0; j++)
		{


		}

		fout << "Case #"<<i+1<<": ";
		solve(j);
	}
}
