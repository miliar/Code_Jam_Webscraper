#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<iomanip>
#include<list>
#include<tuple>

using namespace std;
#define PI 3.14159265258979

class Solver {
public:
	Solver(ifstream& ifs, ofstream& ofs) {
		int N;
		int K;

		ifs >> N >> K;

		vector<tuple<double, double, double, double>> P;

		for (int ii = 0; ii < N; ii++) {
			double r;
			double h;
			ifs >> r >> h;
			double s1 = PI * r * r;
			double s2 = 2 * PI * r * h;
			P.push_back(make_tuple(r, h, s1, s2));
		}

		sort(P.begin(), P.end(), [](
			const tuple<double, double, double, double> &x,
			const tuple<double, double, double, double> &y)
		{
			if (std::get<0>(x) != std::get<0>(y)) {
				return std::get<0>(x) > std::get<0>(y);
			}
			return std::get<1>(x) > std::get<1>(y);
		}
		);

		double max_s = 0;
		for (int ii = 0; ii < N - K + 1; ii++) {
			auto P2 = P;
			sort(P2.begin()+ii+1, P2.end(), [](
				const tuple<double, double, double, double> &x,
				const tuple<double, double, double, double> &y)
			{
				return std::get<3>(x) > std::get<3>(y);
			}
			);

			double s = std::get<2>(P2[ii]);
			for (int jj = ii; jj < ii + K; jj++) {
				s += std::get<3>(P2[jj]);
			}
			max_s = max(max_s, s);
		}

		ofs << fixed << setprecision(9) << max_s << endl;
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
