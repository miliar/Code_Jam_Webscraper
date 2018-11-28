#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef pair<i64, i64> pi64;
typedef double ld;

template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }

int main() {
	FILE* fpin = fopen("c:\\B-small-attempt0.in", "r");
	FILE* fpout = fopen("c:\\B.out","w");

	int T;
	fscanf(fpin, "%d", &T);
	long long N;

	for(int i = 0; i < T; i++)
	{
		fscanf(fpin, "%lld", &N);
		printf("Case #%d: ", i+1);
		if (N < 10)	
			printf("%d\n", N);
		else
		{
			long long j = N;
			bool v = false;
			for(; j >= 10; j--)
			{
				long long tmp = j;
				long long pre = 0;
				long long c = 0;
				long long d ;
				bool r = true;
				while(tmp > 0)
				{
					d = tmp % 10;
					tmp = tmp / 10;
					c++;
					if(c == 1)
					{
						pre = d;
						continue;
					}
					if (pre >= d)
					{
						pre = d;
						continue;
					}
					else
					{
						r = false;
						break;
					}
				}
				if( r == true)
				{
					printf("%lld\n", j);
					v = true;
					break;
				}
			}
			if( v == false)
				printf("IMPOSSIBLE");//shud never reach here
		}
	}

	fclose(fpin);
	fclose(fpout);

	return 0;
}
