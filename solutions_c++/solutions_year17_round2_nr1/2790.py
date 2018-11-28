#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "iostream"
#include "assert.h"
using namespace std;
typedef long long i64;

int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		int D, N;
		cin >> D >> N;

		double maxT = 0.0;
		for (int i=0;i<N;++i) {
			int K, S;
			cin >> K >> S;
			double t = (double)(D - K) / S;
			if (maxT < t) maxT = t;
		}
		
		printf("Case #%d: %06f\n", Ti, D / maxT);
	}
	return 0;
}
