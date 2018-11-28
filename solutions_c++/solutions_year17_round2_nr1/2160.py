#include <iostream>
#include <cstdio>
#include <iomanip>
using namespace std;

int main() {
	int TC; cin >> TC;
	double D, N, lastS, lastK, K, S; 
	int cont = 0;
	while (TC --) {
		cont++;
		cin >> D >> N;
		cin >> lastK >> lastS;
		for (int i = 1; i < N; i++) {
			cin >> K >> S;
			lastS = min(((D - K)*lastS)/(D - lastK), S);
			lastK = K;
		}

		lastS = D*lastS/(D - lastK);
		printf("Case #%d: %.6f\n",cont, lastS);
	}


}