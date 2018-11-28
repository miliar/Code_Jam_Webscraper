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
#define ld long double
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

int main(void) {

	ll t;
	f >> t;

	g << fixed << setprecision(7);

	for (ll tt = 1; tt <= t; tt++) {
		g << "Case #" << tt << ": ";

		ll nn, qq;
		f >> nn >> qq;

		ll h_dist[1000];
		ll h_speed[1000];
		ld dp[1000];
		ll city_dist[1000];

		for (ll i = 1; i <= nn; i++) {
			f >> h_dist[i] >> h_speed[i];
			dp[i] = 0;
			city_dist[i] = 0;
		}

		for (ll i = 1; i <= nn; i++) {
			for (ll j = 1; j <= nn; j++) {
				ll dist;
				f >> dist;
				if (i + 1 == j) {
					city_dist[j] = dist;
				}
			}
		}

		for (ll i = 1; i <= qq; i++) {
			ll st, ed;
			f >> st >> ed;
		}

		dp[nn] = 0;
		for (ll i = nn - 1; i > 0; i--) {
			ll went = 0;
			ld bestTime = HUGE_VALL;
			auto toGo = h_dist[i];
			for (ll j = i + 1; j <= nn; j++) {
				went += city_dist[j];
				if (went > toGo) {
					break;
				}
				ld time = ((ld) went) / h_speed[i];
				if (time + dp[j] < bestTime) {
					bestTime = time + dp[j];
				}
			}

			dp[i] = bestTime;
		}

		g << dp[1] << e;
	}


	return 0;
}
