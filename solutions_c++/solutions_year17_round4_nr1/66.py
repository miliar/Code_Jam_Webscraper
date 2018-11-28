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

struct state
{
	int c[4];
	int code()
	{
		return ((((0 + c[0]) * 128 + c[1]) * 128 + c[2]) * 128 + c[3]);
	}
};

int mod;

int add_mod(int x, int y)
{
	return (x + y) % mod;
}

int cache[128 * 128 * 128 * 128];

int solve(int sum, state& s)
{
	if (cache[s.code()] != -1)
		return cache[s.code()];

	int ans = 10005000;
	fori(mod)
		if (s.c[i])
		{
			--s.c[i];
			int test = solve(add_mod(sum, i), s);
			ans = min(ans, test);
			++s.c[i];
		}

	if (ans == 10005000)
		ans = 0;
	else if (sum != 0)
		++ans;

	return cache[s.code()] = ans;
}


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
		int n, p;
		read n >> p;
		vi v(n);
		forin read v[i];
		
		::mod = p;

		state s;
		s.c[0] = s.c[1] = s.c[2] = s.c[3] = 0;
		forin ++s.c[v[i] % mod];

		memset(cache, -1, sizeof(cache));
	
		write "Case #" << gett << ": " << (n - solve(0, s));
		writeln;
	}

	return 0;
}