#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <assert.h>
#include <set>

using namespace std;

int main(void) {
	int num_test;
	cin>>num_test;
	
	for (int test=1; test<=num_test; test++) {
		int N, P;
		cin >> N >> P;
		
		vector <int> G(N);
		
		for (int i=0; i<N; i++) cin >> G[i];
		
		vector <int> R(P, 0);
		for (int a : G) R[a%P]++;
		
		int number = 0;

		number += R[0];
		R[0] = 0;
		
		const int opposite = (P-1)%P;
		
		if (P>2) {
			int K = min(R[1], R[opposite]);
			R[1] -= K;
			R[opposite] -= K;
			number += K;
		}
		
		if (P==3) {
			assert(R[1] * R[2] == 0);
			int K = (R[1] + R[2]) / 3;
			if (R[1] > 0) R[1] -= K*3;
			else R[2] -= K*3;
			assert(R[1] >= 0);
			assert(R[2] >= 0);
			number += K;
		}
		if (P==4) {
			int K = (R[1] + R[3]) /2;
			if (R[1] > 0) R[1] -= K*2;
			else R[3] -= K*2;
			R[2] += K;
		}
		
		if (P %2 == 0) {
			const int middle = P/2;
			int K = R[middle] / 2;
			number += K;
			R[middle] -= K * 2;
		}
		for (int i=0; i<P; i++) cerr << R[i] <<"\t";
		cerr << "\n";
		if (accumulate(R.begin(), R.end(), 0) > 0) number++;
		
		cout<<"Case #"<<test<<": " << number << "\n";
		
	}
	return 0;
}
