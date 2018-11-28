#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

typedef unsigned long long ull;

int main(void) {
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++) {
		int N, D;
		cin >> D >> N;
		double slowest = 0;
		
		for (int c = 0; c < N; c++) {
			long long ki, si;
			cin >> ki >> si;
			double currTime = ((double)(D - ki))/(double)si;
			if ( currTime > slowest ) {
				slowest = currTime;
			}
		}
		cout << "Case #" << cc << ": ";
		cout.precision(17);
		cout << ((double)D)/slowest << endl;
	}


	return 0;
}