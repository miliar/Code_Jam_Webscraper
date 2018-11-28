#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <string.h>
#include <iomanip>
#include <fstream>
using namespace std;

char s[2000];

void test() {
	ios::sync_with_stdio(false);
	fstream fin("C:\\Users\\BOSON\\Desktop\\A-small-attempt0.in", ios::in);
	fstream fout("C:\\Users\\BOSON\\Desktop\\A-small-attempt1.txt", ios::out);
	int t, k;
	//cin >> t; 
	fin >> t;
	cout << t << endl;
	int kase = 0;
	while (t--) {
		int ans = 0;
		//cin >> s; cin >> k;
		fin >> s; fin >> k;
		cout << s << ends << k << endl;
		int len = strlen(s);
		bool flag = false;
		for (int i = 0; i < len; ++i) {
			if (s[i] == '-') {
				if (i + k - 1 >= len) {
					//cout << "Case #" << ++kase << ": IMPOSSIBLE" << endl;
					cout << "Case #" << ++kase << ": IMPOSSIBLE" << endl;
					flag = true;
					break;
				}
				else {
					for (int j = i; j <= i + k - 1; ++j) {
						if (s[j] == '-') s[j] = '+';
						else if (s[j] == '+') s[j] = '-';
					}
					++ans;
				}
			}
		}
		if (flag) continue;
		//cout << "Case #" << ++kase << ": " << ans << endl;
		cout << "Case #" << ++kase << ": " << ans << endl;
	}
}

void test2() {
	ios::sync_with_stdio(false);
	fstream fin("C:\\Users\\BOSON\\Desktop\\B-small-attempt0.in", ios::in);
	fstream fout("C:\\Users\\BOSON\\Desktop\\B-small-attempt1.txt", ios::out);
	int t; fin >> t;
	int kase = 0;
	while (t--) {
		int a[10];
		int n; fin >> n;
		for (int i = n; i >= 1; --i) {
			int t = i, cnt = 0;
			while (t) {
				a[cnt++] = t % 10;
				t /= 10;
			}
			bool flag = true;
			for (int j = cnt - 1; j >= 1; --j) {
				if (a[j] > a[j - 1]) {
					flag = false; break;
				}
			}
			if (flag) {
				fout << "Case #" << ++kase << ": " << i << endl;
				break;
			}
		}
	}
}

int main() {
	test2();
	return 0;
}