// google_code_jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool non_dec(long long n) {
	while (1) {
		if (n < 10) return true;

		long long last = n % 10;
		n = n / 10;
		long long sLast = n % 10;
		if (sLast > last) return false;
		continue;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	long long n;
	cin >> t;  
	for (int i = 1; i <= t; ++i) {
		cin >> n;  
		long long* numbers = new long long[100];
		memset(numbers, 0, sizeof(numbers));
		int pos = 0;

		while (1) {
			if (non_dec(n)) {
				numbers[pos++] = n;
				break;
			}
			else {
				numbers[pos++] = 9;
				n = n / 10 - 1;
				continue;
			}
		}

		long long y = 0;
		for (int k = pos-1; k >= 0; k--) {
			y = y * 10 + numbers[k];
		}

		cout << "Case #" << i << ": " << y << endl;
	}

	return 0;
}

