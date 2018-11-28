#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <cstring>

using namespace std;


int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int qwer; cin >> qwer;

	for (int tc = 1; tc <= qwer; tc++) {

		int r, c; cin >> r >> c;
		char d[30][30] = { 0 };

		for (int i = 1; i <= r; i++) cin >> d[i] + 1;

		for (int i = 1; i <= r; i++) {
			int flag = 0;

			for (int j = 1; j <= c; j++) if (d[i][j] != '?') flag = 1;

			if (flag == 0) continue;

			char temp = 0;

			for (int j = 1; j <= c; j++) {
				if (temp == 0 && d[i][j] == '?') continue;
				else if (temp == 0 && d[i][j] != '?') {
					for (int k = j - 1; k >= 1; k--) d[i][k] = d[i][j]; temp = d[i][j];
				}
				else if (d[i][j] == '?') d[i][j] = temp;
				else temp = d[i][j];
			}
		}

		for (int i = 1; i <= r; i++) {

			int flag = 0;

			for (int j = 1; j <= c; j++) if (d[i][j] != '?') flag = 1;

			if (flag == 1) continue;

			if (i == 1) {
				for (int j = 2; j <= r; j++) {
					if (d[j][1] != '?') {
						for (int k = 1; k <= c; k++) d[i][k] = d[j][k];
						break;
					}
				}
			}
			else for (int j = 1; j <= c; j++) d[i][j] = d[i - 1][j];
		}


		cout << "Case #" << tc << ":\n";

		int flag = 0;

		for(int i = 1 ; i<= r ; i++)
			for (int j = 1; j <= c; j++) 
				if (d[i][j] == '?') flag = 1;

		if (flag == 1) 
			for (int i = 1; i <= r; i++) {
				for (int j = 1; j <= c; j++) cout << '?';
				cout << endl;
			}
		else
			for (int i = 1; i <= r; i++) {
				for (int j = 1; j <= c; j++) cout << d[i][j];
				cout << endl;
			}
	}

	return 0;
}