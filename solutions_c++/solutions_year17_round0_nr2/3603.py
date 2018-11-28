#include <cstdio>
#include <iostream>
#include <ctime>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <bitset>
#include <cassert>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define endl ('\n')
#define FOR(i,a,b) for (int i = (a), _b = (b); i < _b; i++)
#define CLEAR(a, n) memset(a, 0, n * sizeof(a[0]))

#define IMPOSSIBLE ("IMPOSSIBLE")

clock_t __starttime = clock();

template<class T> inline void read_vector(vector<T> &a, int n) { a.clear(); a.reserve(n); T x; FOR(i, 0, n) { fastin.readInt(x); a.push_back(x); } }

void prepare_io() {
	freopen("sample.in", "r", stdin);
	freopen("sample.out", "w", stdout);
}

int get_test_count() {
	int T;
	scanf("%d", &T);
	return T;
}

void read_input(int);
void solve(int);

int main() {
	prepare_io();
	FOR(__test, 0, get_test_count()) {
		read_input(__test + 1);
		solve(__test + 1);
	}
	clock_t __endtime = clock();
	fprintf(stderr, "execution time : %.3lf s\n", (double)(__endtime - __starttime) / CLOCKS_PER_SEC);
	return 0;
}


long long n;

void read_input(int testCaseId) {
	scanf("%lld", &n);
}

bool isTidy(long long n)
{
	int largestDigit = n % 10;
	while (n > 0)
	{
		int lastDigit = n % 10;
		if (lastDigit > largestDigit)
		{
			return false;
		}

		n /= 10;
		largestDigit = lastDigit;
	}

	return true;
}

long long solveNaive(long long n)
{
	while (!isTidy(n)) n--;
	return n;
}

void split(long long n, int *digits, int &nSize)
{
	nSize = 0;
	while (n > 0)
	{
		digits[nSize] = n % 10;
		nSize++;
		n /= 10;
	}
}

long long join(int *digits, int nSize)
{
	long long result = 0;
	for (int i = nSize - 1; i >= 0; i--)
	{
		result = 10 * result + digits[i];
	}
	return result;
}

bool ss(int *digits, int pos, int largestDigit)
{
	if (pos == -1)
	{
		return true;
	}

	if (largestDigit > digits[pos])
	{
		return false;
	}

	bool t = ss(digits, pos - 1, digits[pos]);
	if (!t)
	{
		if (digits[pos] <= largestDigit)
		{
			return false;
		}

		digits[pos]--;
		for (int i = pos - 1; i >= 0; i--)
		{
			digits[i] = 9;
		}
	}
	return true;
}

long long solveSmart(long long n)
{
	int nSize = 0;
	int digits[30];

	split(n, digits, nSize);

	ss(digits, nSize - 1, 0);

	return join(digits, nSize);
}

void solve(int testCaseId) {
	long long sol = solveSmart(n);// solveNaive(n);

	printf("Case #%d: %lld\n", testCaseId, sol);
}
