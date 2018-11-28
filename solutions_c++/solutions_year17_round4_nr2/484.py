#include <iostream>
#include <iomanip>
using namespace std;

int numtickets[1000];
int demand[1000];

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N, C, M;
		cin >> N >> C >> M;

		int rides = 0;

		for (int i = 0; i < C; i++) {
			numtickets[i] = 0;
		}
		for (int i = 0; i < N; i++) {
			demand[i] = 0;
		}
		for (int i = 0; i < M; i++) {
			int pos, cus;
			cin >> pos >> cus;
			numtickets[cus-1]++;
			demand[pos-1]++;

			if (numtickets[cus-1] > rides) {
				rides = numtickets[cus-1];
			}
		}

		int totaldemand = 0;
		for (int i = 0; i < N; i++) {
			totaldemand += demand[i];
			if ((totaldemand+i) / (i+1) > rides) {
				rides = (totaldemand+i) / (i+1);
			}
		}

		int promotions = 0;
		for (int i = 0; i < N; i++) {
			if (demand[i] > rides) {
				promotions += demand[i]-rides;
			}
		}

		cout << "Case #" << t << ": " << rides << ' ' << promotions << '\n';
	}

	return 0;
}
