#define _USE_MATH_DEFINES
#include <algorithm>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <limits.h>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>

#ifdef SpOleM98
#include <conio.h>
#endif 

using namespace std;

#pragma warning(disable:4996)
#pragma comment(linker, "/STACK:256000000")

#define endl '\n'
#define MIN(a, b) ((a)<(b)) ? (a) : (b)
#define MAX(a, b) ((a)>(b)) ? (a) : (b)
#define I (int)
#define LL long long
#define LD long double
#define U unsigned
#define X first
#define Y second
#define PB push_back
#define MP make_pair

FILE* stream;

const int INF = 1e9 + 7;
const LL INFL = (LL)1e18 + 1;
const int SIZE = 2e5 + 10;
const int TSIZE = 1e3 + 10;
const LD eps = 0.000001;
const long long MOD = 1e9 + 7;

char POW(char a, char b)
{
	if (b == 0)
		return 1;
	char cur = POW(a, b / 2);
	if (b % 2 == 0)
		return cur * cur;
	else
		return cur * cur * a;
}

LL gcd(LL &x, LL &y, LL a, LL b)
{
	if (a == 0)
	{
		y = 1;
		x = 0;
		return abs(b);
	}
	long long x1 = 0, y1 = 0;
	long long d = gcd(x1, y1, b % a, a);
	x = y1 - (b / a) * x1;
	y = x1;
	return d;
}

LL gcd(LL a, LL b)
{
	if (a == 0)
	{
		return abs(b);
	}
	LL d = gcd(b % a, a);
	return d;
}
bool cmp(pair<int, int> a, pair<int, int> b) {

	return (LL)a.first * b.second > (LL)a.second * b.first;
}

void accept()
{
	int n, k;
	long long ans = 0;
	cin >> n >> k;
	vector <pair<long long, long long> > a; 
	for (int i = 0; i < n; i++)
	{
		long long x, y;
		cin >> x >> y;
		a.push_back(MP(-x, -y));
	}
	sort(a.begin(), a.end());
	vector < vector< long long > > dp(k + 1);
	for (int i = 0; i <= k; i++)
	{
		dp[i].resize(n);
	}
	for (int i = 0; i < n; i++)
	{
		dp[1][i] = a[i].first * a[i].first + 2 * a[i].first * a[i].second;
	}
	for (int i = 2; i <= k; i++)
	{
		for (int j = i - 1; j < n; j++)
		{
			for (int l = i - 2; l < j; l++)
			{
				if (dp[i][j] < dp[i - 1][l] + 2 * a[j].second * a[j].first)
				{
					dp[i][j] = dp[i - 1][l] + 2 * a[j].second * a[j].first;
				}
			}
		}
	}
	for (int i = 0; i < n; i++)
	{
		ans = max(ans, dp[k][i]);
	}
	long double answer = ans * M_PI;
	cout << fixed << setprecision(10) << answer << endl;

}

void solution()
{
	long long t = 1;
	cin >> t;
	for (long long i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		accept();
	}
	return;
}

void test()
{
	//freopen("input.txt", "w", stdout);
	cout << "100000\n";
	for (int k = 0; k < 100000 - 1; k++)
	{
		cout << k + 1 << " ";
	}
	cout << "100000\n";
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

#ifdef SpOleM98

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	double beg = clock();
#endif 
	srand(time(0));

	solution();
	//test();

#ifdef SpOleM98
	double end = clock();
	fprintf(stderr, "\n*** Total time = %.3f ***\n", (end - beg) / CLOCKS_PER_SEC);
	getch();
#endif
	return 0;
}