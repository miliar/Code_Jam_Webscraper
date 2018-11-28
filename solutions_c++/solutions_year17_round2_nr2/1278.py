#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<map>

using namespace std;

struct nc {
	int number;
	char color;
};

bool operator<(const nc& left, const nc& right) {
	return left.number < right.number;
}

int main(void) {
	ifstream ifs("B-small-attempt1.in");
	ofstream ofs("out.txt");

	int T;
	ifs >> T;

	for (int t = 1; t <= T; t++) {
		int N, R, O, Y, G, B, V;
		ifs >> N >> R >> O >> Y >> G >> B >> V;
		vector<nc> snc(3);
		snc[0].color = 'R';
		snc[0].number = R;
		snc[1].color = 'Y';
		snc[1].number = Y;
		snc[2].color = 'B';
		snc[2].number = B;

		sort(snc.begin(), snc.end());

		if (snc[2].number > snc[0].number + snc[1].number) {
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
			ofs << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
			continue;
		}

		vector<int> ans(N);
		if (N % 2 == 0) {
			for (int i = 0; i < N; i += 2) {
				if (snc[2].number > 0) {
					ans[i] = 2;
					snc[2].number--;
				}
				else {
					ans[i] = 1;
					snc[1].number--;
				}
			}
			for (int i = 1; i < N; i += 2) {
				if (snc[1].number > 0) {
					ans[i] = 1;
					snc[1].number--;
				}
				else {
					ans[i] = 0;
					snc[0].number--;
				}
			}
		}
		else {
			ans[0] = 2;
			ans[1] = 1;
			ans[2] = 0;
			for (int i = 0; i < 3; i++) snc[i].number--;
			for (int i = 3; i < N; i += 2) {
				if (snc[2].number > 0) {
					ans[i] = 2;
					snc[2].number--;
				}
				else {
					ans[i] = 1;
					snc[1].number--;
				}
			}
			for (int i = 4; i < N; i += 2) {
				if (snc[1].number > 0) {
					ans[i] = 1;
					snc[1].number--;
				}
				else {
					ans[i] = 0;
					snc[0].number--;
				}
			}
		}

		string ans_string;
		for (int i = 0; i < N; i++) {
			ans_string.push_back(snc[ans[i]].color);
		}

		cout << "Case #" << t << ": " << ans_string << endl;
		ofs << "Case #" << t << ": " << ans_string << endl;
	}

	system("pause");
	return 0;
}