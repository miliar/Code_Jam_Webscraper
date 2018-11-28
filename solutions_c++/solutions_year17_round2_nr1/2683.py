#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <stdio.h>

using namespace std;

int main() {
	int T;
	double D;
	cin >> T;
	for (int i=0; i<T; ++i) {
		int N;
		cin >> D >> N;
		set<double> T;
		for (int j=0; j<N; ++j) {
			double K_, S_, T_;
			cin >> K_ >> S_;
			T.insert((D - K_) / S_);
		}
		double max_T = *T.rbegin();
		//cout << "Case #" << (i+1) << ": " << (D / max_T) << endl;
		printf("Case #%d: %f\n", i+1, D/max_T);
	}
}
