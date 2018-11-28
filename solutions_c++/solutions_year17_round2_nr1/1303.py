#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

using arr_1D = vector<int>;
using arr_2D = vector<arr_1D>;

int main() {
	ifstream input;
 	ofstream res;
	int T;
	input.open("./Downloads/A-large.in");
	res.open("result_cj_20170422_Al.out");
	input >> T;
	for (int t = 0; t < T; t ++) {
		int D, N;
		input >> D >> N;
		arr_2D pos;
		for (int i = 0; i < N; i ++) {
			arr_1D pr(2, 0);
			input >> pr[0] >> pr[1];
			pos.push_back(pr);
		}
		double ret = -1;
		for (int i = 0; i < N; i ++) {
			double tmp = (double)(D - pos[i][0]) / pos[i][1];
			tmp = D / tmp;
			if (ret < 0 || tmp < ret) {
				ret = tmp;
			}
		}
		res << "Case #" << t + 1 << ": " << std::fixed << ret << endl;
	}
	input.close();
	res.close();
}
