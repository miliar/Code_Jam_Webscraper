#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

using arr_1D = vector<char>;
using arr_2D = vector<arr_1D>;

int main() {
	ifstream input;
 	ofstream res;
	int T;
	input.open("./Downloads/B-small-attempt0.in");
	res.open("result_cj_20170422_Bs.out");
	input >> T;
	for (int t = 0; t < T; t ++) {
		int N, R, O, Y, G, B, V;
		input >> N >> R >> O >> Y >> G >> B >> V;
		arr_1D ret;
		if (O == 0 && G == 0 && V == 0) {
			if (R >= B && R >= Y && R <= B + Y) {
				for (int i = 0; i < R; i ++) {
					ret.push_back('R');
					if (i < B) {
						ret.push_back('B');
					}
					if (i >= R - Y) {
						ret.push_back('Y');
					}
				}	
			} else if (B >= R && B >= Y && B <= R + Y) {
				for (int i = 0; i < B; i ++) {
                                        ret.push_back('B');
                                        if (i < R) {
                                                ret.push_back('R');
                                        } 
                                        if (i >= B - Y) {
                                                ret.push_back('Y');
                                        }
                                }
			} else if (Y >= R && Y >= B && Y <= B + R) {
				for (int i = 0; i < Y; i ++) {
                                        ret.push_back('Y');
                                        if (i < R) {
                                                ret.push_back('R');
                                        } 
                                        if (i >= Y - B) {
                                                ret.push_back('B');
                                        }
                                }
			}
		}
		
		res << "Case #" << t + 1 << ": ";
		if (ret.empty()) {
			res << "IMPOSSIBLE" << endl;
		} else {
			for (int i = 0; i < ret.size(); i ++) {
				res << ret[i];
			}
			res << endl;
		}
	}
	input.close();
	res.close();
}
