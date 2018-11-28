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
	input.open("./Downloads/C-small-attempt1.in");
	res.open("result_cj_20170422_Cs.out");
	input >> T;
	for (int t = 0; t < T; t ++) {
		int N, Q;
		input >> N >> Q;
		arr_1D rw(N, 0);
		arr_2D mp(N, rw);
		arr_1D sn(N, 0);
		arr_1D en(N, 0);
		vector<double> rwd(N, -1);
		vector<vector<double> > mpd(N, rwd);
		vector<double> ret;
		for (int i = 0; i < N; i ++) {
			input >> en[i] >> sn[i];
		}
		for (int i = 0; i < N; i ++) {
			for (int j = 0; j < N; j ++) {
				input >> mp[i][j];
			}
		}
		for (int i = 0; i < Q; i ++) {
			int U, V;
			input >> U >> V;
			double tmp = 0;
			vector<double> res_t;
			vector<double> rm_t;
			
			for (int j = 1; j < N; j ++) {
				if (en[j - 1] >= mp[j - 1][j]) {
					res_t.push_back(tmp + ((double)mp[j - 1][j]) / sn[j - 1]);
					rm_t.push_back(en[j - 1] - mp[j - 1][j]);
					tmp = tmp + ((double)mp[j - 1][j]) / sn[j - 1];
				} else {
					tmp = -1;
					res_t.push_back(0);
					rm_t.push_back(-1);
				}
				for (int k = 0; k + 1 < res_t.size(); k ++) {
					if (rm_t[k] >= mp[j - 1][j] && rm_t[k] >= 0) {
						rm_t[k] = rm_t[k] - mp[j - 1][j];
						res_t[k] = res_t[k] + ((double)mp[j - 1][j]) / sn[k];
						if (tmp < 0 || tmp > res_t[k]) {
							tmp = res_t[k];
						}
					} else {
						rm_t[k] = -1;
					}
				}
			}
			tmp = -1;
			for (int j = 0; j < res_t.size(); j ++) {
				if ((tmp < 0 || tmp >= res_t[j]) && rm_t[j] >= 0) {
					tmp = res_t[j];
				}
			}
			ret.push_back(tmp);
		}

		res << "Case #" << t + 1 << ": " << std::fixed;
		for (int i = 0; i < ret.size(); i ++) {
			res << ret[i] << " ";
		}
		res << endl;
	}
	input.close();
	res.close();
}
