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

void assert(bool b)
{
	if (!b)
		throw 0;
}

pair<ll, ll> pick(map<ll, ll> &mp, ll k)
{
	auto it = mp.end();
	--it;
	if (it->second > k)
	{
		it->second -= k;
		return {it->first, k};
	}

	auto result = *it;
	mp.erase(it);
	return result;
}

int main()
{
	ios::sync_with_stdio(false);

#ifdef _MSC_VER
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#else
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#endif
	
	readt;
	fort
	{
		ll n, k;
		read n >> k;
		--k;

		map<ll, ll> mp;
		mp[n] = 1;

		while (k > 0)
		{
			auto v = pick(mp, k);
			k -= v.second;
			--v.first;
			mp[v.first / 2] += v.second;
			mp[(v.first + 1) / 2] += v.second;
		}

		auto v = pick(mp, 1);
		--v.first;

		write "Case #" << gett << ": ";
		write ((v.first + 1) / 2) << " " << (v.first / 2);
		writeln;
	}

	return 0;
}