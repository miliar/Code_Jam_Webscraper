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
		f >> n;

		string s = to_string(n);

		bool redo = true;
		while (redo) {
			redo = false;
			for (ll i = 1; i < s.length(); i++) {
				if (s[i] < s[i - 1]) {
					for (ll j = i; j < s.length(); j++) {
						s[j] = '9';
					}
					s[i - 1]--;
					redo = true;
					break;
				}
			}
		}

		ll res;
		istringstream (s) >> res;

		g << "Case #" << tt << ": " << res << e;

	}

	return 0;
}
