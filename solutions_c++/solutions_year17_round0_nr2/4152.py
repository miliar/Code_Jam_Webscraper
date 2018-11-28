// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

int t;

int main()
{
	cin >> t;
	for (int testcase = 0; testcase < t; testcase++) {
		int n;
		cin >> n;
		for (int i = n; i > 0; i--) {
			string a = to_string(i);
			bool ok = true;
			for (int j = 1; j < a.length(); j++) {
				if (a[j - 1] > a[j]) {
					ok = false;
					break;
				}
			}
			if (ok) {
				cout << "Case #" << testcase << ": " << i << endl;
				break;
			}
		}
	}
	return 0;
}

