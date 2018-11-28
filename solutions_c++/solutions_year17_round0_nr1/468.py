#include<iostream>
#include<fstream>
#include<vector>
#include<string>

using namespace std;

class Solver {
public:
	Solver(ifstream& ifs, ofstream& ofs) {
		string S;
		int K;

		ifs >> S >> K;
		int len = S.length();

		int counter = 0;
		int ii = 0;
		for (; ii < len - K + 1; ii++) {
			if (S[ii] == '-') {
				counter++;
				for (int jj = ii; jj < ii + K; jj++) {
					S[jj] = (S[jj] == '+') ? '-' : '+';
				}
			}
		}

		for (; ii < len; ii++) {
			if (S[ii] == '-') {
				ofs << "IMPOSSIBLE" << endl;
				return;
			}
		}

		ofs << counter << endl;
		return;
	}
};

void main(int argc, char* argv[]) {
	string fname_i = argv[1];
	string fname_o = fname_i.substr(0, fname_i.find_last_of(".")) + ".out";
	ifstream ifs(fname_i);
	ofstream ofs(fname_o);

	int T;
	ifs >> T;
	for (int No = 1; No <= T; No++) {
		ofs << "Case #" << No << ": ";
		cout << "Case #" << No << "...";
		Solver(ifs, ofs);
		cout << endl;
	}
}
