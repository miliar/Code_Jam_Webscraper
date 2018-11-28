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
		int N;
		int K;

		ifs >> N >> K;

		double U;

		ifs >> U;

		vector<double> P;

		for (int ii = 0; ii < N; ii++) {
			double p;
			ifs >> p;
			P.push_back(p);
		}

		sort(P.begin(), P.end(), [](const double &x, const double &y)
		{
			return x > y;
		}
		);

		for (int ii = 0; ii < N; ii++) {
			double limit = P[ii];
			double sum_u = 0;
			for (int jj = ii + 1; jj < N; jj++) {
				sum_u += limit - P[jj];
			}
			if (U - sum_u > - 0.0000001) {
				for (int jj = ii + 1; jj < N; jj++) {
					P[jj] = limit;
				}
				U -= sum_u;
				double add_u = U / (double)(N - ii);
				for (int jj = ii; jj < N; jj++) {
					P[jj] += add_u;
				}
				break;
			}
		}
		double result = 1;
		for (auto p : P) {
			result *= p;
		}

		ofs << fixed << setprecision(6) << result << endl;
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
