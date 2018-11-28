#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(void) {
	int T;
	ifstream inputfile("A-large.in");
	ofstream outputfile("out.txt");

	inputfile >> T;

	for (int t = 1; t <= T; t++) {
		int K;
		int ans = 0;
		string S;

		inputfile >> S >> K;

		for (int i = 0; i + K <= S.size(); i++) {
			if (S[i] == '-') {
				ans++;
				for (int j = 0; j < K; j++) {
					if (S[i + j] == '-') S[i + j] = '+';
					else S[i + j] = '-';
				}
			}
		}

		int i;
		for (i = 0; i < S.size(); i++) {
			if (S[i] != '+') break;
		}

		outputfile << "Case #" << t << ": ";
		if (i >= S.size()) outputfile << ans << endl;
		else outputfile << "IMPOSSIBLE" << endl;
	}

	return 0;
}