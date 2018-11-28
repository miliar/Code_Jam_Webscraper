#undef MYDEBUG
#define _CRT_SECURE_NO_WARNINGS
#define TASK "B-large"
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

long long pw[19];

long long solve(long long n)
{
	long long ans = 0;

	int len = 0;
	while (n >= pw[len])
		++len;

	vector <int> d;
	long long tmp = n;
	while (tmp)
	{
		d.push_back(tmp % 10);
		tmp /= 10;
	}
	d.push_back(-1);

	bool still_good = true;
	for (int i = len - 1; i >= 0; --i)
	{
		if (d[i] < d[i + 1])
		{
			still_good = false;
			break;
		}
		if (d[i] == d[i + 1])
			continue;
		long long cur = 0;
		for (int j = len - 1; j > i; --j)
			cur += d[j] * pw[j];
		cur += (d[i] - 1)*pw[i];
		for (int j = i - 1; j >= 0; --j)
			cur += 9 * pw[j];
		ans = max(ans, cur);
	}
	if (still_good)
		ans = n;

	return ans;
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

	pw[0] = 1;
	for (int i = 1; i <= 18; ++i)
		pw[i] = 10 * pw[i - 1];
	
	int CASE;
	cin >> CASE;
	for (int TEST_ID = 1; TEST_ID <= CASE; ++TEST_ID)
	{
		long long x;
		cin >> x;
		cout << "Case #" << TEST_ID << ": " << solve(x) << "\n";
	}

	my_return(0);
}