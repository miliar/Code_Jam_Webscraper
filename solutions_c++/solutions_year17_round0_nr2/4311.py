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


void solve(string &s, int pos) {
	if (pos == 0) return;

	if (s[pos - 1] <= s[pos])
		return;

	s[pos] = '9';
	--s[pos - 1];

	solve(s, pos - 1);
}

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
		string s;
		IN >> s;
		
		int pos = 1;
		for (int i = 1; i < s.length(); i++) {
			if (s[i] < s[i - 1])
				break;
			pos++;
		}

		if (pos != s.length()) {
			for (int i = pos; i < s.length(); i++)
				s[i] = '9';
			--s[pos - 1];
			solve(s, pos - 1);
		}

		reverse(s.begin(), s.end());
		while (s.size() > 1 && s.back() == '0') {
			s.pop_back();
		}
		reverse(s.begin(), s.end());

		OUT << "Case #" << t + 1 << ": " << s << endl;
	}

#ifndef CONSOLE
	IN.close();
	OUT.close();
#endif

	system("pause");
	return 0;
}

