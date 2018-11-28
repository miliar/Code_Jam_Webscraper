#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<math.h>
#include<algorithm>
#include<iomanip>


using namespace std;

int main() {
	int t;
	ofstream ofs("out.txt");
	ifstream ifs("in.txt");
	ifs >> t;
	for (int i = 0; i < t; i++) {
		vector<string> s;
		int r, c;
		ifs >> r >> c;
		s.resize(r);
		for (int j = 0; j < r; j++)
			ifs >> s[j];
		ofs << "Case #" << (i + 1) << ": " << endl;
		int bR = 0;
		for (int j = 0; j < r; j++) {
			int count = 0;
			vector<int> chaIds;
			for (int k = 0; k < c; k++) {
				if (s[j][k] >= 'A' && s[j][k] <= 'Z') {
					count++;
					chaIds.push_back(k);
				}
			}
			int firstIndex = 0;
			for (int k = 0; k < chaIds.size(); k++) {
				for (int h = firstIndex; h < chaIds[k]; h++) {
					s[j][h] = s[j][chaIds[k]];
				}
				firstIndex = chaIds[k] + 1;
			}
			if (count > 0) {
				for (int k = firstIndex; k < c; k++) {
					s[j][k] = s[j][chaIds[chaIds.size() - 1]];
				}
				for (int k = bR; k < j; k++) {
					s[k] = s[j];
				}

				bR = j + 1;
			}
		}
		for (int j = bR; j < r; j++) {
			s[j] = s[bR - 1];
		}
		for (int j = 0; j < r; j++)
			ofs << s[j] << endl;
	}
	return 0;
}