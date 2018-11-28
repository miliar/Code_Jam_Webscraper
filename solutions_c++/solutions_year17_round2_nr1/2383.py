#include <stdio.h>
#include <iostream>
#include <stack>
#include <queue>
#include <set>
#include <algorithm>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

int T;
int main() {
	freopen("c:\\users\\ahsalam\\documents\\gcj\\round_b\\A-large (1).in", "r", stdin);
	freopen("c:\\users\\ahsalam\\documents\\gcj\\round_b\\a-large.out", "w", stdout);

	cin >> T;
	for (int t = 1; t <= T; t++) {
		int D, N;
		cin >> D >> N;

		long double slowest_time = 0;
		for (int i = 0; i < N; i++) {
			int K, S;
			cin >> K >> S;

			long double time = 1.0 * (D - K) / S;
			slowest_time = max(slowest_time, time);
		}

		long double speed = D / slowest_time;
		//cout << "Case #" << t << ": " << ": " << speed << endl;
		printf("Case #%d: %.8Lf\n", t, speed);
	}

	return 0;
}