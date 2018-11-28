#include<fstream>
using namespace std;

int main(){
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int t = 0;
	fin >> t;

	char s[20];
	for (int kk = 1; kk <= t; kk++) {
		fin >> s;
		int l = strlen(s);
		bool mark = true;
		int i = 1;
		for (i = 1; i < l; i++) {
			if(s[i] < s[i - 1]) {
				mark = false;
				break;
			}
		}
		if (mark) {
			fout << "Case #" << kk << ": " << s << endl;
		} else {
			i--;
			while (i > 0 && s[i] == s[i-1]) {
				i--;
			}
			if (s[i] > '1') {
				s[i] = s[i] - 1;
				for (int j = i + 1; j < l; j++) {
					s[j] = '9';
				}
			} else {
				for (int j = 0; j < l - 1; j++) {
					s[j] = '9';
				}
				s[l - 1] = '\0';
			}
			fout << "Case #" << kk << ": " << s << endl;
		}
	}
	return 0;
}