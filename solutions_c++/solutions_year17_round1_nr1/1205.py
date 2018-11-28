#include <vector>
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("out.txt");

	int T;
	string temp;
	getline(in, temp);
	T = stoi(temp);

	int current = 1;
	while (T) {
		string s;
		getline(in, s);

		int R = stol(s.substr(0, s.find(" ")));
		int C = stol(s.substr(s.find(" ") + 1));

		vector<string> data(R);
		for (int i = 0; i < R; i++) {
			getline(in, s);
			data[i] = s;
		}

		vector<string> filled = data;

		// check each column
		for (int i = 0; i < C; i++) {
			bool empty_col = true;
			for (int j = 0; j < R; j++) {
				if (data[j][i] != '?') {
					empty_col = false;
					break;
				}
			}

			if (!empty_col) {
				char start_ch;
				for (int j = 0; j < R; j++) {
					if (data[j][i] != '?') {
						start_ch = data[j][i];
						break;
					}
				}

				for (int j = 0; j < R; j++) {
					if (data[j][i] == '?') data[j][i] = start_ch;
					else start_ch = data[j][i];
				}
			}
		}

		// Fill the empty cols 
		for (int i = 0; i < C; i++) {
			if (data[0][i] == '?') {
				for (int j = 0; j < R; j++) {
					char fill = '?';
					for (int k = i + 1; k < C; k++) {
						if (data[j][k] != '?') {
							fill = data[j][k];
							break;
						}
					}

					if (fill == '?') {
						for (int k = i - 1; k >= 0; k--) {
							if (data[j][k] != '?') {
								fill = data[j][k];
								break;
							}
						}
					}

					data[j][i] = fill;
				}
			}
		}

		T--;
		out << "Case #" << current << ":" << endl;
		current++;
		for (int i = 0; i < R; i++) {
			out << data[i] << endl;
		}

	}
}