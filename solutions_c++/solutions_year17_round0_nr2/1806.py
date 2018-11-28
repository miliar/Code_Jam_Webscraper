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
		string s;
		ifs >> s;
		int n = 0;
		for (int j = 1; j < s.size(); j++) {
			if (s[j - 1] > s[j]) {
				if (s[j - 1] == '1') {
					int ssize = s.size();
					s = "";
					for (int h = 0; h < ssize - 1; h++) {
						s += "9";
					}
					break;
				}
				else {
					s[j - 1 - n]--;
					for (int h = 0; h + j - n < s.size(); h++) {
						s[h + j - n] = '9';
					}
					break;
				}
			}
			else if (s[j - 1] == s[j]) {
				n++;
			}
			else {
				n = 0;
			}
		}
		ofs << "Case #" << (i + 1) << ": ";
		ofs << s << endl;
	}

	return 0;
}