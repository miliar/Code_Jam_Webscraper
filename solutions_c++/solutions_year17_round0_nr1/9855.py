#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int coun[1000];
int main() {
	ofstream file;
	file.open("ou.in");
	int n;
	cin >> n;
	string s;
	int spoon ;
	for (int i = 0;i < n;i++) {
		cin >> s;
		cin >> spoon;
		int c = 0;
		for (int j = 0;j < s.size();j++) {
			if (s[j] == '-') {
				if (spoon + j > s.size()) {
					coun[i] = -1;
					break;
				}
				for (int k = 0;k < spoon;k++) {
					s[k+j] = s[k+j] == '-' ? '+' : '-';
				}
				c++;
			}
			coun[i]=coun[i] != -1 ? c : -1;


		}
	}

	for (int i = 0;i < n;i++) {
		file << "Case #" << (i + 1) ;
		if (coun[i] == -1) {
			file << ": IMPOSSIBLE\n";
		}
		else {
			file <<": " <<coun[i] << "\n";
		}
	}

	return 0;
}