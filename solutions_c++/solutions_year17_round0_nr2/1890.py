#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <utility>
#include <algorithm>
#include <functional>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <memory.h>
#include <sstream>
#include <cassert>
#include <ctime>
#include <complex>
#include <unordered_map>
#include <unordered_set>
#include <bitset>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;
typedef pair<int64, int> pli;

const int INF = (int)(1e9+1e5);
const int64 LINF = (int64)(4e18);
const double EPS = 1e-10;
const int MOD = (int)1e9 + 7;
#define sq(x) ((x)*(x))
#define FAIL() ((*(int*)0)++)
#define y0 y00

int tnum;

string n;

void init()
{
	char buf[25];
	scanf ("%s", &buf);
	n = buf;
}

bool is_tidy(string s)
{
	char last = '0';
	for (int i = 0; i < (int)s.size(); i++)
	{
		if (last > s[i])
		{
			return false;
		}
		last = s[i];
	}
	return true;
}

void solve()
{
	init();
	if (is_tidy(n))
	{
		printf("Case #%d: %s\n", tnum, n.c_str());
		return;
	}
	n.insert(n.begin(), '0');
	string s = n;
	for (int i = (int)n.size() - 1; i >= 1; i--)
	{
		if (n[i] > n[i - 1])
		{
			string s = n;
			s[i] = s[i - 1];
			fill(s.begin() + i + 1, s.end(), '9');
			if (is_tidy(s))
			{
				for (char c = s[i] + 1; c <= '9'; c++)
				{
					s[i] = c;
					if (s > n)
					{
						s[i] = c - 1;
						break;
					}
				}
				while (!s.empty() && s[0] == '0')
				{
					s.erase(s.begin());
				}
				printf("Case #%d: %s\n", tnum, s.c_str());
				return;
			}
		}
	}
}

int main()
{
	//srand(time(0)); testgen(10, 5, 30);
    ios_base::sync_with_stdio(false); cin.tie(0);
#ifdef _MY_DEBUG
    freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
#endif

    double st = clock();
    int tests = 1;
    scanf ("%d", &tests);
    for (tnum = 1; tnum <= tests; tnum++)
    {
    	solve();
    }

    //fprintf(stderr, "%.3lf\n", (clock() - st) / CLOCKS_PER_SEC);
    return 0;
}
