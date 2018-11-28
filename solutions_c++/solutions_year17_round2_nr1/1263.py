#pragma warning(disable:4996)
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int K[1001];
int S[1001];

int main() {
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	int D, N;
	for (int tc = 1; tc <= T; tc++) {
		cin >> D;
		cin >> N;
		for (int i=0; i<N; i++) {
			cin >> K[i];
			cin >> S[i];
		}

		double m = 0;
		for (int i=0; i<N; i++) {
			double t = (double)(D-K[i])/S[i];
			if (t > m) {
				m=t;
			}
		}

		

		printf("Case #%d: ", tc);
			printf("%f\n", (double)D/m);
		
		

	}
	return 0;
}
