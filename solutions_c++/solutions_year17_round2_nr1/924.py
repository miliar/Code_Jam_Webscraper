#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		int D, N;
		cin >> D >> N;
		double m = 0.0;
		for (int i = 0; i < N; i++) {
			int K, S;
			cin >> K >> S;
			m = max(m,1.0*(D - K) / S);
		}
		printf("%.10f\n", D/m);
	}
	return 0;
}
