#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

map<ll, ll> s;

void solve(int test)
{
	printf("Case #%d: ", test + 1);

	ll n, k; cin >> n >> k;

	s.clear();
	s[n] = 1;

	ll len1;
	ll len2;

	while (k > 0)
	{
		map<ll, ll>:: iterator iter = s.end();
		iter--;
		pair<ll, ll> p = (*iter);
		s.erase(iter);
		len1 = (p.first - 1) / 2;
		len2 = p.first / 2;
		k -= p.second;
		s[len1] += p.second;
		s[len2] += p.second;
	}

	cout << len2 << " " << len1 << endl;
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc; cin >> tc;
	forn(it, tc) solve(it);

	return 0;
}
