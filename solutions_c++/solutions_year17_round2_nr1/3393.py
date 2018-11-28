#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <float.h>

using namespace std;

int main() {
	int T; // number of tests
	cin >> T;

	for (int m = 0; m < T; m++) {
		long long int D;
		int N;
		cin >> D;
		cin >> N;

		double min_speed = FLT_MAX;
		for (int i = 0; i < N; i++) {
			long long int si;
			long long int ki;
			cin >> ki;
			cin >> si;
			// cout << "D: "<< D << " " << endl;
			// cout << "si: "<< si << " " << endl;
			// cout << "ki: "<< ki << " " << endl;
			double speed = (D * si * 1.0) / (D - ki);
			min_speed = min(min_speed, speed);
		}

		cout << "Case #" << m+1 << ": ";
		printf("%.30g\n", min_speed);

	}
}