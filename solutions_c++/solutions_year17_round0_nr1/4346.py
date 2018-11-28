// Codejam_Sample.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <limits.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

//#define CONSOLE

#define IN		cin
#define OUT		cout

int main() {
#ifndef CONSOLE
	fstream IN, OUT;
	IN.open("inB.txt", ios::in);
	OUT.open("outB.txt", ios::out);
#endif

	/*
	*
	*	START CODE HERE
	*
	*/

	int T; IN >> T;
	for (int t = 0; t < T; t++) {
		string s; int k;
		IN >> s >> k;

		int res = 0;
		for (int i = 0; i < s.length() - k + 1; i++) {
			if (s[i] == '-') {
				res++;
				for (int j = i; j < i + k; j++) {
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
			}
		}

		bool complete = true;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				complete = false;
				break;
			}
		}

		if (complete)
			OUT << "Case #" << t + 1 << ": " << res << endl;
		else
			OUT << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
	}


#ifndef CONSOLE
	IN.close();
	OUT.close();
#endif

	system("pause");
	return 0;
}

