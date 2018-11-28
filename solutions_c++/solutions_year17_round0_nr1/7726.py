#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int t, k;
int arr[2000];

int main() {
	ofstream fout;
	fout.open("output.txt");

	cin >> t;
	for (int i = 1; i <= t; i++) {
		string panCake;
		int cnt = 0;
		int flg = 0;
		cin >> panCake >> k;
		for (int j = 0; j <= panCake.length() - k; j++) {
			if (panCake[j] == '-') {
				for (int w = 0; w < k; w++) {
					if (panCake[j + w] == '+') panCake[j + w] = '-';
					else panCake[j + w] = '+';
				}
				cnt++;
			}
		}
		for (int p = 0; p < panCake.length(); p++) {
			if (panCake[p] == '-') {
				cout << "Case #" << i << ": IMPOSSIBLE" << endl;
				fout << "Case #" << i << ": IMPOSSIBLE" << endl;
				flg = 1;
				break;
			}
		}
		if (flg == 0) {
			cout << "Case #" << i << ": " << cnt << endl;
			fout << "Case #" << i << ": " << cnt << endl;
		}
	}



	fout.close();

	return 0;
}