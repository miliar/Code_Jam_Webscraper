#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream fin; fin.open("in.txt");
	ofstream fout; fout.open("out.txt");
	int n; fin >> n;
	for(int tc = 1; tc <= n; tc++) {
		string s; fin >> s;
		for(int i = s.size() - 1; i > 0; i--) {
			if(s[i] < s[i - 1]) {
				s[i - 1]--;
				for(int j = i; j < s.size(); j++) {
					s[j] = '9';
				}
			}
		}
		fout << "Case #" << tc << ": ";
		int start;
		for(start = 0; start < s.size(); start++) {
			if(s[start] != '0') break;
		}
		fout << s.substr(start) << endl;
	}
	return 0;
}