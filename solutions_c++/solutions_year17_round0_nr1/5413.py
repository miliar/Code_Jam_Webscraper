// PancakeFlipper.cpp : Defines the entry point for the console application.
//

// #include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int n;
	cin >> n;

	string* outputs = new string[n];

	for (int i = 0; i < n; i++) {
		string s;
		int k;
		cin >> s;
		cin >> k;

		int flips = 0;

		for (int j = 0; j <= (s.length() - k); j++) {
			if (s[j] == '-') {
				flips++;
				for (int t = j; t < j+k; t++) {
					s[t] = (s[t] == '+') ? '-' : '+';
				}
			}
		}

		bool possible = true;

		for (int j = 0; j < s.length(); j++) {
			if (s[j] == '-') possible = false;
		}

		outputs[i] = "Case #" + to_string(i+1) + ": " + (possible ? to_string(flips) : "IMPOSSIBLE");
	}

	for (int i = 0; i < n; i++)
		cout << outputs[i] << endl;

	delete[] outputs;

	// system("PAUSE");

    return 0;
}

