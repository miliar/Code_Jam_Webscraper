#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int flip(string& S, int K) {
	int flips = 0;
			for (int s = 0; s < S.length(); ++s) {
			if (S[s] == '+') {
				continue;
			}
			if (K + s > S.length()) {
				return -1;
			}
			flips++;
			for (int k = 0; k <K ; ++k) {
				if (S[k + s]  == '+') {
					S[k + s]  = '-'	;
				} else {
					S[k + s]  = '+'	;
				}
			}

		}
		return flips;
}
int main() {
	ifstream input;
	input.open("A-large.in");

	int T, K;
	string S;
	input >> T;

	for (int t = 1; t <=T ; ++t) {
		input>>S>>K;
		int f = flip(S, K);
		cout << "Case #"<<t<<": ";
		if (f == -1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << f;
		}
		cout<<endl;

	}


	return 0;
}