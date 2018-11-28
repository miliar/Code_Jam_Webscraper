#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
	int T; cin >> T;

	for (int t = 0; t < T; t++) {
		int D, N; cin >> D >> N;
		double maxTime = 0;
		for (int i = 0; i < N; i++) {
			int K, S;
			cin >> K >> S;
			maxTime = max(maxTime, double(D - K) / S);
		}
		cout <<"Case #"<<t+1<<": "<<fixed << setprecision(7) << D / maxTime << endl;
	}

    return 0;
}

