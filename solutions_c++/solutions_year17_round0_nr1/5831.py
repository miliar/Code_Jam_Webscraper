// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

char pancakes[1111];
int T;
int K;
int len;
int uses;

int main()
{
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cin >> pancakes;
		cin >> K;

		uses = 0;

		len = strlen(pancakes);

		for (int j = 0; j < len - K + 1; j++) {
			if (pancakes[j] == '-') {
				uses++;
				for (int k = 0; k < K; k++) {
					if (pancakes[j + k] == '-') pancakes[j + k] = '+';
					else pancakes[j + k] = '-';
				}
			}
		}

		for (int j = len - K + 1; j < len; j++) {
			if (pancakes[j] == '-') uses = -1;
		}


		cout << "Case #" << i << ": ";
		if (uses == -1) cout << "IMPOSSIBLE";
		else cout << uses;
		cout << endl;
	}

    return 0;
}

