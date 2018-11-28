#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

using arr_1d = vector<double>;
using arr_2d = vector<arr_1d>;

bool myComp(arr_1d const & A, arr_1d const & B)
{
	return A[0] < B[0];
}

int main() {
	ifstream input;
	ofstream res;
	int T;
	input.open("./Downloads/A-large.in");
	res.open("result_cj_20170430_Al.out");
	input >> T;
	for (int t = 0; t < T; t ++) {
		int N, K;
		input >> N >> K;
		arr_2d d_r;
		for (int i = 0; i < N; i ++) {
			double R, H;
			input >> R >> H;
			arr_1d tmp(2, 0);
			tmp[0] = H * R * 2 * M_PI;
			tmp[1] = R * R * M_PI;
			d_r.push_back(tmp);
		}
		sort(d_r.begin(), d_r.end(), myComp);
		int cnt = 0;
		double ret = 0;
		double l = 0;
		double max = -1;
		for (int i = N - 1; i >= 0; i --) {
			cnt ++;
			if (cnt < K) {
				if (max < d_r[i][1]) {
                                	max = d_r[i][1];
                        	}
				ret += d_r[i][0];
			} else if (cnt == K) {
				if (max < d_r[i][1]) {
					max = d_r[i][1]; 
				}
				l = d_r[i][0];
				
			} else if (l + max < d_r[i][0] + d_r[i][1]) {
				l = d_r[i][0];
				max = d_r[i][1];
				
			}
		}
		ret += l + max;
                res << "Case #" << t + 1 << ": " << std::fixed << ret << endl;
	}
	input.close();
	res.close();
}
