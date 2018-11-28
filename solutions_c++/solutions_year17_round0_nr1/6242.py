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
		int k; fin >> k;
		int count = 0;
		for(int i = 0; i <= s.size() - k; i++) {
			if(s[i] == '+') continue;
			count ++;
			for(int j = 0; j < k; j++) {
				if(s[i + j] == '+') {
					s[i + j] = '-';
				} else {
					s[i + j] = '+';
				}
			}
		}
		bool succ = true;
		for(int i = 0; i < s.size(); i++) {
			succ = succ && s[i] == '+';
		}
		fout << "Case #" << tc << ": ";
		if(succ)
			fout << count << endl;
		else
			fout << "IMPOSSIBLE" << endl;
	}
	return 0;
}