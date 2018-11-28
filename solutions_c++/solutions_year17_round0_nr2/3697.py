// q2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "string"
using namespace std;


int main()
{
	int T;
	string S;


	cin >> T;

	for (int Tl = 1; Tl <= T; ++Tl) {
		cin >> S;

		int ch;
		int i;
		int rep = S.length();

		ch = '9';

		for (i = S.length() - 1; i >= 0; --i) {
			/*if (S[i] == '0') {
				// zero rule
				S = string(S.length() - 1, '9');
				break;
			} else */
			if (S[i] <= ch) {
				ch = S[i];
			}
			else {
				ch = --S[i];
				rep = i + 1;
			}
		}

		if (rep != S.length()) {
			if (S[0] == '0') {
				S = string(S.length() - 1, '9');
			}
			else {

				for (; rep < S.length(); ++rep) S[rep] = '9';
			}
		}


		cout << "Case #" << Tl << ": ";
		cout << S;
		cout << endl;
	}
	return 0;
}

