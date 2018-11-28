#undef MYDEBUG
#define _CRT_SECURE_NO_WARNINGS
#define TASK "A-large"
#pragma comment(linker, "/STACK:671088640")
#include <stdio.h>
#include <iostream>
#include <iomanip> 
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <functional>
#include <assert.h>
#include <bitset>
#include <unordered_set>
#include <unordered_map>
#include <random>
#include <complex>
using namespace std;

const int MOD = 786433;
const int INF = 1000000000;
const long double EPS = 1e-7;
const int HASH_POW = 29;
const long double PI = acos(-1.0);
mt19937_64 rnd(1);

double workTime()
{
	return double(clock()) / CLOCKS_PER_SEC;
}

void my_return(int code)
{
#ifdef MYDEBUG
	cout << "\nTime = " << fixed << setprecision(3) << workTime() << endl;
#endif
	exit(code);
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
#ifdef MYDEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen(TASK".in", "r", stdin);
	freopen(TASK".out", "w", stdout);
	/*freopen("pie_progress.txt", "r", stdin);
	freopen("pie_progress_output.txt", "w", stdout);*/
#endif

	int CASE;
	cin >> CASE;
	for (int TEST_ID = 1; TEST_ID <= CASE; ++TEST_ID)
	{
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		for (int i = 0; i + k - 1 < s.length(); ++i)
		{
			if (s[i] == '-')
			{
				++ans;
				for (int j = 0; j < k; ++j)
				{
					if (s[i + j] == '+')
						s[i + j] = '-';
					else
						s[i + j] = '+';
				}
			}
		}
		cout << "Case #" << TEST_ID << ": ";
		if (s.find("-") != s.npos)
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << "\n";
	}

	my_return(0);
}