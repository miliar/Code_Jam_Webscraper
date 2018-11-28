// TidyNumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;

		int k = 0;
		while (k < s.length()-1) {
			if (s[k] > s[k + 1]) {
				s[k] = s[k] - 1;
				k--;
				while (k >= 0 && s[k] > s[k + 1]) {
					s[k] = s[k] - 1;
					k--;
				}
				k+=2;
				while (k < s.length()) {
					s[k] = '9';
					k++;
				}
				break;
			}
			k++;
		}
		s.erase(0, s.find_first_not_of('0'));
		cout << "Case #" << to_string(i+1) << ": " << s << endl;
	}

    return 0;
}

