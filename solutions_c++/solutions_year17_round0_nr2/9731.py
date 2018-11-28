#include "stdafx.h"
#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t;
	cin >> t;
	string s[110];
	string res[110];
	for (int i = 0; i < t; i++) {
		cin >> s[i];
		for (int j = s[i].length() - 1; j >= 1; j--) {
			if (s[i][j - 1] > s[i][j]) {
				s[i][j - 1]--;
				for (int k = j; k < s[i].length(); k++)
					s[i][k] = '9';
			}
		}
		int ins = i + 1;
		bool started = false;
		for (int j = 0; j < s[i].length(); j++) {
			if (s[i][j] != '0' || started==true) {
				res[i] += s[i][j];
				started = true;
			}
		}
	}
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i+1 << ": " << res[i] << "\n";
	}
	cout << res;
	return 0;
}

