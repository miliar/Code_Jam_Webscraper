#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;
typedef unsigned long long ull;
typedef pair<ull,double> pld;

void solve() {
	int d,n;
	cin >> d >> n;
	pld horses[1010];
	for (int i=0; i<n; ++i) {
		cin >> horses[i].first >> horses[i].second;
	}
	double minSpeed = 0;
	double maxSpeed = 1.0e18L;
	for (int iter=0; iter<1000; ++iter) {
		bool okay = true;
		double speed = (maxSpeed + minSpeed) / 2;
		for (int i=0; i<n; ++i) {
			pld h = horses[i];
			if (d / speed < (d-h.first)/h.second) okay = false;
		}
		if (okay) {
			minSpeed = speed;
		} else {
			maxSpeed = speed;
		}
	}
	cout << setprecision (18) << minSpeed << endl;
}

int main() {
	int cases;
	cin >> cases;
	for (int i=1; i<=cases; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
