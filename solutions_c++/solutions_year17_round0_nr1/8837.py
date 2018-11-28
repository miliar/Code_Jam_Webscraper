//============================================================================
// Name        : .cpp
// Author      : Omar Ahmed
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
//#define SMALL
#define LARGE
//#define FILE
using namespace std;
bool check(string s);
int main() {
#ifdef SMALL
	freopen("C:\\Users\\HP\\Downloads\\A-small-attempt0.in", "rt", stdin);
#endif
#ifdef LARGE
	freopen("C:\\Users\\HP\\Downloads\\A-large.in", "rt", stdin);
#endif
#ifdef FILE
	freopen("input.txt", "rt", stdin);
#endif
	freopen("output.txt", "wt", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int K, count = 0;
		string s;
		cin >> s >> K;
		for (unsigned int i = 0; i < s.length(); i++) {
			if (s[i] == '-' && i + K <= s.length()) {
				count++;
				for (unsigned int j = i; j < K + i && j < s.length(); j++) {
					s[j] = s[j] == '-' ? '+' : '-';
				}
			}
		}
		if (check(s)) {
			cout << "Case #" << t + 1 << ": " << count << endl;
		} else {
			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
bool check(string s) {
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == '-')
			return false;
	}
	return true;
}

