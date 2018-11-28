#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;
const int Mn = 1000 + 10;
const double eps = 1e-8;
int D,N,T;
int S[Mn], K[Mn];
inline int dcmp(double x) {
	return x < -eps ? -1 : x > eps;
}
inline bool check(double v) {
	for(int i = 1; i <= N; ++i) {
		if(S[i] > v){
			continue;
		}
		if(1. * K[i] / (v - S[i]) * v < D) {
			return false;
		}
	}
	return true;
}
int main() {
	cin >> T;
	for(int cas = 1; cas <= T; ++cas) {
		cin >> D >> N;
		for (int i = 1; i <= N; ++i) {
			cin >> K[i] >> S[i];
		}
		double l = 0, r = 1e16 + 10;
		for(int tim = 1; tim <= 100; ++tim) {
			double mid = (l + r) / 2;
			if(check(mid)) {
				l = mid;
			} else {
				r = mid;
			}
		}
		printf("Case #%d: %.10f\n",cas,l);
	}

	return 0;
}