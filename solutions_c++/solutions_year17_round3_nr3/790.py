#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cassert>
using namespace std;

int main() {
	int N, K;
	double a[50], U;
  int tt;
  cin >> tt;
  for (int tcas = 1; tcas <= tt; tcas++) {
		cin >> N >> K >> U;
		for(int j = 0; j < N; ++j)
			cin >> a[j];
		double l = 0, r = 1;
		for(int t = 0; t < 60; ++t) {
			double m = (l + r) * 0.5, s = 0;
			for(int j = 0; j < N; ++j)
				s += max(m - a[j], 0.0);
			if(s > U) r = m; else l = m;
		}
		double ans = 1;
		for(int j = 0; j < N; ++j)
			ans *= max(l, a[j]);
		printf("Case #%d: %.8f\n", tcas, ans);
	}
}
