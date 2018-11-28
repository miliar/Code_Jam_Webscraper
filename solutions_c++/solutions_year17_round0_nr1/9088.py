#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <fstream>

using namespace std;

typedef long long LL;
typedef vector<LL> VLL;
typedef vector< VLL > matrix;

string pancake;

bool isHappy(string&);
void flip(LL);

int main() {
	LL T;

	FILE* fr;
	FILE* fo;
	ifstream fin;
	ofstream fout;

	fin.open("A-large.in");
	fout.open("output.txt");

	fin >> T;

	for (LL i = 1; i <= T; i++) {
		LL k = 0;
		fout << "Case #" << i << ": ";

		fin >> pancake >> k;

		LL ans = 0;
		while (!isHappy(pancake)) {
			flip(k);


			//Debug
			//cout << pancake << endl;


			ans++;

			if (ans >= 10000) {
				fout << "IMPOSSIBLE" << endl;
				break;
			}
		}
		if (ans >= 10000) {
			continue;
		}
		cout << i << " :" <<ans << endl;

		fout << ans << endl;
	}
	

	return 0;
}

bool isHappy(string& str) {
	for (int i = 0; i < str.size(); i++) {
		if (str[i] == '-') {
			return false;
		}
	}
	return true;
}

void flip(LL k) {
	for (int i = 0; i < pancake.size()-k+1; i++) {
		if (pancake[i] == '-') {

			for (int j = 0; j < k; j++) {
				if (pancake[i + j] == '-') {
					pancake[i + j] = '+';
				}
				else {
					pancake[i + j] = '-';
				}
			}
			return;
		}

	}
}