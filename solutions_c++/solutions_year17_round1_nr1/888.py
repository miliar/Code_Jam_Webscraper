#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <string.h>
#include <stack>
#include <list>

#define IMAX 1234567890

using namespace std;

int main(int argc, const char * argv[]) {
	int test;
	int check[26];
	string s[26];
	cin >> test;
	for (int z = 1; z <= test; z++) {
		int r, c;
		cin >> r >> c;
		memset(check, 0, sizeof(check));
		for (int i = 1; i <= r; i++) {
			cin >> s[i];
		}
		for (int i = 1; i <= r; i++) {
			int cnt = 0;
			for (int j = 0; j < c; j++) if (s[i][j] == '?') cnt++;
			if (cnt == c) {
				check[i] = 1;
				continue;
			}
			else {
				int k = 0;
				while (s[i][k] == '?') k++;
				for (int j = 0; j < k; j++) s[i][j] = s[i][k];
				char memo = s[i][k];
				for (int j = k + 1; j < c; j++) {
					if (s[i][j] == '?') s[i][j] = memo;
					else memo = s[i][j];
				}
			}
		}
		for (int i = 1; i <= r; i++) {
			if (i < r && check[i] == 1 && check[i + 1] == 0) {
				for (int j = 0; j < c; j++) s[i][j] = s[i + 1][j];
				check[i] = 0;
			}
			if (i > 1 && check[i] == 1 && check[i - 1] == 0) {
				for (int j = 0; j < c; j++) s[i][j] = s[i - 1][j];
				check[i] = 0;
			}
		}
		for (int i = r; i >= 1; i--) {
			if (i < r && check[i] == 1 && check[i + 1] == 0) {
				for (int j = 0; j < c; j++) s[i][j] = s[i + 1][j];
				check[i] = 0;
			}
			if (i > 1 && check[i] == 1 && check[i - 1] == 0) {
				for (int j = 0; j < c; j++) s[i][j] = s[i - 1][j];
				check[i] = 0;
			}
		}
		printf("Case #%d:\n", z);
		for (int i = 1; i <= r; i++) cout << s[i] << endl;
	}
	return 0;
}