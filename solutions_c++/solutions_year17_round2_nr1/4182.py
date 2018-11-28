
// Author: Tiago Togores

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define SZ(a) ((int)((a).size()))
#define ALL(a) (a).begin(), (a).end()
#define CLR(a, x) memset(a, x, sizeof a)
#define REP(i, n) for (auto i = 0; i < (n); i++)
#define FORT(it, l) for (auto it = (l).begin(); it != (l).end(); it++)
#define READLINE(line) cin.getline((line), sizeof (line))
#define VALID(i, j, n, m) (0 <= (i) && (i) < (n) && 0 <= (j) && (j) < (m))
#define PI M_PI
#define EPSILON 1e-6
#define INF 1000000000
#define MOD 1000000007
#define endl '\n'
//NOTE: append ll to name if using long long
#define BITCOUNT __builtin_popcount
#define BITLEAD0 __builtin_clz
#define BITTRAIL0 __builtin_ctz
#define BITPARITY __builtin_parity

typedef unsigned int uint;
typedef long long int int64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;

///////////////////////////////

int debugging = 0;

void init()
{
	cout.precision(6);
}

int should_debug(int tc)
{
	return 0;
}

#define N 1010
double y[N], v[N], k[N], s[N];

void solve(int tc)
{
	int n;
	double d;
	cin >> d >> n;
	REP (i, n)
	{
		cin >> k[i + 1] >> s[i + 1];
	}

	for (int i = n; i >= 1; --i)
	{
		int m = i;
		for (int j = i - 1; j >= 1; --j)
		{
			if (k[j] > k[i])
			{
				m = j;
			}
		}
		swap(k[i], k[m]);
		swap(s[i], s[m]);
	}

	y[n] = d;
	v[n] = s[n];
	if (debugging)
	{
		cout << n << ' ' << k[n] << ' ' << s[n] << ' ' << y[n] << ' ' << v[n] << endl;
	}
	for (int i = n - 1; i >= 1; --i)
	{
		if (s[i] <= s[i + 1])
		{
			y[i] = d;
		}
		else
		{		
			double x = (s[i + 1]*k[i] - s[i]*k[i + 1])/(s[i + 1] - s[i]);
			if (x > y[i + 1])
			{
				y[i] = y[i + 1];
			}
			else
			{
				y[i] = x;
			}
		}
		double t = (y[i] - k[i])/s[i] + (d - y[i])/s[i + 1];
		v[i] = (d - k[i])/t;
		if (debugging)
		{
			cout << i << ' ' << k[i] << ' ' << s[i] << ' ' << y[i] << ' ' << v[i] << endl;
		}
	}
	double t = (d - k[1])/v[1];
	v[0] = d/t;

	cout << fixed << v[0];
}

int main()
{ _
	init();
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		if (should_debug(tc))
		{
			debugging = 1;
		}
		cout << "Case #" << tc << ": ";
		if (debugging)
		{
			cout << endl;
		}
		solve(tc);
		cout << endl;
		debugging = 0;
	}
	return 0;
}
