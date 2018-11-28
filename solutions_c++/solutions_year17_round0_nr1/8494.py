
/*
USER: nguyens1
PROG: nocows
LANG: C++
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("Out.txt");

	string pancakes[101];
	int T;
	int K[101];
	fin >> T;
	for (int i = 0; i < T; ++i) {
		fin >> pancakes[i];
		fin >> K[i];
	}

	//  for (int i = 0; i < T; ++i){
	//     cout << pancakes[i] << endl;
	//     cout <<  K[i] << endl;
	// }


	string tem;
	int count = 0;
	for (int i = 0; i < T; ++i) {
		tem = pancakes[i];
		count = 0;
		int len = tem.length();
		int flag = false;
		for (int j = 0; j < len; ++j) {
			if (tem[j] == '-') {

				if (len - j  < K[i]) {
					flag = true;
					fout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
					break;
				}

				for (int k = 0; k < K[i]; ++k) {

					if (tem[j + k] == '+')
						tem[j + k] = '-';
					else
						tem[j + k] = '+';
				}

				count++;
			}
		}
		if (!flag)
			fout << "Case #" << i + 1 << ": " << count << endl;
	}

	return 0;
}