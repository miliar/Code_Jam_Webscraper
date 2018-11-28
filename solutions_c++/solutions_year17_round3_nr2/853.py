#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<string>
#include<limits.h>
#include<fstream>

using namespace std;

int main(void) {
	ifstream ifs("B-small-attempt1 (1).in");
	ofstream ofs("out.txt");

	int T;
	ifs >> T;

	for (int t = 1; t <= T; t++) {
		int A_C, A_J;
		ifs >> A_C >> A_J;
		if (A_C < A_J) swap(A_C, A_J);

		if (A_C + A_J > 2) exit(0);

		int ans;
		if (A_C == 1) {
			ans = 2;
			int dummy;
			for (int i = 0; i < 2 * (A_C + A_J); i++) ifs >> dummy;
		} else {
			vector<int> C(2), D(2);
			for (int i = 0; i < 2; i++) {
				ifs >> C[i] >> D[i];
			}
			if (C[0] > C[1]) {
				swap(C[0], C[1]);
				swap(D[0], D[1]);
			}
			if (min(D[1] - C[0], D[0] + 1440 - C[1]) > 720) ans = 4;
			else ans = 2;
		}

		cout << "Case #" << t << ": " << ans << endl;
		ofs << "Case #" << t << ": " << ans << endl;
	}

	system("pause");
	return 0;
}