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
		int n, c, m;
		read n >> c >> m;
		vi sit_count(n);
		vi buyer_count(c);
		fori(m)
		{
			int p, b;
			read p >> b;
			++sit_count[p - 1];
			++buyer_count[b - 1];
		}
		
		int ans = *max_element(all(buyer_count)) - 1;
		for (int step = 1 << 30; step > 0; step /= 2)
		{
			int test = ans + step;
			int left = 0;
			for (int i = n - 1; i >= 0; i--)
			{
				left += sit_count[i];
				left -= min(left, test);
			}
			if (left > 0)
				ans = test;
		}
		++ans;

		int ans2 = 0;
		forin if (sit_count[i] > ans) ans2 += sit_count[i] - ans;

		write "Case #" << gett << ": " << ans << ' ' << ans2;
		writeln;
	}

	return 0;
}