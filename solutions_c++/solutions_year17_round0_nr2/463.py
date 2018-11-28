#include<iostream>
#include<fstream>
#include<vector>
#include<string>

using namespace std;

class Solver {
public:
	Solver(ifstream& ifs, ofstream& ofs) {
		long long int N_int;
		ifs >> N_int;
		string N = to_string(N_int);
		int len = N.length();

		for (int ii = len - 1; ii > 0; ii--) {
			if (N[ii] < N[ii - 1]) {
				for (int jj = ii; jj < len; jj++) {
					N[jj] = '9';
				}
				N[ii - 1] = (N[ii - 1] == '0') ? '9' : N[ii - 1] - 1;
			}
		}

		int ii = 0;
		for (; ii < len; ii++) {
			if (N[ii] != '0') break;
		}
		for (; ii < len; ii++) {
			ofs << N[ii];
		}
		ofs << endl;
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
