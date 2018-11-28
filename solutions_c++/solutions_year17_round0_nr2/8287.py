/*
* Note: This template uses some c++11 functions , so you have to compile it with c++11 flag.
*       Example:-   $ g++ -std=c++11 c++Template.cpp
*
* Author : Akshay Pratap Singh
* Handle: code_crack_01
*
*/

/********   All Required Header Files ********/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

/*******  All Required define Pre-Processors and typedef Constants *******/
#define SCD(t) scanf("%d",&t)
#define SCLD(t) scanf("%ld",&t)
#define SCLLD(t) scanf("%lld",&t)
#define SCC(t) scanf("%c",&t)
#define SCS(t) scanf("%s",t)
#define SCF(t) scanf("%f",&t)
#define SCLF(t) scanf("%lf",&t)
#define MEM(a, b) memset(a, (b), sizeof(a))
#define FOR(i, j, k, in) for (int i=j ; i<k ; i+=in)
#define RFOR(i, j, k, in) for (int i=j ; i>=k ; i-=in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.end(), cont.begin()
#define FOREACH(it, l) for (auto it = l.begin(); it != l.end(); it++)
#define IN(A, B, C) assert( B <= A && A <= C)
#define MP make_pair
#define PB push_back
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define read(type) readInt<type>()
const double pi = acos(-1.0);
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<PII> VII;
typedef vector<VI> VVI;
typedef map<int, int> MPII;
typedef set<int> SETI;
typedef multiset<int> MSETI;
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int  uint64;

/****** Template of some basic operations *****/
template<typename T, typename U> inline void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if (x < y) x = y; }
/**********************************************/

bool tidy(long long n)
{
	int b = n % 10;
	while (n)
	{		
		n /= 10;
		int a = n % 10;
		if (a > b)
			return false;
		b = a;
	}

	return true;
}

int get_k(long long n, int k)
{
	FOR(i, 0, k, 1)
		n /= 10;
	return n % 10;	
}

int* int_to_arr(long long n, int count)
{	
	int* arr = new int[count];
	count = 0;
	while (n)
	{
		arr[count++] = n % 10;
		n /= 10;
	}
	return arr;
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	int t;
	fin >> t;

	int count_case = 1;
	while (t--)
	{
		long long n;
		fin >> n;

		if (tidy(n)) fout << "Case #" << count_case++ << ": " << n << endl;
		else
		{
			int count = 0;
			long long t = n;
			while (t)
			{
				t /= 10;
				count++;
			}
			int* arr = int_to_arr(n, count);
			int s = sizeof(arr);
			t = n;
			
			int reduce_dig = 0;
			FOR(i, 0, count-1, 1)
			{
				if (arr[i] < arr[i + 1])
				{
					FOR(k,0,i+1,1)
						arr[k] = 9;
					
					int j = i + 1;
					while (j < count && arr[j] == 0)
					{
						arr[j++] = 9;							
					}
					arr[j]--;

					if (arr[j] == 0 && j == count - 1) reduce_dig = 1;
				}
			}

			fout << "Case #" << count_case++ << ": ";
			RFOR(i, count - reduce_dig - 1, 0, 1)
			{
				fout << arr[i];
			}
			fout << endl;

			//debug
			long long number = 0;
			RFOR(i, count - reduce_dig - 1, 0, 1)
			{
				number = 10 * number + arr[i];
			}			
			assert(tidy(number));
			
		}


		
	}
}