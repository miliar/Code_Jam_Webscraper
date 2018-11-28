#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

using arr_1d = vector<int>;
using arr_2d = vector<arr_1d>;

bool myComp(arr_1d const & A, arr_1d const & B)
{
	return A[0] < B[0];
}

int main() {
	ifstream input;
	ofstream res;
	int T;
	input.open("./Downloads/B-small-attempt0.in");
	res.open("result_cj_20170430_Bs.out");
	input >> T;
	for (int t = 0; t < T; t ++) {
		int AC, AJ;
		input >> AC >> AJ;
		arr_2d day;
		int C_c = 0;
		int J_c = 0;
		int S, E;
		for (int i = 0; i < AC; i ++) {
			arr_1d tmp(3, 0);
			input >> tmp[0] >> tmp[1];
			tmp[2] = 1;
			J_c += tmp[1] - tmp[0];
                        day.push_back(tmp);
		}
		for (int i = 0; i < AJ; i ++) {
			arr_1d tmp(3, 0);
                        input >> tmp[0] >> tmp[1];
                        tmp[2] = 2;
                        C_c += tmp[1] - tmp[0];
                        day.push_back(tmp);
		}
		sort(day.begin(), day.end(), myComp);
		int ret = 0;
		for (int i = 0; i < day.size(); i ++) {
			if (i + 1 < day.size()) {
				if (day[i][2] != day[i + 1][2]) {
					ret ++;
				} else if (day[i + 1][1] - day[i][0] > 720) {
					ret += 2;
				} else if (day[i + 1][2] == day[i][2]){
					if (day[i][2] == 1) {
						J_c += day[i + 1][0] - day[i][1];
					} else {
						C_c += day[i + 1][0] - day[i][1];
					}
				}
			}
		}
		cout << J_c << "," << C_c << endl;
		if ((day[0][2] == 1 && J_c + day[0][0] > 720) || (day[0][2] == 2 && C_c + day[0][0] > 720)) {
			ret ++;
			if (day[0][2] == 1) {
				S = 2;
			} else {
				S = 1;
			}
		} else {
			S = day[0][2];
			if (day[0][2] == 1) {
				J_c += day[0][0];
			} else {
				C_c += day[0][0];
			}
		}
		if ((day.back()[2] == 1 && J_c + (1440 - day.back()[1]) > 720) || (day.back()[2] == 2 && C_c + (1440 - day.back()[1]) > 720)) {
                        if (day.back()[2] == 1) {
                                E = 2;
                        } else {
                                E = 1;
                        }
			ret ++;
                } else {
			E = day.back()[2];
		}
		if (S != E) {
			ret ++;
		}
		
                res << "Case #" << t + 1 << ": " << ret << endl;
	}
	input.close();
	res.close();
}
