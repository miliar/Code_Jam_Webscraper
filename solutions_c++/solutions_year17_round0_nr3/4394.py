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

struct Range {
	ll size;
	ll left;
	ll right;

	Range(ll size_, ll left_, ll right_) {
		size = size_;
		left = left_;
		right = right_;
	}
};


class Compare {
public:
    bool operator() (Range & first, Range & second) {
		if (first.size != second.size) {
			return first.size < second.size;
		}

		return first.left < second.left;
    }
};

priority_queue<Range, vector<Range>, Compare> pq;

int main(void) {

	f >> t;

	for (ll tt = 1; tt <= t; tt++) {
		f >> n >> k;

		while (!pq.empty()) {
			pq.pop();
		}
		pq.push(Range(n, 1, n));


		for (ll i = 1; i < k; i++) {
			Range newRange = pq.top();
			pq.pop();

			ll chosenSeat = (newRange.left + newRange.right) / 2;

			Range range1 = Range((chosenSeat - newRange.left), newRange.left, chosenSeat - 1);
			Range range2 = Range((newRange.right - chosenSeat), chosenSeat + 1, newRange.right);

//			g << range1.size << " " << range1.left << " " << range1.right << e;
//			g << range2.size << " " << range2.left << " " << range2.right << e;
			pq.push(range1);
			pq.push(range2);
		}

		Range lastRange = pq.top();
//		g << lastRange.size << " " << lastRange.left << " " << lastRange.right << e;
		pq.pop();
		ll rangeSize = lastRange.size;
		ll small = 0;
		ll large = 0;
		if ((rangeSize - 1 ) % 2 == 0) {
			small = large = (rangeSize - 1) / 2;
		} else {
			small = (rangeSize - 1) / 2;
			large = small + 1;
		}
		g << "Case #" << tt << ": " << large << " " << small << e;

	}

	return 0;
}
