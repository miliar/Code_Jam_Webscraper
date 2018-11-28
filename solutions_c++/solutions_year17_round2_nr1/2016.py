#include<iostream>
#include<string>
#include<iomanip>
using namespace std;

struct HORSE {
	int K = 0;
	int S = 0;
	double time = 0;
};

int main() {
	double output[100];
	int T = 0;
	cin >> T;
	for (int j = 0; j < T; j++) {
		int D = 0, N = 0;
		double longest = 0;
		cin >> D;
		cin >> N;
		getchar();
		HORSE *H;
		H = new HORSE[N];
		for (int i = 0; i < N; i++) {
			cin >> H[i].K;
			cin >> H[i].S;

			H[i].time = (double)(D - H[i].K) / (double)H[i].S;

			if (H[i].time > longest) {
				longest = H[i].time;

			}
		}
		output[j] = D / longest;
		delete [] H;
	}
	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		cout << fixed << setprecision(6) << output[i] << "\n";
	}

	getchar();
	getchar();
	return 0;
}