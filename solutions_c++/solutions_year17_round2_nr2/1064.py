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


class Compare {
public:
    bool operator() (ll & first, ll & second) {
    	return first < second;
    }
};

ll nn, rr, oo, yy, gg, bb, vv;

char buffer[2000];
bool seen[2000];

priority_queue<pair<ll, char>> pq;

int main(void) {

	ll t;
	f >> t;

	for (ll tt = 1; tt <= t; tt++) {
		while (!pq.empty()) {
			pq.pop();
		}

		g << "Case #" << tt << ": ";
		f >> nn >> rr >> oo >> yy >> gg >> bb >> vv;

		for (ll i = 0; i <= nn; i++) {
			buffer[i] = '\0';
			seen[i] = 0;
		}

		pq.push(make_pair(rr, 'R'));
		pq.push(make_pair(oo, 'O'));
		pq.push(make_pair(yy, 'Y'));
		pq.push(make_pair(gg, 'G'));
		pq.push(make_pair(bb, 'B'));
		pq.push(make_pair(vv, 'V'));

		auto largest = pq.top();
		pq.pop();


		if (largest.first > nn / 2) {
			g << "IMPOSSIBLE" << e;
			continue;
		}

		ll pos = 0;
		while (largest.first) {
			buffer[pos] = largest.second;
			seen[pos] = true;
			pos += 2;
			largest.first --;
		}

		pos = 0;

		for (;;) {
			auto top = pq.top();
			pq.pop();
			auto bottom = pq.top();
			pq.pop();

			if (top.first == 0) {
				break;
			}

			while (seen[pos]) pos++;

			if (top.second == buffer[pos - 1]) {
				buffer[pos] = bottom.second;
				seen[pos] = true;
				bottom.first--;
			} else {
				buffer[pos] = top.second;
				seen[pos] = true;
				top.first--;
			}

			pq.push(top);
			pq.push(bottom);
		}

		g << buffer << e;
	}


	return 0;
}
