#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int position[1000];
int speed[1000];

int main() {
	int T;
	cin >> T;
	for (int iCase = 1; iCase <= T; iCase++) {
		int D, N;
		cin >> D >> N;
		for (int i = 0; i < N; i++)
			cin >> position[i] >> speed[i];
		
		double maxTime = (1.0*D - position[0]) / speed[0];
		for (int i = 1; i < N; i++) {
			double time = (1.0*D - position[i]) / speed[i];
			if (time > maxTime)
				maxTime = time;
		}
		
		cout << "Case #" << iCase << ": ";
		printf("%.6lf\n", D / maxTime);
	}
}
