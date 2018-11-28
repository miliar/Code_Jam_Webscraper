#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>
#include <cstdio>
#include <numeric>
#include <cstdlib>
#include <cassert>
#include <set>
#include <ctime>
#include <stack>
#include <cstring>
#include<functional>
#include <sstream>
#include <ctype.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
#pragma comment(linker, "/STACK:16777216")
template<typename T> T fac(T a) { return a ? a*fac(a - 1) : 1; }
template<typename T> T power(T a, int p) { return !p ? 1 : (p & 1 ? a*power(a, p - 1) : power(a*a, p >> 1)); }
template<typename T> T gcd(T a, T b) { return b ? gcd(b, a%b) : a; }
template<typename T> T lcm(T a, T b) { return b / gcd(a, b) * a; }
template<typename T> T next() { T _; cin >> _; return _; }
template<> int next<int>() { int _; scanf("%d", &_); return _; }
template<> double next<double>() { double _; scanf("%lf", &_); return _; }
template<> ll next<ll>() { ll _; scanf("%lld", &_); return _; }
template<typename E> vector<E> next(int n) { vector<E> res(n); for (int i = 0; i < n; i++) res[i] = next<E>(); return res; }
template<class C, class E> int count(const C &c, const E &e) { return count(c.begin(), c.end(), e); }
template<class E> bool has(const vector<E> &c, const E &e) { return find(c.begin(), c.end(), e) != c.end(); }
template<class E> int find(const vector<E> &c, const E &e) { return find(c.begin(), c.end(), e) - c.begin(); }
template<class E> bool binary_has(const vector<E> &c, const E &e) { return binary_search(c.begin(), c.end(), e); }
template<class E> int binary_find(const vector<E> &c, const E &e) { return lower_bound(c.begin(), c.end(), e) - c.begin(); }
template<typename T> T dist2(T i1, T j1, T i2, T j2) { return (i1 - i2)*(i1 - i2) + (j1 - j2)*(j1 - j2); }
bool ok(int i, int j, int n, int m) { return 0 <= i&&i<n && 0 <= j&&j<m; }
const double EPS = 1e-9;
const double PI = acos(-1);
bool LE(double a, double b) { return b - a > -EPS; }
bool BE(double a, double b) { return a - b > -EPS; }
bool EQ(double a, double b) { return fabs(a - b) < EPS; }
bool LESS(double a, double b) { return b - a > EPS; }
bool BIGG(double a, double b) { return a - b > EPS; }

string smart(ll n)
{
	string str = to_string(n);
	while (true)
	{
		bool ok = true;
		for (int i = 0; i + 1 < str.size(); i++)
		{
			if (str[i] > str[i + 1])
			{
				ok = false;
				str[i]--;
				for (int j = i + 1; j < str.size(); j++) str[j] = '9';
				break;
			}
		}

		if (ok)
		{
			if (str[0] == '0')
				str = str.substr(1);
			return str;
		}
	}
}

string brute(ll n)
{
	for (ll s = n;; s--)
	{
		string str = to_string(s);
		bool ok = true;
		for (int i = 0; i + 1 < str.size(); i++)
		{
			if (str[i] > str[i + 1])
			{
				ok = false;
				break;
			}
		}

		if (ok) return str;
	}
}

int main()
{
	freopen("C:\\Users\\ibismail\\Downloads\\B-large.in", "r", stdin);
	freopen("C:\\Users\\ibismail\\Downloads\\codejam\\out.txt", "w", stdout);

	int t = next<int>();

	for (int test = 1; test <= t; test++)
	{
		cout << "Case #" << test << ": " << smart(next<ll>()) << endl;
	}


	return 0;
}