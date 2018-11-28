#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int main() {
	int T, happy = 0, blank = 0 , counter = 0, K;
	string S;
	ifstream infile("A-large.in");
	ofstream outfile("testout.txt");

	infile >> T;
	for (int t = 0; t < T; t++) { //for every test case
		outfile << "Case #" << t + 1 << ": ";

		counter = 0;
		happy = 0;
		blank = 0;
		infile >> S;
		infile >> K;
		while (S.length() > 0){
			//cout << S << endl;
			if (K > S.length()) break;
			if (S[0] == '+') {
					S.erase(0, 1); //delete + from list
					continue;
				}
			else {
				counter++;
				for (int j = 0; j < K; j++) {
					if (S[j] == '-') S[j] = '+';
					else S[j] = '-';
				}
			}
		}
		//cout << "************" << endl;
		for (char& c : S) {
			if (c == '+') happy++;
			else blank++;
		}
		if (blank == 0) outfile << counter << "\n";
		else outfile << "IMPOSSIBLE" << "\n";
	}
	return 0;
}

