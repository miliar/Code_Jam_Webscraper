// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>
#include <cstring>
using namespace std;
#define MX 20
int main()
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++) {
		char s[MX];
		cin >> s;
		char ret[MX];
		int len = strlen(s);
		strcpy(ret, s);
		for (int i = 0; i < len-1; i++) {
			if (s[i] > s[i + 1]) {
				int j = len-1;
				for (j; j >= 0 && (j>i || s[j] >= s[i]); j--)
					ret[j] = '9';
				ret[j + 1] = s[j+1] - 1;
				break;
			}
		}
		if (ret[0] == '0') {
			ret[0] = ' ';
		}
		cout << "Case #" << c << ": ";
		cout << ret << endl;
	}

    return 0;
}

