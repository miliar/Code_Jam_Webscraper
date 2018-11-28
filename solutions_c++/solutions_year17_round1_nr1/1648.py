#include <bits/stdc++.h>
using namespace std;
int main() {
	int t, i, j, r, c, mark[30], flag;
	string s[30];
	cin >> t;
	for(int test = 1; test <= t; test++) {
		cin >> r >> c;
		memset(mark, 0, sizeof(mark));
		for(i = 0; i < r; i++) {
			cin >> s[i];
		}
		for(i = 0; i < r; i++) {
			flag = -1;
			for(j = 0; j < c; j++) {
				if(s[i][j] != '?') {
					flag = j;
					break;
				}
			}
			if(flag == -1) {
				mark[i] = 1;
				continue;
			}
			for(j = 0; j < c; j++) {
				if(s[i][j] != '?') continue;
				if(j < flag) s[i][j] = s[i][flag];
				else s[i][j] = s[i][j - 1];
			}
		}
		flag = -1;
		for(i = 0; i < r; i++) {
			if(mark[i] == 0) {
				flag = i;
				break;
			}
		}
		for(i = 0; i < flag; i++) {
			for(int j = 0; j < c; j++)
				s[i][j] = s[flag][j];
		}
		for(i = flag + 1; i < r; i++) {
			if(mark[i] == 1)
				for(int j = 0; j < c; j++)
					s[i][j] = s[i - 1][j];
		}
		cout << "Case #" << test << ":" << endl;
		for(i = 0; i < r; i++)
			cout << s[i] << endl;
	}
}