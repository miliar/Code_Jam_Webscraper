#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<iomanip>

using namespace std;

class Solver {
public:
	Solver(ifstream& ifs, ofstream& ofs) {
		double D;
		double N;
		ifs >> D >> N;

		double K = 0;

		for (int ii = 0; ii < N; ii++) {
			double a, b;
			ifs >> a >> b;
			K = max(K, (D - a) / b);
		}

		ofs << fixed << setprecision(6) << D / K << endl;
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
