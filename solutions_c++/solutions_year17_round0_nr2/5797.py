// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

char N[20];
char tidy[20];
int T;
int len;

int main()
{
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cin >> N;

		len = strlen(N);

		for (int j = 0; j < len; j++) tidy[j] = '9';
		
		//tidy[0] = N[0];

		int k;
		for (k = 1; k < len; k++) {
			if (N[k - 1] > N[k]) break;
		}
		if (k != len) {
			for (int j = 0; j < len; j++) {
				if (N[j] != N[k - 1]) tidy[j] = N[j];
				else {
					tidy[j] = N[k - 1] - 1;
					break;
				}
			}
		}
		else {
			for (int j = 0; j < len; j++) {
				tidy[j] = N[j];
			}
		}

		cout << "Case #" << i << ": ";

		if (len == 1) cout << N[0];
		else {
			if (tidy[0] != '0') cout << tidy[0];
			for (int j = 1; j < len; j++) cout << tidy[j];
		}
		cout << endl;
	}

	return 0;
}

