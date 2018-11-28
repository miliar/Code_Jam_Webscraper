#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;

string str;
int T;

string tidy(string str) {
	int n = 0;
	int p = 0;
	while (n<str.size()-1) {
		if (str[n] > str[n + 1])
		{
			for (int i = n + 1; i <= str.size() - 1; i++) {
				str[i] = '9';
			}
			char tmp = str[n];
			str[n] = str[n] - 1;
			while (n>0&&str[n-1]==tmp) {
				str[n] = '9';
				n--;
			}
			if (str[n] == tmp)str[n] = str[n] - 1;
			break;
		}
		n++;
	}
	if (str[0] == '0') {
		return str.substr(1,str.size()-1);
	}
	else return str;
}

int main() {
	cin >> T;
	for (int i = 1; i <=T;i++) {
		cin >> str;
		string res=tidy(str);

		cout << "Case #" << i << ": " << res << endl;
	}

	return 0;
}