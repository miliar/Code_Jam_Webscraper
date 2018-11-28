#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;
string s[50];
int main() {
	int T, R, C;
	ofstream out("answer.txt");
	cin >> T;
	int i, j, k, t;
	int kase = 0, ans;
	while (T--) {
		t = 0;
		cin >> R >> C;
		for (i = 0; i < R; i++) {
			cin >> s[i];
			for (j = 0; j < C; j++) {
				if (s[i][j] == '?')
					t++;
			}
		}
		while (t > 0) {
			for (i = 0; i < R; i++) {
				for (j = 0; j < C; j++) {
					if (s[i][j] != '?') {
						k = j - 1;
						while (k >= 0 && s[i][k] == '?') {
							t--;
							s[i][k] = s[i][j];
							k--;
						}
						k = j + 1;
						while (k < C && s[i][k] == '?') {
							t--;
							s[i][k] = s[i][j];
							k++;
						}
					}
				}
			}
			for (j = 0; j < C; j++) {
				for (i = 0; i < R; i++) {
					if (s[i][j] != '?') {
						k = i - 1;
						while (k >= 0 && s[k][j] == '?') {
							t--;
							s[k][j] = s[i][j];
							k--;
						}
						k = i + 1;
						while (k < R && s[k][j] == '?') {
							t--;
							s[k][j] = s[i][j];
							k++;
						}
					}
				}
			}
		}
		out << "Case #" << (++kase) << ": " << endl;
		for (i = 0; i < R; i++) {
			out << s[i] << endl;
		}

	}
	out.close();
	return 0;
}
