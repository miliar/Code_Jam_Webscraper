#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long ll;
typedef long double ld;

struct pancake {
	ll a, b;
	//a = 2 * radius * height
	//b = radius^2
	pancake(): a(0), b(0) {}
	pancake(ll r, ll h) : a(2*r*h), b(r*r) {}
	bool operator < (const pancake& p) const {
		return a > p.a || (a == p.a && b > p.b);
	}
};

typedef vector<pancake> vp;

//n = number of pancakes.
//k = parameter
//finds set I for size k that maximizes: \sum_{i \in I} a_i + \max_{i \in I} b_i.
ll maximize(vp& pancakes, int n, int k) {
	sort(pancakes.begin(), pancakes.end());
	ll sum = 0, maxB = 0;
	for(int i = 0;i < k-1; ++i) {
		sum += pancakes[i].a;
		if(pancakes[i].b > maxB) {
			maxB = pancakes[i].b;
		}
	}
	ll bestAddition = 0;
	for(int i = k-1;i < n; ++i) {
		ll add = pancakes[i].a;
		if(pancakes[i].b > maxB) {
			add += pancakes[i].b - maxB;
		}
		if(add > bestAddition) {
			bestAddition = add;
		}
	}
	return sum + maxB + bestAddition;
}

ld pi = atan(1)*4;

ld solve() {
	int n,k;
	cin >> n >> k;
	vp pancakes(n);
	for(int i = 0;i < n; ++i) {
		ll r, h;
		cin >> r >> h;
		pancakes[i] = pancake(r,h);
	}
	return pi * maximize(pancakes, n, k);
}

int main() {
	cout << fixed << setprecision(10);
	int T;
	cin >> T;
	for(int t = 1;t <= T; ++t) {
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}