#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {

	ifstream fin("A-large.in");
	ofstream fout("A-large.out");	

	int T;
	fin >> T;

	for (int c = 0; c < T; ++c) {
		string S;
		int K;

		fin >> S;
		fin >> K;

		const int cakes = S.size();

		int totalFlips = 0;

		for (int i = 0; i < cakes; ++i) { // loop through all cakes
			if ((i + K) <= cakes && S[i] == '-') { // not near the end
				for (int f = 0; f < K; ++f) // flip
					S[i + f] = (S[i + f] == '-') ? '+' : '-';
				++totalFlips;
			}
			else if ((i + K) > cakes && S[i] == '-') {
				fout << "Case #" << (c + 1) << ": IMPOSSIBLE" << endl;
				totalFlips = -1;
				break;
			}
		}
		
		if (totalFlips >= 0)
			fout << "Case #" << (c + 1) << ": " << totalFlips << endl;
	}

	fin.close();
	fout.close();

	return 0;
}