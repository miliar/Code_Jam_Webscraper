#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int T, D, N, K, S;
	double maxtime;

	cin >> T;

    cout << fixed;
    cout << setprecision(8);

	for(int i=1 ; i<=T ; ++i) {
		cin >> D >> N;
		maxtime = 0;

		for(int x=0 ; x<N ; ++x) {
			cin >> K >> S;

			double time = (D-K);
			time /= S;
			if (time > maxtime)
				maxtime = time;
		}

		cout << "Case #" << i << ": " << ((double)D)/maxtime << endl;
	}

	return 0;
}
