#include <iostream>
#include <fstream>
#include <string>
using namespace std;
string sol[100];
int main() {
	int T;
	cin >> T;
	string s;
	ofstream file;
	file.open("oo.in");
	for (int i = 0;i < T;i++) {
		int per = 0;
		cin >> s;
		for (int j = 0;j < s.length();j++) {

			if (int(s[j]) - 48 < per) {
				for (j=j-1;j >= 0 ;j--) {
					if (int(s[j]) - 48 < per) {
						j++;
						s[j] = char(int(s[j]) - 1);
						break;
					}
					if (j == 0) {
						s[j] = char(int(s[j]) - 1);
						break;
					}

				}
				
				for (j=j+1;j < s.length();j++) {
					s[j] = '9';
				}
			
			
			}
			per = int(s[j]) - 48;
		}
		sol[i] = s;

	}

	for (int i = 0;i < T;i++) {
		file << "Case #" << i + 1;
		file << ": ";
		int j = 0;
			while (sol[i][j] == '0') j++;
		for (;j < sol[i].size();j++)
			file << sol[i][j] ;
		file << endl;
	}
	return 0;
}