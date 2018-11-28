#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int main() {
	ifstream in;
	ofstream out;

	in.open("C:\\works\\in.txt");
	out.open("C:\\works\\out.txt");

	int n;

	in >> n;

	for (int i = 0; i < n; i++) {
		int r, c;
		in >> r;
		in >> c;
		bool first = true;
		vector<vector<char>> cake = vector<vector<char>>(r, vector<char>(c, 0));
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				char cell;
				in >> cake[j][k];
			}
		}
		int lastInit = -1;
		vector<int> lastInitPos;
		for (int j = 0; j < r; j++) {
			bool hasInit = false;
			vector<int> initPos = { -1 };
			for (int k = 0; k < c; k++) {
				if (cake[j][k] != '?') {
					hasInit = true;
					initPos.push_back(k);
				}
			}
			if (hasInit) {
				if (first) {
					first = false;
					for (int k = 1; k < initPos.size(); k++) {
						for (int m = initPos[k]; m > initPos[k - 1]; m--) {
							for (int a = j - 1; a >= 0; a--) {
								cake[a][m] = cake[j][initPos[k]];
							}
						}
						for (int m = initPos[initPos.size() - 1]; m < c; m++) {
							for (int a = j - 1; a >= 0; a--) {
								cake[a][m] = cake[j][initPos[initPos.size() - 1]];
							}
						}
					}
				}
				if (lastInit >= 0) {
					for (int k = 1; k < lastInitPos.size(); k++) {
						for (int m = lastInitPos[k]; m > lastInitPos[k - 1]; m--) {
							for (int a = j - 1; a >= lastInit; a--) {
								cake[a][m] = cake[lastInit][lastInitPos[k]];
							}
						}
						for (int m = lastInitPos[lastInitPos.size() - 1]; m < c; m++) {
							for (int a = j - 1; a >= lastInit; a--) {
								cake[a][m] = cake[lastInit][lastInitPos[lastInitPos.size() - 1]];
							}
						}
					}
				}
				lastInit = j;
				lastInitPos = initPos;
			}
		}
		for (int k = 1; k < lastInitPos.size(); k++) {
			for (int m = lastInitPos[k]; m > lastInitPos[k - 1]; m--) {
				for (int a = r - 1; a >= lastInit; a--) {
					cake[a][m] = cake[lastInit][lastInitPos[k]];
				}
			}
			for (int m = lastInitPos[lastInitPos.size() - 1]; m < c; m++) {
				for (int a = r - 1; a >= lastInit; a--) {
					cake[a][m] = cake[lastInit][lastInitPos[lastInitPos.size() - 1]];
				}
			}
		}
		out << "Case #" << i + 1 << ": ";
		for (int j = 0; j < r; j++) {
			out << endl;
			for (int k = 0; k < c; k++) {
				out << cake[j][k];
			}
		}
		out << endl;
	}
}