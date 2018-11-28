//============================================================================
// Name        : cj2017b.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

long long n;

bool valid(string s) {
	for (int i = 0; i < s.length(); i++) {
		if(s[i] == '-')
			return false;
	}
	return true;
}

int solve(string s, int i) {
	if (i > s.length() - n) {
		if (valid(s))
			return 0;
		else
			return 10000000;
	}
	string changed = s;
	for (int j = i; j - i < n; j++) {
		if (changed[j] == '+')
			changed[j] = '-';
		else
			changed[j] = '+';
	}
	return min( solve(s,i+1), 1 + solve(changed, i+1) );
}

int main() {
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("outA.txt", "w", stdout);
	int t;
	int num = 0;
	cin >> t;
	while(t--) {
		string s;
		cin >> s >> n;
		int sol = solve(s,0);
		cout << "Case #" << ++num << ": ";
		if (sol == 10000000) {
			cout << "IMPOSSIBLE";
		} else {
			cout << sol;
		}
		cout << endl;
	}
	return 0;
}
