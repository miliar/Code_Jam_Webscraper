#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define e '\n'
#define INF 1023456789
#define ll long long
#define ull unsigned long long

#define gg(x) cerr << #x << ": " << x << endl;

//#define FILE "data"

#ifdef FILE
ifstream f(string (string(FILE) + ".in").c_str());
ofstream g(string (string(FILE) + ".out").c_str());
#endif
#ifndef FILE
#define f cin
#define g cout
#endif

#ifdef CLION
#undef f
#undef g
ifstream f("data.in");
#define g cout
#endif

ll mul_inv(ll a, ll b) {
  ll b0 = b, t, q;
  ll x0 = 0, x1 = 1;
  if (b == 1) return 1;
  while (a > 1) {
    q = a / b;
    t = b, b = a % b, a = t;
    t = x0, x0 = x1 - q * x0, x1 = t;
  }
  if (x1 < 0) x1 += b0;
  return x1;
}

ll a, b, c, m, n, t, k;
string s;

int main(void) {

	f >> t;

	for (ll tt = 1; tt <= t; tt++) {
		f >> s >> k;
		ll m = s.length();
		bool possible = true;
		ll turns = 0;
		for (ll i = 0; i < m; i++) {
			if (s[i] == '+') {
				continue;
			}

			turns++;

			if (i + k > m) {
				possible = false;
				break;
			}

			for (ll j = i; j < i + k; j++) {
				if (s[j] == '-') {
					s[j] = '+';
				} else {
					s[j] = '-';
				}
			}
		}

		g << "Case #" << tt << ": ";
		if (!possible) {
			g << "IMPOSSIBLE" << e;
		} else {
			g << turns << e;
		}

	}

	return 0;
}
