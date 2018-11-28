#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int ii = 0; ii < T; ++ii) {
		cout << "Case #" << ii + 1 << ":" << endl;
		int R, C;
		cin >> R >> C;
		vector<string> output;
		string curFillRow;
		string firstFillRow;
		char curFill;
		for (int rr = 0; rr < R; ++rr) {
			int lastInit = -1;
			for (int cc = 0; cc < C; ++cc) {
				char cell;
				cin >> cell;
				if (cell == '?') {
					if (curFillRow.length() < C && lastInit > -1) {
						curFillRow.push_back(curFill);
					}
					continue;
				}

				if (curFillRow.length() == C) curFillRow = "";
				curFill = cell;
				if (lastInit == -1) {
					for (int c2 = 0; c2 < cc; ++c2) {
						curFillRow.push_back(curFill);
					}
				}
				curFillRow.push_back(curFill);
				lastInit = cc;
			}
			if (curFillRow.length() > 0) {
				if (firstFillRow.length() == 0) {
					firstFillRow = curFillRow;
					for (int r2 = 0; r2 < rr; ++r2) {
						output.push_back(curFillRow);
					}
				}
				output.push_back(curFillRow);
			}
		}
		for (auto s : output) {
			cout << s << endl;
		}
	}
	return 0;
}