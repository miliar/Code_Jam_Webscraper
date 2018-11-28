#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <ctime>
#include <bitset>
#include <random>
using namespace std;

#pragma comment(linker, "/stack:64000000")

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

typedef vector<int> vi;
typedef vector<pair<int, int > > vii;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<ld> vld;

typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef vector<vll> vvll;
typedef vector<vs> vvs;

typedef map<int, int> mpii;
typedef map<int, string> mpis;
typedef map<string, int> mpsi;
typedef map<string, string> mpss;

#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define sz(a) (int)((a).size())
#define len(a) (int)((a).length())

#define forr(i,n) for (int i = 0; i < (n); ++i)
#define fori(n) forr(i,n)
#define forj(n) forr(j,n)
#define fork(n) forr(k,n)
#define forin fori(n)
#define forjn forj(n)
#define forjm forj(m)
#define forkm fork(m)
#define foria(a) fori(sz(a))
#define foriv foria(v)
#define foris fori(len(s))
#define forja(a) forj(sz(a))
#define forjv forj(v)
#define forjs forj(len(s))

#define read cin>>
#define write cout<<
#define writeln write endl

#define readt int aaa; read aaa;
#define gett (bbb+1)
#define fort forr(bbb,aaa)


ld dis(ld x, ld y) { return sqrt(x*x + y*y); }
const ld PI = acos(ld(0.0)) * 2;

ll gcd(ll a, ll b) { return b ? gcd(b, a%b) : a; }


struct cake_type
{
	ld h;
	ld r;
	ld edge()
	{
		return 2 * PI * r * h;
	}
	ld top()
	{
		return PI * r * r;
	}
};

int dp[2][750][750];

int main()
{
	ios::sync_with_stdio(false);

#ifdef _MSC_VER
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#else
#endif

	cout.setf(ios::fixed);
	cout.precision(20);

	readt;
	fort
	{
		int n1, n2;
		read n1 >> n2;

		vi banned1(1441, 0), banned2(1441, 0);

		fori(n1)
		{
			int f, t;
			read f;
			read t;
			for (int j = f; j < t; j++)
				banned1[j] = 1;
		}

		fori(n2)
		{
			int f, t;
			read f;
			read t;
			for (int j = f; j < t; j++)
				banned2[j] = 1;
		}

		int ans = 10000000;

		fork(2)
		{
			fori(730) forj(730) dp[0][i][j] = dp[1][i][j] = 10000000;
			dp[k][720][720] = 0;

			for (int i = 720; i >= 0; i--)
				for (int j = 720; j >= 0; j--)
				{
					int t = i + j;
					if (!banned1[t])
						dp[0][i][j] = min(dp[0][i][j], dp[0][i + 1][j]);
					if (!banned1[t])
						dp[1][i][j] = min(dp[1][i][j], dp[0][i + 1][j] + 1);

					if (!banned2[t])
						dp[1][i][j] = min(dp[1][i][j], dp[1][i][j + 1]);
					if (!banned2[t])
						dp[0][i][j] = min(dp[0][i][j], dp[1][i][j + 1] + 1);
				}

			ans = min(ans, dp[k][0][0]);
			ans = min(ans, dp[1-k][0][0] + 1);
		}

		write "Case #" << gett << ": " << ans;
		writeln;
	}

	return 0;
}