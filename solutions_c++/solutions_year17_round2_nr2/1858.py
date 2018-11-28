#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<list>

using namespace std;

class Solver {
public:
	Solver(ifstream& ifs, ofstream& ofs) {
		int N;
		ifs >> N;
		int R, O, Y, G, B, V;
		ifs >> R >> O >> Y >> G >> B >> V;

		if (R * 2 > N) { ofs << "IMPOSSIBLE" << endl; return; }
		if (Y * 2 > N) { ofs << "IMPOSSIBLE" << endl; return; }
		if (B * 2 > N) { ofs << "IMPOSSIBLE" << endl; return; }

		if ((G != 0) && (G == R) && (V + Y + O + B > 0)) { ofs << "IMPOSSIBLE" << endl; return; }
		if ((V != 0) && (V == Y) && (G + R + O + B > 0)) { ofs << "IMPOSSIBLE" << endl; return; }
		if ((O != 0) && (O == B) && (G + R + V + Y > 0)) { ofs << "IMPOSSIBLE" << endl; return; }

		if (G > R) { ofs << "IMPOSSIBLE" << endl; return; }
		if (V > Y) { ofs << "IMPOSSIBLE" << endl; return; }
		if (O > B) { ofs << "IMPOSSIBLE" << endl; return; }

		string ans_G;
		while (G > 0 && R > 0) {
			ans_G.push_back('R'); R--; N--;
			ans_G.push_back('G'); G--; N--;
		}
		if (R > 0) {
			ans_G.push_back('R'); R--; N--;
		}
		if (G > 0) {
			ofs << 'G' << ans_G << endl;
			return;
		}

		string ans_V;
		while (V > 0 && Y > 0) {
			ans_V.push_back('Y'); V--; N--;
			ans_V.push_back('V'); Y--; N--;
		}
		if (Y > 0) {
			ans_V.push_back('Y'); Y--; N--;
		}
		if (V > 0) {
			ofs << 'V' << ans_V << endl;
			return;
		}

		string ans_O;
		while (O > 0 && B > 0) {
			ans_O.push_back('B'); B--; N--;
			ans_O.push_back('O'); O--; N--;
		}
		if (B > 0) {
			ans_O.push_back('B'); B--; N--;
		}
		if (O > 0) {
			ofs << 'O' << ans_O << endl;
			return;
		}

		int num_R = (ans_G.size() == 0) ? R : R + 1;
		int num_Y = (ans_V.size() == 0) ? Y : Y + 1;
		int num_B = (ans_O.size() == 0) ? B : B + 1;
		int num_N = num_R + num_Y + num_B;

		vector<string> ans;
		ans.resize(num_N);

		if (num_R == max({ num_R, num_Y, num_B })) {
			for (int ii = 0; ii < num_N; ii += 2) {
				ans[ii] = (ans_G.size() == 0) ? "R" : ans_G;
				ans_G.clear();
				num_R--;
				if (num_R == 0) break;
			}
		}
		else if (num_Y == max({ num_R, num_Y, num_B })) {
			for (int ii = 0; ii < num_N; ii += 2) {
				ans[ii] = (ans_V.size() == 0) ? "Y" : ans_V;
				ans_V.clear();
				num_Y--;
				if (num_Y == 0) break;
			}
		}
		else if (num_B == max({ num_R, num_Y, num_B })) {
			for (int ii = 0; ii < num_N; ii += 2) {
				ans[ii] = (ans_O.size() == 0) ? "B" : ans_O;
				ans_O.clear();
				num_B--;
				if (num_B == 0) break;
			}
		}

		if (num_R + num_Y + num_B != 0) {
			int start_N = (num_N % 2 == 0) ? num_N - 1 : num_N - 2;
			if (num_R == max({ num_R, num_Y, num_B })) {
				for (int ii = start_N; ii >= 0; ii -= 2) {
					ans[ii] = (ans_G.size() == 0) ? "R" : ans_G;
					ans_G.clear();
					num_R--;
					if (num_R == 0) break;
				}
			}
			else if (num_Y == max({ num_R, num_Y, num_B })) {
				for (int ii = start_N; ii >= 0; ii -= 2) {
					ans[ii] = (ans_V.size() == 0) ? "Y" : ans_V;
					ans_V.clear();
					num_Y--;
					if (num_Y == 0) break;
				}
			}
			else if (num_B == max({ num_R, num_Y, num_B })) {
				for (int ii = start_N; ii >= 0; ii -= 2) {
					ans[ii] = (ans_O.size() == 0) ? "B" : ans_O;
					ans_O.clear();
					num_B--;
					if (num_B == 0) break;
				}
			}

			if (num_R != 0) {
				for (int ii = 0; ii < num_N; ii++) {
					if (ans[ii].size()) continue;
					ans[ii] = (ans_G.size() == 0) ? "R" : ans_G;
					ans_G.clear();
					num_R--;
					if (num_R == 0) break;
				}
			}
			else if (num_Y != 0) {
				for (int ii = 0; ii < num_N; ii++) {
					if (ans[ii].size()) continue;
					ans[ii] = (ans_V.size() == 0) ? "Y" : ans_V;
					ans_V.clear();
					num_Y--;
					if (num_Y == 0) break;
				}
			}
			else if (num_B != 0) {
				for (int ii = 0; ii < num_N; ii++) {
					if (ans[ii].size()) continue;
					ans[ii] = (ans_O.size() == 0) ? "B" : ans_O;
					ans_O.clear();
					num_B--;
					if (num_B == 0) break;
				}
			}
		}


		for (auto& v : ans) {
			ofs << v;
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
