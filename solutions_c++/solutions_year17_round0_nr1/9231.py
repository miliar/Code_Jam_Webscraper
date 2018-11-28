// OPP.cpp: Okreœla punkt wejœcia dla aplikacji konsoli.
//

#include "stdafx.h"
#include<iostream>
#include<string>
using namespace std;
string s;
int k;
int results[110];
inline void flip(int x,int y) {
	for (int i = x; i < y; i++) {
		if (s[i] == '-')
			s[i] = '+';
		else {
			s[i] = '-';
		}
	}
}
inline int flipper() {
	int res = 0;
	cin >> s >> k;
	for (int i = 0; i <= s.length() - k; i++) {
		if (s[i] == '-') {
			flip(i, i + k);
			res++;
		}
	}
	for (int i = s.length() - k; i < s.length() - 1; i++) {
		if (s[i] != s[i + 1])
			return -1;
	}
	//cout << s << "\n";
	return res;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) 
		results[i] = flipper();
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		if (results[i] == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << results[i] << "\n";
	}
	return 0;
}

