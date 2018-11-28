#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
#include<iomanip>

using namespace std;

int main(void) {
	ifstream ifs("A-large.in");
	ofstream ofs("out.txt");

	int T;
	ifs >> T;
	
	for (int t = 1; t <= T; t++) {
		int D, N;
		ifs >> D >> N;

		double max_time = 0.0;
		for (int i = 0; i < N; i++) {
			int K, S;
			ifs >> K >> S;
			max_time = max(max_time, (double)(D - K) / S);
		}
		cout<< "Case #" << t << ": " << fixed << setprecision(10) << D / max_time << endl;
		ofs << "Case #" << t << ": " << fixed << setprecision(10) << D / max_time << endl;
	}

	system("pause");
	return 0;
}